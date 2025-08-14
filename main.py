# main.py

import copy
import os
from data import TEAMS, find_weapon_by_id
from simulation import simulate_full_round

WIN_SCORE = 13
HALF_TIME_ROUND = 12

def clear_screen():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_team_for_match(team_data):
    """Prepara a estrutura de um time para a partida, como em a2.ts e a3.ts."""
    team = copy.deepcopy(team_data)
    team['score'] = 0
    for player in team['players']:
        player['kills'] = 0
        player['deaths'] = 0
        player['credits'] = 800
        player['is_alive'] = True
        player['weapon'] = find_weapon_by_id('classic')
    return team

def print_scoreboard(team_a, team_b):
    """Exibe o placar detalhado com estatísticas dos jogadores."""
    print("-" * 60)
    print(f"{'JOGADOR':<20} {'K':<3} {'D':<3} | {'JOGADOR':<20} {'K':<3} {'D':<3}")
    print(f"{team_a['name']:<27} | {team_b['name']:<27}")
    print("-" * 60)
    
    for p_a, p_b in zip(team_a['players'], team_b['players']):
        line_a = f"{p_a['name']:<20} {p_a['kills']:<3} {p_a['deaths']:<3}"
        line_b = f"{p_b['name']:<20} {p_b['kills']:<3} {p_b['deaths']:<3}"
        print(f"{line_a} | {line_b}")
    print("-" * 60)

def check_win_condition(team_a, team_b, is_overtime):
    """Verifica a condição de vitória, incluindo prorrogação, como em a2.ts."""
    score_a, score_b = team_a['score'], team_b['score']
    
    if is_overtime:
        if score_a >= score_b + 2:
            return team_a
        if score_b >= score_a + 2:
            return team_b
    else:
        if score_a == WIN_SCORE:
            return team_a
        if score_b == WIN_SCORE:
            return team_b
    return None

def main():
    """Função principal que executa o simulador de partida."""
    clear_screen()
    print('Bem-vindo ao Simulador Avançado de Valorant!\n')

    # --- Seleção de Times ---
    print('Escolha o primeiro time:')
    for i, team in enumerate(TEAMS):
        print(f"{i + 1}. {team['name']}")
    
    choice1 = int(input('\nEscolha uma opção: ')) - 1
    team_a_data = TEAMS[choice1]

    print('\nAgora escolha o segundo time:')
    available_teams = [t for t in TEAMS if t['id'] != team_a_data['id']]
    for i, team in enumerate(available_teams):
        print(f"{i + 1}. {team['name']}")
        
    choice2 = int(input('\nEscolha uma opção: ')) - 1
    team_b_data = available_teams[choice2]

    # --- Inicialização da Partida ---
    team_a = initialize_team_for_match(team_a_data)
    team_b = initialize_team_for_match(team_b_data)
    round_number = 1
    is_overtime = False
    match_winner = None
    
    # --- Loop da Partida ---
    while not match_winner:
        clear_screen()
        
        # Checa se entrou em prorrogação
        if not is_overtime and team_a['score'] == WIN_SCORE - 1 and team_b['score'] == WIN_SCORE - 1:
            is_overtime = True

        ot_status = "| PRORROGAÇÃO" if is_overtime else ""
        print(f"--- Round {round_number} {ot_status} ---")
        print(f"{team_a['name']} {team_a['score']} x {team_b['score']} {team_b['name']}\n")
        
        print_scoreboard(team_a, team_b)

        # --- Controles da Simulação ---
        print("\nOpções:")
        print("[1] Simular Próximo Round")
        print("[2] Simular Partida até o Fim (Fast Simulate)")
        action = input("Escolha uma ação: ")

        if action == '1': # Simular um round
            team_a, team_b, winner, kill_feed = simulate_full_round(team_a, team_b)
            print("\nKill Feed do Round:")
            for kill in kill_feed:
                print(f" > {kill}")
            
            winner_name = team_a['name'] if winner == 'teamA' else team_b['name']
            print(f"\n>> {winner_name} venceu o round! <<")
            input("\nPressione Enter para continuar...")

        elif action == '2': # Simular tudo
            while not match_winner:
                team_a, team_b, _, _ = simulate_full_round(team_a, team_b)
                if not is_overtime and team_a['score'] == WIN_SCORE - 1 and team_b['score'] == WIN_SCORE - 1:
                    is_overtime = True
                match_winner = check_win_condition(team_a, team_b, is_overtime)
            continue # Pula para o fim do loop para exibir o resultado final
        
        else:
            print("Ação inválida.")
            input("\nPressione Enter para tentar novamente...")
            continue

        round_number += 1
        match_winner = check_win_condition(team_a, team_b, is_overtime)
        
    # --- Fim de Jogo ---
    clear_screen()
    print("=" * 25)
    print("    FIM DE JOGO!")
    print("=" * 25)
    print(f"\n{match_winner['name']} venceu a partida!\n")
    print(f"Placar Final: {team_a['name']} {team_a['score']} x {team_b['score']} {team_b['name']}\n")
    print_scoreboard(team_a, team_b)


if __name__ == '__main__':
    main()