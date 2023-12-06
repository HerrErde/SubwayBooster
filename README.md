<h1 align="center">SubwayBooster</h1>
<p align="center">
  <a>
  <img alt="Github All Time Download Count" src="https://img.shields.io/github/downloads/HerrErde/SubwayBooster/total.svg?color=181717&logo=github&style=for-the-badge&cacheSeconds=3600">
  </a>
<a href="https://github.com/HerrErde/SubwayBooster/releases/latest">
  <img alt="Github Release Download Count" src="https://img.shields.io/github/downloads/HerrErde/SubwayBooster/latest/total.svg?color=181717&logo=github&style=for-the-badge&cacheSeconds=3600">
  </a>
  <a href="https://github.com/HerrErde/SubwayBooster/releases/latest">
  <img alt="GitHub Release Tag" src="https://img.shields.io/github/release/HerrErde/SubwayBooster/all.svg?style=for-the-badge&logo=github&logoColor=fafafa&colorA=191b25&colorB=32cb8b&cacheSeconds=3600">
  </a>
  <a href="https://github.com/HerrErde/SubwayBooster/releases/">
    <img alt="GitHub Release Date" src="https://img.shields.io/github/release-date-pre/HerrErde/SubwayBooster.svg?style=for-the-badge&cacheSeconds=3600">
  </a>
</p>

## Please always backup all gameplay data

## Announcement

You can use [subway_gen](https://subway.herrerde.xyz) to customize your own SubwaySurf files, with different Coin/Keys/Boards/.. amount

## Features

- Every [**Character**](https://subwaysurf.fandom.com/wiki/Characters) and their **Outfits**
- Every [**Hoverboard**](https://subwaysurf.fandom.com/wiki/Hoverboard) with every **Special Ability**
- **All Upgrades**
- **Double Coins**
- **Endless Token Boost**
- _basicly_ **Unlimited Coins**
- _basicly_ **Unlimited Keys**
- _basicly_ **Unlimited Boosters**
- _basicly_ **Unlimited Hoverboards**
- Complete **Season**
- Top of **Highscore**
- **30 of 30 Missions/Score Multipliers**
- All **Collections**
- All **Trophies**
- All **Achievements**

### Info

The files of the SubwaySurfers App are now encrypted, not changing the way to add new names for the Characters/Outfits/Boards.
Because it is still possible to modify the SubwaySurfers files by just replacing the original SubwaySurfers files with the modified ones.

If you want to extract your own set of Characters or Boards, you can achieve this by downloading the app, renaming it to `.zip`, \
and then extracting the files `characters.json` and `boards.json` from the folder `assets/tower/gamedata/`. \
This folder contains the necessary data, allowing you to set all characters or boards along with their outfits and Special Abilities.

### How do I use it?

To modify the SubwaySurfers files, you'll need a file explorer and the latest release from [this link](https://github.com/HerrErde/SubwayBooster/releases/latest). Once you've downloaded the release, unpack the Zip file and extract it into the same folder. In the extracted files, you'll find the **Android** folder. Copy this folder to the **Internal Storage** of your Android device.

If you know what you're doing, you can edit the individual files and then copy them into the `com.kiloo.subwaysurf` folder. Just make sure to be careful and understand the changes you're making.

---

Other [docs/info](docs/info.md)

---

| Id            | Name               | Default Value       | File                                                     |
| ----------------- | ------------------ | ------------------- | -------------------------------------------------------- |
| `highscore`                 | Highscore          | 2147483647          | [Android/.../user_stats.json](src/profile/user_stats.json) |
| `currentScore`                 | CurrentScore       | 9223372036854775807 | [Android/.../top_run.json](src/profile/top_run.json)       |
| 1                 | Coins              | 2100000000          | [Android/.../wallet.json](src/profile/wallet.json)         |
| 2                 | Keys               | 2100000000          | [Android/.../wallet.json](src/profile/wallet.json)         |
| 3                 | Shop Boards        | 2100000000          | [Android/.../wallet.json](src/profile/wallet.json)         |
| 4                 | Shop Headstart     | 2100000000          | [Android/.../wallet.json](src/profile/wallet.json)         |
| 5                 | Shop Score Booster | 2100000000          | [Android/.../wallet.json](src/profile/wallet.json)         |
| 6                 | Event Coins        | 2100000000          | [Android/.../wallet.json](src/profile/wallet.json)         |
| `collectedTokens`               | Season Tokens        | 2                   | [Android/.../season_hunt.json](src/profile/season_hunt.json)     |
| `currencyPickupModifiers.doubleCoins`    | Double Coins       | 2                | [Android/.../upgrades.json](src/profile/upgrades.json)     |
| `currencyPickupModifiers.permanent_score_multiplier.expirationValue` | Token Boost Time   | 99999999999999      | [Android/.../upgrades.json](src/profile/upgrades.json)     |
