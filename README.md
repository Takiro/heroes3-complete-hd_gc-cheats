# Heroes 3 Complete - GC Cheats

This repo contains address lists for the use with *Game Conqueror* to cheat in *Heroes and Might and Magic 3 Complete HD+* and some generator scripts to generate cheats for every hero.

This is for people like me who play on Linux and recently got in the mood of playing Heroes of Might and Magic 3 Complete again. Although I just wanted to edit a skill I didn't like I ended up mapping most of the memory for a character and then created scripts for to generate the cheat addresses for all heroes.

You can find the Cheats in the Cheat directory. Since they are so many I put every list into a single file for each Character. Just load the `json` file with GameConquerer. 

The lists will probably only work with the Complete Edition (or when you have the base game + Armageddons Blade and Shadow of Death installed) since there are heroes only available in the expansions.

I also used the unofficial HD+ patch (not the broken thing from Steam)


# Players

In `all player's resources.json` you find the addresses for editing Wood, Ore, Gold etc for every Player. The game is pretty simple and always loads all players even if they are not part of the current game. Just edit the values for your color (or the one for your enemies if you want to be mean and take stuff away from them)

## Heroes

For each Hero you can edit:

- Movement Points (Lock this to run forever, yay)
- Experience Points (I didn't include editing Level directly because this seems to do nothing expept changing the Number)
- Unit Types [1]
- Unit Count
- Experience
- Base Stats (Athough you can set values greater than 99, Heroes moving to the next mission will get reset to 99)
- Backpack (add whatever artefact you want, 64 Holy Grails? No problem.) [1]
- Skill levels [2]
- Skill Slots [2]
- Spells in Spellbook [3]
- Special Items like First Aid Tent or Ballista

[1] Unlike Cheat-Engine Game-Conqueror doesn't allow choices or scripts so here are only raw numbers instead of the actual names. You can find useful numbers on the internet like [here](http://heroescommunity.com/viewthread.php3?TID=18817)

[2] To learn a new skill it needs a level greater 0 (smaller than 4 or it crashes the game) and it must be assigned a slot (where it appears in the games Interface) there is also a value `Skill Count` you have to increase when you are not just simply switching skills.

[3] Remember some heroes and classes just can't learn certain spells, this doesn't seem to be changeable even by changing it in memory, the game will change the spell to unknown (0) the instant you change it to known (1).

## Be Cautious

As always when using a memory editor, be careful what you type in as values because to big or small ones can make your game crash or behave abnormally.

## The Python Scripts

The python scripts can be used to regenerate the Hero Cheats. This could be needed when you have additional Mods that change the Memory layout. This way you just have to change the offsets and find them for one hero and can generate all adresses for all 157 other heroes in an instant. 
