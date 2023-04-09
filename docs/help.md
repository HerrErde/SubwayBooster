# How it works

## Character

RULES

1. any name with a space is "firstSecond" which means, for example "Miss Maia"\
   is without space and with the first letter of the second word big\
   example `missMaia`.

2. additional outfits are named like this `{outfitname}Outfit`.\
   example `goldOutfit`. in code is it `\"value\":\"goldOutfit\",\"expirationType\":0}`\
   when the outfit name has a space, rule 1.

3. Characters without outfits just have the `\"lastOutfit\":\"default\"`

### Example

#### Miss Maia - One Outfit

```
\"missMaia\":{\"value\":{\"id\":\"missMaia\",\"ownedOutfits\":[{\"value\":\"default\",\"expirationType\":0}],\"lastOutfit\":\"default\"},\"expirationType\":0}
```

#### Jake - Two additional outfits

```
\"jake\":{\"value\":{\"id\":\"jake\",\"ownedOutfits\":[{\"value\":\"default\",\"expirationType\":0},{\"value\":\"darkOutfit\",\"expirationType\":0},{\"value\":\"starOutfit\",\"expirationType\":0}],\"lastOutfit\":\"default\"},\"expirationType\":0}
```

#### example code

```
\"firstSecond\":{\"value\":{\"id\":\"firstSecond\",\"ownedOutfits\":[{\"value\":\"default\",\"expirationType\":0}],\"lastOutfit\":\"default\"},\"expirationType\":0}
```

---

## Boards

RULES

1. any name with a space is "firstSecond" which means, for example "Skull Fire"\
   is without space and with the first letter of the second word big\
    example `skullFire`.

2. special abilitys are named just after the ability name \
    example "Trail" is `trail` in code is it `\"trail\":{\"value\":true,\"expirationType\":0`\
   when the special ability has a space, rule 1.\
   below is a list of all special abilitys

3. Boards without a visible ability which you can enable and disable\
   just have the `\"default\":{\"value\":true,\"expirationType\":0}`

### Example

#### Default Board

```
\"default\":{\"value\":{\"id\":\"default\",\"ownedUpgrades\":{}},\"expirationType\":0}
```

#### Skull Fire - Two special abilitys

```
\"skullFire\":{\"value\":{\"id\":\"skullFire\",\"ownedUpgrades\":{\"default\":{\"value\":true,\"expirationType\":0},\"doubleJump\":{\"value\":true,\"expirationType\":0},\"highSpeed\":{\"value\":true,\"expirationType\":0}}},\"expirationType\":0}
```

#### example code

```
\"firstSecond\":{\"value\":{\"id\":\"firstSecond\",\"ownedUpgrades\":{\"default\":{\"value\":true,\"expirationType\":0}}},\"expirationType\":0}
```

#### special abilitys

`\"firstSecond\":{\"value\":true,\"expirationType\":0}`

---

| Name         | other name                      | code         |
| ------------ | ------------------------------- | ------------ |
| Double Jump  | -                               | `doubleJump` |
| Trils        | Bubble, heart, music, pink, ... | `trail`      |
| Color Splash | -                               | -            |
| Speed Up     | -                               | `highSpeed`  |
| Super Jump   | -                               | `superJump`  |
| Smooth Drift | -                               | `glider`     |
| Super Jump   | -                               | `jumper`     |
| Stay Low     | -                               | `lowrider`   |
| Zap Sideways | -                               | `teleport`   |
