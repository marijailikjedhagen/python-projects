# RPG Character

A function that builds a character sheet for an RPG adventure.

`create_character(name, strength, intelligence, charisma)` checks that:
- the name is a non-empty string, at most 10 characters, with no spaces
- every stat is an integer from 1 to 4, and the stats add up to 7

If everything is valid, it returns the character sheet:

```
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

Otherwise it returns a message explaining what's wrong.

Run it: `python rpg_character.py`
