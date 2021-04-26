import json
from pprint import pprint

# Generates the offsets for `generate_cheat_list.py` based on a address list made with Game Conqueror.
# Its assumed the cheats are all just for one and the same hero.
# You can copy the output to `generate_cheat_list.py` which will generate the address list for all other heroes.

# Orrin
base_address = 27278243

with open('hero_base_cheats.json') as json_file:
    data = json.load(json_file)
    # My original cheat Table used the Name of the Hero and was not clean
    # so this the Name has to be filtered for and removed otherwise it will be included in the generation
    # for other heroes.
    cheats = [[a[2], a[3], a[4]] for a in data['cheat_list'] if 'Orrin' in a[2]]
    offsets = []
    for c in cheats:
        offsets.append([c[0][6:], int(c[1])-base_address, c[2]])

    pprint(offsets)
