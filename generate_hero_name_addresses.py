import json
# This small program creates a cheat List only containing the character names
# You can load the generated `hero_adresses.json` file into Game Conqueror
# And it should show all the Names of the Heroes as values
# The Address list can then be used again to generate the base addresses
# for `generate_cheat_list.py`.
#
# If everything looks fine in Game Conqueror save the cheat list as `hero_names.json`
# and use it with `generate_hero_base_addresses.py`.

# Address of the first hero in memory (Orrin)
address = 27278243
# Offset to the next Hero in Memory
offset = 0x492
number_of_heroes = 156

with open("hero_addresses.json", mode='w') as f:
    characters = []
    for i in range(0, number_of_heroes):
        # `" "*13` ist to work around a limitation of Game Conqueror that string types have no length
        # but use whatever length the value has
        characters.append(["=", False, "Name", address, 'string', " "*13, True])
        address += offset

    f.write(json.dumps({'cheat_list': characters}))
