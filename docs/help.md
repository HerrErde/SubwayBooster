# How it works

## Character

RULES

1. any name with a space is "firstSecond" which means, for example "Miss Maia"\
   is without space and with the first letter of the second word big\
   example `missMaia`.

2. additional outfits are named like this `{outfitname}Outfit`.\
   example `goldOutfit`. in code is it `\"value\":\"goldOutfit\"}`\
   when the outfit name has a space, rule 1.

3. Characters without outfits just have the `\"lastOutfit\":\"default\"`

### Example

#### Miss Maia - One Outfit

```
\"missMaia\":{\"value\":{\"id\":\"missMaia\",\"ownedOutfits\":[{\"value\":\"default\"}],\"lastOutfit\":\"default\"}}
```

#### Jake - Two additional outfits

```
\"jake\":{\"value\":{\"id\":\"jake\",\"ownedOutfits\":[{\"value\":\"default\"},{\"value\":\"darkOutfit\"},{\"value\":\"starOutfit\"}],\"lastOutfit\":\"default\"}}
```

#### example code

```
\"firstSecond\":{\"value\":{\"id\":\"firstSecond\",\"ownedOutfits\":[{\"value\":\"default\"}],\"lastOutfit\":\"default\"}}
```

---

## Boards

RULES

1. any name with a space is "firstSecond" which means, for example "Skull Fire"\
   is without space and with the first letter of the second word big\
    example `skullFire`.

2. special abilitys are named just after the ability name \
    example "Trail" is `trail` in code is it `\"trail\":{\"value\":true`\
   when the special ability has a space, rule 1.\
   below is a list of all special abilitys

3. Boards without a visible ability which you can enable and disable\
   just have the `\"default\":{\"value\":true}`

### Example

#### Default Board

```
\"default\":{\"value\":{\"id\":\"default\",\"ownedUpgrades\":{}}}
```

#### Skull Fire - Two special abilitys

```
\"skullFire\":{\"value\":{\"id\":\"skullFire\",\"ownedUpgrades\":{\"default\":{\"value\":true},\"doubleJump\":{\"value\":true},\"highSpeed\":{\"value\":true}}}}
```

#### example code

```
\"firstSecond\":{\"value\":{\"id\":\"firstSecond\",\"ownedUpgrades\":{\"default\":{\"value\":true}}}}
```

#### special abilitys

`\"firstSecond\":{\"value\":true}`

---

| Name                  | other name                              | code         |
| --------------------- | --------------------------------------- | ------------ |
| Double Jump           | -                                       | `doubleJump` |
| Trails                | `bubble`, `heart`, `music`, `pink`, ... | `trail`      |
| Speed Up, Super Speed | `speed`                                 | `highSpeed`  |
| Super Jump            | `jumper`                                | `superJump`  |
| Smooth Drift          | -                                       | `glider`     |
| Stay Low              | -                                       | `lowrider`   |
| Zap Sideways          | -                                       | `teleport`   |
