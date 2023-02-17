# Lyrics Bot for Telegram

<b>Main idea</b>

This bot was made especially in training<br>
purpose, just for fun and do not have<br>
any commercial interest.<br> 
Main idea is that sometimes you can<br>
answer to messages in telegram using<br>
your favourite artist or music band<br>
lyrics. You can't remember the whole<br>
text, this bot reminds you.<br>

<b>How to deploy this bot</b>

First of all you need a database of<br>
lyrics, which consists of lines of text.<br>
Don't worry about punctuation marks -<br> 
function does not count it in process<br>
of search. Database can be presented<br>
as simple .txt file. It is enough for<br>
good perfomance if it contains dozen<br>
of albums (remember about copyright).<br>


<b>How to use this bot</b>

This telegram bot works in inline mode<br>
in any (or almost any) chat, and allows<br>
to send lines from song lyrics.<br> 
You need just type the word or a phrase<br>
after the bot call:<br>

<b>@"botname" "your word or phrase"</b><br>

Bot will search and offer you some<br> 
random options of lyrics containing<br> 
your word or phrase looks like<br> 
popup buttons above the input line.<br>
There are will be no results if word<br> 
or a phrase not in database of lyrics.<br>
Function search only full match, for example:<br>

request: <b>@"botname" "fun"</b> will find only<br>
lines from lyrics including "<b>fun</b>", not "<b>fun</b>ction".<br>

request: <b>@"botname" "how are you"</b> will find only<br>
lines from lytics including "<b>how are you</b>",<br>
not "<b>how</b> far from home <b>are you</b>?"<br>

It was made for better match.

 
