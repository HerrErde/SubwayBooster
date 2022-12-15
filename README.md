<h1 align="center">SubwayBooster</h1>
<p align="center">
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

## Anouncement
Because Kiloo/Sybo now erncrypt all files in the SubwaySurfers app, it's harder to publish the files for the characters and boards-

You can still download all files and put them in the right folder and it will work, SubwaySurfers makes it just easy enough and encrypts those files when they are in the folder, so there changes nothing in this

You can also use an old versions of the app, right now I found [v2.39.0](https://www.apkmirror.com/apk/sybo-games/subwaysurfers/subwaysurfers-2-39-0-release/) best working and the files will not be encrypted, the downside there is that the SeasonHunt will say that you need to udate your app and you dont get new Characters 

Insight how I did it [test](Todo/test)

#### Other

For these Versions I tried to find the right name for the characters and boards and write the json code directly in the old files instead of taking it directly out of the game folder

Found out you can use and edit all files so they have no commas in them (exept the one after "version": 3) and it still works somehow ...
Still gonna use with commas because why not


### App Info

App Version: `v3.5.0`

Season Hunt: `0060`

## TODO
Add every Character and Board that has existed in the game



## Works before v3.0.1

### Score

Android/data/com.kiloo.subwaysurf/files/profile/user_stats.json

Highscore
DefaultValue:100000000


Android/data/com.kiloo.subwaysurf/files/profile/top_run.json

CurrentScore
DefaultValue:100000000

### Currencies / Items

Android/data/com.kiloo.subwaysurf/files/profile/wallet.json

3 Boards
DefaultValue:100000000

2 Keys
DefaultValue:100000000

1 Coins
DefaultValue:100000000

5 Shop:Score Booster
DefaultValue:100000000

6 EventCoins
DefaultValue:100000000

4 Shop:Headstart
DefaultValue:100000000
