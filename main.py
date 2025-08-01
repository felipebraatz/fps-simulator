import random

score_team_1 = 0
score_team_2 = 0
team_1 = {}
team_2 = {}

# --- Definição dos Times e Jogadores (mantida a mesma) ---
team_acend_2021 = {
    'name': 'Acend 2021',
    'players': [
        {'name': 'cNed', 'role': 'Duelist', 'nationality': 'Turkey', 'aim': 100, 'game_sense': 60, 'clutch': 70},
        {'name': 'Starxo', 'role': 'Initiator', 'nationality': 'Poland', 'aim': 80, 'game_sense': 80, 'clutch': 60},
        {'name': 'zeek', 'role': 'Flex', 'nationality': 'Poland', 'aim': 70, 'game_sense': 60, 'clutch': 60},
        {'name': 'Kiles', 'role': 'Sentinel', 'nationality': 'Spain', 'aim': 60, 'game_sense': 70, 'clutch': 60},
        {'name': 'BONECOLD', 'role': 'Controller', 'nationality': 'Finland', 'aim': 70, 'game_sense': 80, 'clutch': 60}
    ]
}

team_loud_2022 = {
    'name': 'LOUD 2022',
    'players': [
        {'name': 'Less', 'role': 'Sentinel', 'nationality': 'Brazil', 'aim': 80, 'game_sense': 70, 'clutch': 70},
        {'name': 'Aspas', 'role': 'Duelist', 'nationality': 'Brazil', 'aim': 100, 'game_sense': 60, 'clutch': 60},
        {'name': 'Sadhak', 'role': 'Flex', 'nationality': 'Argentina', 'aim': 70, 'game_sense': 100, 'clutch': 70},
        {'name': 'Sacy', 'role': 'Initiator', 'nationality': 'Brazil', 'aim': 80, 'game_sense': 90, 'clutch': 80},
        {'name': 'Pancada', 'role': 'Controller', 'nationality': 'Brazil', 'aim': 90, 'game_sense': 70, 'clutch': 100}
    ]
}

team_eg_2023 = {
    'name': 'Evil Geniuses 2023',
    'players': [
        {'name': 'Demon1', 'role': 'Duelist', 'nationality': 'USA', 'aim': 100, 'game_sense': 60, 'clutch': 70},
        {'name': 'Ethan', 'role': 'Initiator', 'nationality': 'USA', 'aim': 70, 'game_sense': 80, 'clutch': 60},
        {'name': 'jawgemo', 'role': 'Flex', 'nationality': 'USA', 'aim': 80, 'game_sense': 70, 'clutch': 70},
        {'name': 'Boostio', 'role': 'Sentinel', 'nationality': 'USA', 'aim': 70, 'game_sense': 90, 'clutch': 60},
        {'name': 'C0M', 'role': 'Controller', 'nationality': 'USA', 'aim': 60, 'game_sense': 70, 'clutch': 60}
    ]
}

team_edg_2024 = {
    'name': 'EDward Gaming 2024',
    'players': [
        {'name': 'ZmjjKK', 'role': 'Duelist', 'nationality': 'China', 'aim': 100, 'game_sense': 60, 'clutch': 70},
        {'name': 'nobody', 'role': 'Initiator', 'nationality': 'China', 'aim': 80, 'game_sense': 70, 'clutch': 60},
        {'name': 'CHICHOO', 'role': 'Flex', 'nationality': 'China', 'aim': 90, 'game_sense': 70, 'clutch': 70},
        {'name': 'S1Mon', 'role': 'Controller', 'nationality': 'China', 'aim': 80, 'game_sense': 70, 'clutch': 60},
        {'name': 'Smoggy', 'role': 'Sentinel', 'nationality': 'China', 'aim': 80, 'game_sense': 70, 'clutch': 60}
    ]
}

# --- Dicionário para Mapear Opções para Times (com poderes pré-calculados) ---
# Adicionaremos uma nova chave 'total_power' a cada dicionário de time
# após a seleção, ou podemos fazer isso na definição.
# Para manter a clareza, vamos pré-calcular aqui.

def calculate_team_overall_power(team_data):
    """Calcula o poder total de um time com base na média dos atributos dos jogadores."""
    total_player_power = sum((p['aim'] + p['game_sense'] + p['clutch']) / 3 for p in team_data['players'])
    return total_player_power

# Adiciona o 'total_power' aos dicionários de times existentes
team_acend_2021['total_power'] = calculate_team_overall_power(team_acend_2021)
team_loud_2022['total_power'] = calculate_team_overall_power(team_loud_2022)
team_eg_2023['total_power'] = calculate_team_overall_power(team_eg_2023)
team_edg_2024['total_power'] = calculate_team_overall_power(team_edg_2024)

available_teams_options = {
    '1': team_acend_2021,
    '2': team_loud_2022,
    '3': team_eg_2023,
    '4': team_edg_2024
}

# --- Round Calculation Function (mais eficiente agora) ---
def calculate_round_winner(current_team_1_power, current_team_2_power):
    global score_team_1
    global score_team_2

    # team_1_power e team_2_power já são os valores pré-calculados!
    # Não precisamos mais iterar pelos jogadores aqui.

    luck_factor_1 = random.randint(50, 200)
    luck_factor_2 = random.randint(50, 200)

    round_score_1 = current_team_1_power + luck_factor_1
    round_score_2 = current_team_2_power + luck_factor_2

    if round_score_1 > round_score_2:
        score_team_1 += 1
    else:
        score_team_2 += 1

# --- Team Selection ---
print('Bem-vindo ao Simulador de Valorant!\n')

print('Escolha o primeiro time:')
for key, team_dict in available_teams_options.items():
    print(f"{key}. {team_dict['name']}")

while True:
    choice_team_1_str = input('\nEscolha uma das opcoes: ')
    if choice_team_1_str in available_teams_options:
        team_1 = available_teams_options[choice_team_1_str]
        break
    else:
        print('Opcao invalida, tente novamente...')

print('\nAgora escolha o segundo time:')
for key, team_dict in available_teams_options.items():
    print(f"{key}. {team_dict['name']}")

while True:
    choice_team_2_str = input('\nEscolha uma das opcoes: ')
    if choice_team_2_str in available_teams_options:
        if available_teams_options[choice_team_2_str]['name'] == team_1['name']:
            print('Opcao ja escolhida, tente novamente...')
        else:
            team_2 = available_teams_options[choice_team_2_str]
            break
    else:
        print('Opcao invalida, tente novamente...')

# --- Main Game Loop ---
while True:
    print(f'\n{team_1["name"]} {score_team_1}x{score_team_2} {team_2["name"]}')

    if score_team_1 >= 12 and score_team_2 >= 12 and abs(score_team_1 - score_team_2) < 2:
        print("\n--- PRORROGAÇÃO ---")
        while not ((score_team_1 >= 13 and score_team_1 - score_team_2 >= 2) or \
                   (score_team_2 >= 13 and score_team_2 - score_team_1 >= 2)):
            
            print(f'{team_1["name"]} {score_team_1}x{score_team_2} {team_2["name"]}')
            
            # Passa o 'total_power' pré-calculado
            calculate_round_winner(team_1['total_power'], team_2['total_power'])
            
            input('Aperte qualquer tecla para o próximo round de prorrogação:')
        
    if (score_team_1 >= 13 and score_team_1 - score_team_2 >= 2) or \
       (score_team_1 == 13 and score_team_2 < 12):
        print(f'\nFim de jogo! {team_1["name"]} venceu!')
        break
    elif (score_team_2 >= 13 and score_team_2 - score_team_1 >= 2) or \
         (score_team_2 == 13 and score_team_1 < 12):
        print(f'\nFim de jogo! {team_2["name"]} venceu!')
        break
    
    # Passa o 'total_power' pré-calculado
    calculate_round_winner(team_1['total_power'], team_2['total_power'])
    input('Aperte qualquer tecla para o próximo round:')