<h1 align="center">SubwayBooster</h1>
<p align="center">
  <a>
  <img alt="Github All Time Download Count" src="https://img.shields.io/github/downloads/HerrErde/SubwayBooster/total.svg?color=181717&logo=github&style=for-the-badge">
  </a>
<a href="https://github.com/HerrErde/SubwayBooster/releases/latest">
  <img alt="Github Release Download Count" src="https://img.shields.io/github/downloads/HerrErde/SubwayBooster/latest/total.svg?color=181717&logo=github&style=for-the-badge">
  </a>
  <a href="https://github.com/HerrErde/SubwayBooster/releases/latest">
  <img alt="GitHub Release Tag" src="https://img.shields.io/github/release/HerrErde/SubwayBooster/all.svg?style=for-the-badge&logo=github&logoColor=fafafa&colorA=191b25&colorB=32cb8b">
  </a>
  <a href="https://github.com/HerrErde/SubwayBooster/releases/">
    <img alt="GitHub Release Date" src="https://img.shields.io/github/release-date-pre/HerrErde/SubwayBooster.svg?style=for-the-badge">
  </a>
</p>

## Please always backup all gameplay data

## Announcement

You can use [subway_gen](https://subway.herrerde.xyz) to customize your own SubwaySurf files, with different Coin/Keys/Boards/.. amount

## Features

- All*most all* [**Characters**](todo/Characters.md) and their **Outfits**
- All*most all* [**Boards**](todo/Boards.md) with every **Special Ability**
- **Double Coins**
- **All Upgrades**
- _basicly_ **Unlimited Coins**
- _basicly_ **Unlimited Keys**
- _basicly_ **Unlimited Boosters**
- Complete **Season**
- Top of **Highscore**
- **30 of 30 Missions/Multiplier**
- All **Trophies**
- All **Achievements**

### Info

The files of the SubwaySurfers App are now encrypted, making it more difficult to add new names for the Characters/Outfits/Boards.
However, it is still possible to modify the SubwaySurfers files by replacing the original SubwaySurfers files with the modified ones.

But it's not too difficult. You can achieve this by downloading the app, renaming it to `.zip`, and then extracting the files `characters.json` and `boards.json` from the folder `assets/tower/game data/`. This folder contains all the necessary information, allowing you to view all characters or boards along with their outfits and Special Abilities.

You can play the old SubwaySurfers app versions. When you set the date of your Phone to the same date (or before) the release of the app on [apkmirror.com](https://apkmirror.com). \
For example, when the app was released on 29.08.2022 set your phone to the same date.

---

### How do I use it?

To modify the SubwaySurfers files, you'll need a file explorer and the latest release from [this link](https://github.com/HerrErde/SubwayBooster/releases/latest). Once you've downloaded the release, unpack the Zip file and extract it into the same folder. In the extracted files, you'll find the **Android** folder. Copy this folder to the **Internal Storage** of your Android device.

If you know what you're doing, you can edit the individual files and then copy them into the `com.kiloo.subwaysurf` folder. Just make sure to be careful and understand the changes you're making.

---

Insight how I did it [docs/help](docs/help.md) <br>
Some Infos [docs/info](docs/info.md) <br>
Character [todo/Character.md](todo/Character.md) <br>
Boards [todo/Boards.md](todo/Boards.md)

### App Info

App Version: `3.12.0`

Season Hunt: `0067`

## TODO

/

---

| Number | Name               | Default Value       | File                                                                                           |
| ------ | ------------------ | ------------------- | ---------------------------------------------------------------------------------------------- |
| -      | Highscore          | 9223372036854775807 | [Android/.../user_stats.json](Android/data/com.kiloo.subwaysurf/files/profile/user_stats.json) |
| -      | CurrentScore       | 9223372036854775807 | [Android/.../top_run.json](Android/data/com.kiloo.subwaysurf/files/profile/top_run.json)       |
| 1      | Coins              | 2100000000          | [Android/.../wallet.json](Android/data/com.kiloo.subwaysurf/files/profile/wallet.json)         |
| 2      | Keys               | 2100000000          | [Android/.../wallet.json](Android/data/com.kiloo.subwaysurf/files/profile/wallet.json)         |
| 3      | Shop Boards        | 2100000000          | [Android/.../wallet.json](Android/data/com.kiloo.subwaysurf/files/profile/wallet.json)         |
| 4      | Shop Headstart     | 2100000000          | [Android/.../wallet.json](Android/data/com.kiloo.subwaysurf/files/profile/wallet.json)         |
| 5      | Shop Score Booster | 2100000000          | [Android/.../wallet.json](Android/data/com.kiloo.subwaysurf/files/profile/wallet.json)         |
| 6      | EventCoins         | 2100000000          | [Android/.../wallet.json](Android/data/com.kiloo.subwaysurf/files/profile/wallet.json)         |
| -      | Token Boost        | 2                   | [Android/.../upgrades.json](Android/data/com.kiloo.subwaysurf/files/profile/upgrades.json)     |
