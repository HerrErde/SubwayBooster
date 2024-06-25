# Some Infos found out

## Input limits

<p>
There are Limits to how much value you can add.<br>
The limit for the <code style="background-color: lightblue;">wallet.json</code> is the 32-bit integer wich is <code style="color: red;">2,147,483,647</code>.
That's why everything is only <code style="color: red;">2100000000</code>, the reason is, if the number is at the limit and only + 1 would happen the whole number would turn over and the value goes into minus (With which you cant do anything). That way there are about a hundred million coins/keys/.. buffer that you can collect before this happens.
</p>

<p>
To set the Highscore you actually have to edit two files with the same number (but they also can be different).<br>
<code style="background-color: lightblue;">user_stats.json</code> is the local highscore which you can see next to the crown over the "What's New?" button.<br>
<code style="background-color: lightblue;">top_run.json</code> is the score viewable in the "Top Run" list (on opening the leaderboard).<br>
Both files <code style="background-color: lightblue;">user_stats.json</code> have the 32-bit integer limit which is <code style="color: red;">2,147,483,647</code>.
The <code style="background-color: lightblue;">top_run.json</code> had until 3.29.0 has had the 64-bit integer limit which is <code style="color: red;">9,223,372,036,854,775,807</code>, was changed to the 32-bit limit.
</p>

## Play old SubwaySurfers app versions

<p>
You can still play the old versions of the SubwaySurfers app, by downloading them from <a href="https://www.apkmirror.com/apk/sybo-games/subwaysurfers/">apkmirror.com</a>.<br>
On the bottom left of the <code>Download APK</code> page, you can see the apk upload date, which you need to set your phone's date to, to avoid the annoying <code>Download Update</code> popup.
</p>

## Creating weird stuff

<p>
When finding out what the best highest number for the <code>expirationValue</code> in <code style="background-color: lightblue;">upgrades.json</code> is,<br>
I found out that when the number is set too high (the first try was 64-bit) and the Token Boost widget duplicates itself multiple times under each other (which got really laggy).
So the highest number is <code>99999999999999</code>.
</p>

<p>
When editing <code>shortcut</code> or <code>icon</code> values in any file, they will stay and the values dont reset.
This means you can Link any button to any (available) page or you can set all icons to specific icons.
You can get a list of the available icons and shortcuts list <a href="stuff.json">here</a>.
</p>

## Value Ids

| Id                                           | Name               | Default Value   | File                                                            |
| -------------------------------------------- | ------------------ | --------------- | --------------------------------------------------------------- |
| `highscore`                                  | Highscore          | 2147483647      | [Android/.../user_stats.json](../src/profile/user_stats.json)   |
| `currentScore`                               | CurrentScore       | 2147483647      | [Android/.../top_run.json](../src/profile/top_run.json)         |
| 1                                            | Coins              | 2100000000      | [Android/.../wallet.json](../src/profile/wallet.json)           |
| 2                                            | Keys               | 2100000000      | [Android/.../wallet.json](../src/profile/wallet.json)           |
| 3                                            | Shop Boards        | 2100000000      | [Android/.../wallet.json](../src/profile/wallet.json)           |
| 4                                            | Shop Headstart     | 2100000000      | [Android/.../wallet.json](../src/profile/wallet.json)           |
| 5                                            | Shop Score Booster | 2100000000      | [Android/.../wallet.json](../src/profile/wallet.json)           |
| 6                                            | Event Coins        | 2100000000      | [Android/.../wallet.json](../src/profile/wallet.json)           |
| `collectedTokens`                            | Season Tokens      | 2               | [Android/.../season_hunt.json](../src/profile/season_hunt.json) |
| `doubleCoins`                                | Double Coins       | 2               | [Android/.../upgrades.json](../src/profile/upgrades.json)       |
| `permanent_score_multiplier.expirationValue` | Token Boost Time   | 999999999999999 | [Android/.../upgrades.json](../src/profile/upgrades.json)       |
| `token_multiplier_low.expirationValue`       | Token Boost Time   | 99999999999999  | [Android/.../upgrades.json](.src/profile/upgrades.json)         |

## Forced encryption

<p>
In the newest update 3.29.0 comes the Player Profile with the Portrait, Frame and Background.
They also added some stats of Characters Hoverboards, Achievements, Destinations and Top Run Badges.<br>
Because they dont want anyone to edit the save files, now the file requires a forced pre encrypton, to be even loaded, so no normal unencrypted json and from the game again being reincrypted. But Right now it only affects the file <code style="background-color: red;">user_stats.json</code>.
But wich weirdly dosnt affect the new  <code style="background-color: lightgray;">profile_portrait.json</code> <code style="background-color: lightgray;">profile_frame.json</code>  or <code style="background-color: lightgray;">profile_background.json</code> files
</p>

(Inside the Player Profile from right to left)

| Nmae    | Place | Default Value | File                                                          |
| ------- | ----- | ------------- | ------------------------------------------------------------- |
| Champ   | 102   | 2147483647    | [Android/.../user_stats.json](../src/profile/user_stats.json) |
| Diamond | 103   | 2147483647    | [Android/.../user_stats.json](../src/profile/user_stats.json) |
| Gold    | 104   | 2147483647    | [Android/.../user_stats.json](../src/profile/user_stats.json) |
| Silver  | 105   | 2147483647    | [Android/.../user_stats.json](../src/profile/user_stats.json) |
| Bronze  | 106   | 2147483647    | [Android/.../user_stats.json](./.src/profile/user_stats.json) |

## Assets encrypted/compiled

<p>
Since the 3.29.1 update, the json files in the <code>assets/tower/gamedata</code> directory of the APK are now encrypted. <br>
It seems like they are in some form compiled. This change prevents me from updating SubwayBooster, as it is no longer possible to read the necessary files.<br>
Therefore, SubwayBooster will remain at version 1.4.0 until it is possible to decrypt or decompile the files and access the data again.
</p>

## IOS Game Version

<p>
Apparently Sybo still dosnt encrypt the save files of the IOS version, nor the assets files.
If that changes in the future, we will have to see.
Until then SubwayBooster will use the IOS version of the game and extract the assets files, which have the same format.
</p>


## File Version

<p>
All files have a <code>version</code> key.
Some save files might not work and get corrupted if their version doesn't match what's needed by the app.
The weird thing is that not all files are like this and will still work.
But it is still something to check for.
</p>