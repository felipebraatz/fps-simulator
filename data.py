# data.py

def generate_attributes(aim, hs, cl, movement, support, aggression):
    """Gera um dicionário de atributos para um jogador."""
    return {
        "aim": aim,        # Mira geral
        "hs": hs,          # Taxa de headshot
        "cl": cl,          # Habilidade em situações de clutch
        "movement": movement, # Capacidade de evasão/dificultar ser atingido
        "support": support,   # Habilidade de ajudar o time (refrags, info, etc.)
        "aggression": aggression # Tendência a iniciar confrontos
    }

# Atributos perfeitos para jogadores lendários em seu auge.
generate_perfect_attributes = generate_attributes

# Táticas de mapa padrão. No futuro, isso pode influenciar a simulação.
default_tactics = {
    'ascent': 10, 'bind': 10, 'breeze': 10, 'fracture': 10, 'haven': 10,
    'icebox': 10, 'lotus': 10, 'split': 10, 'sunset': 10,
}

# Lista de armas, inspirada em a1.ts e lib/weapons.ts
WEAPONS = [
    {'id': 'classic', 'name': 'Classic', 'type': 'Sidearm', 'cost': 0, 'damage': {'short': 78, 'medium': 66, 'long': 66}},
    {'id': 'shorty', 'name': 'Shorty', 'type': 'Sidearm', 'cost': 150, 'damage': {'short': 150, 'medium': 64, 'long': 24}},
    {'id': 'frenzy', 'name': 'Frenzy', 'type': 'Sidearm', 'cost': 450, 'damage': {'short': 78, 'medium': 63, 'long': 63}},
    {'id': 'ghost', 'name': 'Ghost', 'type': 'Sidearm', 'cost': 500, 'damage': {'short': 105, 'medium': 88, 'long': 85}},
    {'id': 'sheriff', 'name': 'Sheriff', 'type': 'Sidearm', 'cost': 800, 'damage': {'short': 160, 'medium': 155, 'long': 145}},

    {'id': 'stinger', 'name': 'Stinger', 'type': 'SMG', 'cost': 1100, 'damage': {'short': 67, 'medium': 62, 'long': 57}},
    {'id': 'spectre', 'name': 'Spectre', 'type': 'SMG', 'cost': 1600, 'damage': {'short': 78, 'medium': 66, 'long': 60}},

    {'id': 'bucky', 'name': 'Bucky', 'type': 'Shotgun', 'cost': 850, 'damage': {'short': 150, 'medium': 112, 'long': 72}},
    {'id': 'judge', 'name': 'Judge', 'type': 'Shotgun', 'cost': 1850, 'damage': {'short': 136, 'medium': 85, 'long': 51}},

    {'id': 'bulldog', 'name': 'Bulldog', 'type': 'Rifle', 'cost': 2050, 'damage': {'short': 115, 'medium': 115, 'long': 115}},
    {'id': 'guardian', 'name': 'Guardian', 'type': 'Rifle', 'cost': 2250, 'damage': {'short': 195, 'medium': 195, 'long': 195}},
    {'id': 'phantom', 'name': 'Phantom', 'type': 'Rifle', 'cost': 2900, 'damage': {'short': 156, 'medium': 140, 'long': 124}},
    {'id': 'vandal', 'name': 'Vandal', 'type': 'Rifle', 'cost': 2900, 'damage': {'short': 160, 'medium': 160, 'long': 160}},

    {'id': 'marshal', 'name': 'Marshal', 'type': 'Sniper', 'cost': 950, 'damage': {'short': 202, 'medium': 202, 'long': 202}},
    {'id': 'operator', 'name': 'Operator', 'type': 'Sniper', 'cost': 4700, 'damage': {'short': 255, 'medium': 255, 'long': 255}},

    {'id': 'ares', 'name': 'Ares', 'type': 'Heavy', 'cost': 1600, 'damage': {'short': 72, 'medium': 67, 'long': 64}},
    {'id': 'odin', 'name': 'Odin', 'type': 'Heavy', 'cost': 3200, 'damage': {'short': 95, 'medium': 77, 'long': 63}},
]

def find_weapon_by_id(weapon_id):
    """Encontra uma arma pelo seu ID na lista de armas."""
    for weapon in WEAPONS:
        if weapon['id'] == weapon_id:
            return weapon
    return None

# Lista de times com estrutura de dados e atributos detalhados, como em a4.ts e lib/teams.ts
TEAMS = [
    {
        'id': 'loud-2022',
        'name': 'LOUD 2022',
        'shortName': 'LOUD',
        'category': 'Historic Teams',
        'players': [
            {'id': 'loud22-1', 'name': 'aspas', 'role': 'Duelist', 'attributes': generate_perfect_attributes(80, 38, 96, 80, 82, 98)},
            {'id': 'loud22-2', 'name': 'Sacy', 'role': 'Initiator', 'attributes': generate_attributes(78, 37, 90, 79, 92, 85)},
            {'id': 'loud22-3', 'name': 'pANcada', 'role': 'Controller', 'attributes': generate_perfect_attributes(79, 40, 99, 80, 98, 80)},
            {'id': 'loud22-4', 'name': 'Less', 'role': 'Sentinel', 'attributes': generate_attributes(78, 36, 90, 79, 90, 88)},
            {'id': 'loud22-5', 'name': 'saadhak', 'role': 'Flex', 'attributes': generate_attributes(78, 35, 95, 75, 95, 84)},
        ],
        'mapTactics': default_tactics,
    },
    {
        'id': 'acend-2021',
        'name': 'ACEND 2021',
        'shortName': 'ACEND',
        'category': 'Historic Teams',
        'players': [
            {'id': 'acend21-1', 'name': 'BONECOLD', 'role': 'Controller', 'attributes': generate_attributes(78, 35, 90, 78, 88, 78)},
            {'id': 'acend21-2', 'name': 'cNed', 'role': 'Duelist', 'attributes': generate_perfect_attributes(80, 38, 95, 80, 80, 96)},
            {'id': 'acend21-3', 'name': 'Kiles', 'role': 'Sentinel', 'attributes': generate_attributes(77, 35, 86, 79, 85, 80)},
            {'id': 'acend21-4', 'name': 'starxo', 'role': 'Initiator', 'attributes': generate_attributes(78, 34, 88, 78, 87, 85)},
            {'id': 'acend21-5', 'name': 'zeek', 'role': 'Flex', 'attributes': generate_attributes(78, 35, 89, 78, 86, 88)},
        ],
        'mapTactics': default_tactics,
    },
    {
        'id': 'eg-2023',
        'name': 'Evil Geniuses 2023',
        'shortName': 'EG',
        'category': 'Historic Teams',
        'players': [
            {'id': 'eg23-1', 'name': 'Demon1', 'role': 'Duelist', 'attributes': generate_perfect_attributes(80, 39, 94, 77, 80, 95)},
            {'id': 'eg23-2', 'name': 'Ethan', 'role': 'Initiator', 'attributes': generate_attributes(77, 28, 88, 76, 90, 82)},
            {'id': 'eg23-3', 'name': 'Boostio', 'role': 'Controller', 'attributes': generate_attributes(76, 32, 85, 75, 88, 77)},
            {'id': 'eg23-4', 'name': 'jawgemo', 'role': 'Sentinel', 'attributes': generate_attributes(78, 30, 86, 78, 81, 84)},
            {'id': 'eg23-5', 'name': 'C0M', 'role': 'Flex', 'attributes': generate_attributes(75, 29, 87, 75, 89, 79)},
        ],
        'mapTactics': default_tactics,
    },
    {
        'id': 'sen-2024',
        'name': 'Sentinels 2024',
        'shortName': 'SEN',
        'category': 'VCT Americas',
        'players': [
            {'id': 'sen-1', 'name': 'zekken', 'role': 'Duelist', 'attributes': generate_attributes(78, 30, 90, 78, 80, 92)},
            {'id': 'sen-3', 'name': 'Zellsis', 'role': 'Initiator', 'attributes': generate_attributes(76, 28, 88, 75, 89, 85)},
            {'id': 'sen-5', 'name': 'TenZ', 'role': 'Controller', 'attributes': generate_attributes(79, 36, 92, 79, 85, 88)},
            {'id': 'sen-4', 'name': 'johnqt', 'role': 'Sentinel', 'attributes': generate_attributes(77, 31, 91, 76, 88, 80)},
            {'id': 'sen-2', 'name': 'Sacy', 'role': 'Flex', 'attributes': generate_attributes(78, 32, 90, 78, 92, 83)},
        ],
        'mapTactics': default_tactics,
    },
]