BASE_VALUE = 100

LEVEL_SHARDS = dict([
    (35, 150),
    (40, 275),
    (45, 500),
    (50, 750),
    (55, 1000),
    (60, 1500),
    (65, 2000),
    (70, 3250),
    (75, 4500),
    (80, 5750),
    (85, 7500),
    (90, 10000),
    (95, 12500),
    (100, 15000)
])

FEAT_SHARDS_MULTIPLIER = 10

LEGENDARY_SHARDS = {
    "Lich": {"value": 10, "extra": 5, "limit": -1},
    "Gorgon": {"value": 10, "extra": 5, "limit": -1},
    "Harpy": {"value": 10, "extra": 5, "limit": -1},
    "Reaper": {"value": 20, "extra": 10, "limit": -1},
    "Cyclops": {"value": 20, "extra": 10, "limit": -1},
    "Archdemon": {"value": 20, "extra": 10, "limit": 3},
    "Cursed": {"value": 30, "extra": 0, "limit": 1},
    "Colossus": {"value": 30, "extra": 0, "limit": 1},
    "Infernal": {"value": 30, "extra": 0, "limit": 1},
    "Robochicken": {"value": 20, "extra": 10, "limit": 3},
    "Shieldbot": {"value": 30, "extra": 15, "limit": 3},
    "Soul Stalker": {"value": 40, "extra": 20, "limit": -1}
}

LEGENDARY_SET_SHARDS = {
    ("Lich", "Gorgon", "Harpy"): 20,
    ("Reaper", "Cyclops", "Archdemon"): 40,
    ("Cursed", "Colossus", "Infernal"): 60,
    ("Robochicken", "Shieldbot", "Soul Stalker"): 80,
    ("Lich", "Gorgon", "Harpy",
     "Reaper", "Cyclops", "Archdemon",
     "Cursed", "Colossus", "Infernal",
     "Robochicken", "Shieldbot", "Soul Stalker"): 100
}
