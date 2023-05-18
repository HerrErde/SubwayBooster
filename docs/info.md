# Some Infos found out

## Input limits

<p>
There are Limits to how much stuff you can add.
The limit for the <code style="background-color: purple;">wallet.json</code> is the 32-bit integer wich is <code style="color: lightgreen;">2147483647</code>. That's why everything is only <code style="color: lightgreen;">2.100.000.000</code>, the reason is if the number is too high and goes over the limit, the value goes into minus. That way there is about a hundred million coins/keys/.. buffer that you can use before this happens.
</p>

<p>
To set the Highscore you actually have to edit two files with the same number (but they can also be different).
<code style="background-color: purple;">user_stats.json</code> is the local highscore wich you can see next to the crown over the "What's News?" button.
<code style="background-color: purple;">top_run.json</code> is the score viewable in the "Top Run" list (when you open the leaderboard).
The <code style="background-color: purple;">user_stats.json</code> and <code style="background-color: purple;">top_run.json</code> have the limit of the 64-bit integer which is <code style="color: lightgreen;">9,223,372,036,854,775,807</code>,
but it is hard to even reach this number, so it is set.
</p>

## Play old SubwaySurfers app versions

<p>
You can still play the old versions of the SubwaySurfers app, by downloading them from <a href="https://www.apkmirror.com/apk/sybo-games/subwaysurfers/">apkmirror.com</a>. On the bottom left of the <code>Download APK</code> page, you can see the apk upload date, which you need to set your phone's date to, to avoid the annoying <code>Download Update</code> popup.
</p>

## Creating weird stuff

<p>
When finding out what the best number for the <code>expirationValue</code> in <code style="background-color: purple;">upgrades.json</code> is, I found out that when the set number is too high(my first try was the 64bit), the number is too much and the same Token Boost widget duplicates itself multiple times under each other.
</p>
