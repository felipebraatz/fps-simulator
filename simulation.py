# simulation.py

import random
import copy
from data import WEAPONS, find_weapon_by_id

WIN_REWARD = 3000
LOSS_REWARD = 1900
STARTING_CREDITS = 800
MAX_CREDITS = 9000

def determine_economy_type(average_credits):
    """Determina o tipo de economia com base na média de créditos."""
    if average_credits < 2000: return 'Full Eco'
    if average_credits < 3900: return 'Semi Buy'
    return 'Full Buy'

def buy_weapons_for_team(team):
    """Lógica de compra de armas para um time, baseada em a1.ts."""
    avg_credits = sum(p['credits'] for p in team['players']) / len(team['players'])
    eco_type = determine_economy_type(avg_credits)
    
    for player in team['players']:
        # Sobreviventes mantêm suas armas, a menos que seja uma pistola e a equipe esteja em Full Buy.
        if player['is_alive'] and player['weapon']['type'] != 'Sidearm' and player['weapon']['cost'] > 0:
            continue

        affordable_weapons = []
        if eco_type == 'Full Eco':
            affordable_weapons = [w for w in WEAPONS if w['cost'] <= player['credits'] and w['type'] == 'Sidearm' and w['id'] != 'classic']
        elif eco_type == 'Semi Buy':
            affordable_weapons = [w for w in WEAPONS if w['cost'] <= player['credits'] and (w['type'] in ['SMG', 'Shotgun'] or w['id'] in ['bulldog', 'guardian'])]
        elif eco_type == 'Full Buy':
            # Duelistas e Flex com alta mira podem priorizar a Operator
            if player['role'] in ['Duelist', 'Flex'] and player['attributes']['aim'] > 78 and player['credits'] >= 4700:
                 affordable_weapons = [w for w in WEAPONS if w['id'] == 'operator']
            if not affordable_weapons: # Se não comprou Operator ou não pode
                affordable_weapons = [w for w in WEAPONS if w['cost'] <= player['credits'] and w['type'] == 'Rifle']

        # Se não puder comprar armas primárias na categoria, busca qualquer opção melhor que a classic
        if not affordable_weapons and eco_type != 'Full Eco':
            affordable_weapons = sorted([w for w in WEAPONS if w['cost'] <= player['credits'] and w['cost'] > 0], key=lambda x: x['cost'], reverse=True)

        chosen_weapon = max(affordable_weapons, key=lambda x: x['cost']) if affordable_weapons else None
        
        if chosen_weapon:
            player['credits'] -= chosen_weapon['cost']
            player['weapon'] = chosen_weapon
        else: # Se nada puder ser comprado
            player['weapon'] = find_weapon_by_id('classic')

def calculate_combat_score(player, opponent, is_clutch, alive_teammates):
    """Calcula a pontuação de combate para um duelo, traduzido de a1.ts."""
    attrs = player['attributes']
    
    base_score = attrs['aim']
    
    # Chance de headshot
    is_headshot = random.random() < (attrs['hs'] / 100)
    headshot_multiplier = 1.5 if is_headshot else 1.0
    
    # Fator de evasão baseado na movimentação do oponente
    evasion_factor = 1 - ((opponent['attributes']['movement'] - 70) / 100) * 0.3
    
    # Bônus de Clutch
    clutch_bonus = 1 + ((attrs['cl'] - 80) / 100) * 0.2 if is_clutch else 1
    
    # Bônus de agressividade por iniciar o duelo
    aggression_bonus = 1 + ((attrs['aggression'] - 75) / 100) * 0.1
    
    # Bônus de suporte dos companheiros vivos
    support_sum = sum(p['attributes']['support'] for p in alive_teammates if p['id'] != player['id'])
    support_avg = support_sum / (len(alive_teammates) - 1) if len(alive_teammates) > 1 else 0
    support_bonus = 1 + (support_avg / 100) * 0.15

    # Bônus da arma
    weapon_bonus = player['weapon']['damage']['medium'] / 50

    final_score = base_score * headshot_multiplier * evasion_factor * clutch_bonus * aggression_bonus * support_bonus + weapon_bonus
    
    # Fator de aleatoriedade
    final_score *= (1 + (random.random() - 0.5) * 0.5) # Variação de +/- 25%

    return max(10, final_score)

def apply_round_results(team_a, team_b, winner):
    """Aplica os resultados do round, como score e créditos."""
    if winner == 'teamA':
        team_a['score'] += 1
        for p in team_a['players']: p['credits'] += WIN_REWARD
        for p in team_b['players']: p['credits'] += LOSS_REWARD
    else:
        team_b['score'] += 1
        for p in team_b['players']: p['credits'] += WIN_REWARD
        for p in team_a['players']: p['credits'] += LOSS_REWARD
    
    # Reseta o status para o próximo round
    for team in [team_a, team_b]:
        for p in team['players']:
            p['credits'] = min(MAX_CREDITS, p['credits'])
            if not p['is_alive']:
                p['weapon'] = find_weapon_by_id('classic')

def simulate_full_round(team_a, team_b):
    """Simula um round completo do início ao fim."""
    temp_team_a = copy.deepcopy(team_a)
    temp_team_b = copy.deepcopy(team_b)
    
    # Reseta status e compra armas
    for p in temp_team_a['players'] + temp_team_b['players']:
        p['is_alive'] = True
    
    buy_weapons_for_team(temp_team_a)
    buy_weapons_for_team(temp_team_b)
    
    kill_feed = []
    
    while sum(1 for p in temp_team_a['players'] if p['is_alive']) > 0 and \
          sum(1 for p in temp_team_b['players'] if p['is_alive']) > 0:
        
        alive_a = [p for p in temp_team_a['players'] if p['is_alive']]
        alive_b = [p for p in temp_team_b['players'] if p['is_alive']]

        # Seleciona duelistas com base na agressividade
        player_a = random.choices(alive_a, weights=[p['attributes']['aggression'] for p in alive_a], k=1)[0]
        player_b = random.choices(alive_b, weights=[p['attributes']['aggression'] for p in alive_b], k=1)[0]

        is_clutch_a = len(alive_a) == 1 and len(alive_b) > 1
        is_clutch_b = len(alive_b) == 1 and len(alive_a) > 1

        score_a = calculate_combat_score(player_a, player_b, is_clutch_a, alive_a)
        score_b = calculate_combat_score(player_b, player_a, is_clutch_b, alive_b)

        if score_a > score_b:
            killer, victim = player_a, player_b
            killer_team_id, victim_team_id = temp_team_a['id'], temp_team_b['id']
        else:
            killer, victim = player_b, player_a
            killer_team_id, victim_team_id = temp_team_b['id'], temp_team_a['id']
            
        killer['kills'] += 1
        victim['deaths'] += 1
        victim['is_alive'] = False
        
        kill_feed.append(f"{killer['name']} ({killer['weapon']['name']}) elimiou {victim['name']}")
    
    winner = 'teamA' if sum(1 for p in temp_team_a['players'] if p['is_alive']) > 0 else 'teamB'
    
    # Atualiza o estado original dos times com os resultados
    final_a = copy.deepcopy(team_a)
    final_b = copy.deepcopy(team_b)
    
    # Copia Kills/Deaths para o estado final
    for i in range(len(final_a['players'])):
        final_a['players'][i]['kills'] = temp_team_a['players'][i]['kills']
        final_a['players'][i]['deaths'] = temp_team_a['players'][i]['deaths']
        final_a['players'][i]['is_alive'] = temp_team_a['players'][i]['is_alive']

    for i in range(len(final_b['players'])):
        final_b['players'][i]['kills'] = temp_team_b['players'][i]['kills']
        final_b['players'][i]['deaths'] = temp_team_b['players'][i]['deaths']
        final_b['players'][i]['is_alive'] = temp_team_b['players'][i]['is_alive']

    apply_round_results(final_a, final_b, winner)

    return final_a, final_b, winner, kill_feed