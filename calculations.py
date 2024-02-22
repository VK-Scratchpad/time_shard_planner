from data.shards import LEGENDARY_SHARDS, LEVEL_SHARDS, FEAT_SHARDS_MULTIPLIER, BASE_VALUE, LEGENDARY_SET_SHARDS

legendary_table = {x: 0 for x in LEGENDARY_SHARDS.keys()}


def get_level_shards(level):
    return LEVEL_SHARDS[level]


def get_feat_shards(feats):
    return (feats * FEAT_SHARDS_MULTIPLIER) + BASE_VALUE


def list_legendaries():
    return [x for x in LEGENDARY_SHARDS.keys()]


def list_legendary_limits():
    return [x['limit'] for x in LEGENDARY_SHARDS.values()]


def init_legendary_table():
    legendary_table = {x: 0 for x in LEGENDARY_SHARDS.keys()}


def update_legendary_count(update_val, legend):
    legendary_table[legend] = update_val


def get_legendary_table():
    return legendary_table


def get_legendary_shards():
    val = 0

    for legend, count in legendary_table.items():
        if count == 0:
            continue
        else:
            extra = count - 1
            val += LEGENDARY_SHARDS[legend]['value'] + (extra * LEGENDARY_SHARDS[legend]['extra'])

    for tier, value in LEGENDARY_SET_SHARDS.items():
        set_bonus = True
        for t in tier:
            if legendary_table[t] == 0:
                set_bonus = False

        if set_bonus:
            val += value

    return val
