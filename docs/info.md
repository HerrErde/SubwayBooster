# Some Infos found out

## Input limits

<p>
There are Limits to how much value you can add.<br>
The limit for the <code style="background-color: lightblue;">wallet.json</code> is the 32-bit integer wich is <code style="color: red;">2,147,483,647</code>.
That's why everything is only <code style="color: red;">2100000000</code>, the reason is if the number is where too high and the value would go over the limit, the value goes into minus. That way there are about a hundred million coins/keys/.. buffer that you can collect before this happens.
</p>

<p>
To set the Highscore you actually have to edit two files with the same number (but they can also be different).<br>
<code style="background-color: lightblue;">user_stats.json</code> is the local highscore which you can see next to the crown over the "What's News?" button.<br>
<code style="background-color: lightblue;">top_run.json</code> is the score viewable in the "Top Run" list (on opening the leaderboard).<br>
The <code style="background-color: lightblue;">user_stats.json</code> file has the 32-bit integer limit which is <code style="color: red;">2,147,483,647</code> (don't know why they changed it) and the <code style="background-color: lightblue;">top_run.json</code> has the 64-bit integer limit which is <code style="color: red;">9,223,372,036,854,775,807</code>, but it is hard to even reach this number, so it is set.
</p>

## Play old SubwaySurfers app versions

<p>
You can still play the old versions of the SubwaySurfers app, by downloading them from <a href="https://www.apkmirror.com/apk/sybo-games/subwaysurfers/">apkmirror.com</a>.<br>
On the bottom left of the <code>Download APK</code> page, you can see the apk upload date, which you need to set your phone's date to, to avoid the annoying <code>Download Update</code> popup.
</p>

## Creating weird stuff

<p>
When finding out what the best number for the <code>expirationValue</code> in <code style="background-color: lightblue;">upgrades.json</code> is,<br>
I found out that when the set number is too high (the first try was 64-bit) and the same Token Boost widget duplicates itself multiple times under each other (which got really laggy).
</p>

<p>
When editing <code>shortcut</code> or <code>icon</code> values in any file, they will stay and the values dont reset.
Which means you can Link any button to any (avalialbil) page or you can set all icons to specific icons.
You can get a list of the available icon and shortcuts list <a href="stuff.json">here</a>.
</p>
