# Twitter-Giveaway-Bot
Please read the Read ME before executing
This is a Bot which will participate in Twitter Giveaways and will Like Retweet Follow and Comment if mention in the Giveaway Rule.

# Disclaimer
I hold no responsibility for account blocking.  This is only for educational purpose. Use the script at your own risk and responsibility. Dont use it on your main account, make a secondary account for only this purpose (Highly Recommended).

# Language and Lib
python 3.9.5
Tweepy

# Steps
1. Make a twttier account.
2. Apply for twitter developer account with the username and password.
3. Enter to Twitter Apps and click the Create New App button
4. Fill out all details and create the app
5. Generate the keys
6. Now copy Consumer Key, Consumer Secret, Access Token, Access Token Secret and paste them into their right place.
7. open terminal and put this command pip install tweepy. 

# Description
 After entering all the keys generated from the twitter developer page, there is a variable called `WORD`. Change it as per your needs. For Example: I want to participate in   valorant giveaways, thats why `word='valorant giveaway'`.
 If you want to participate in crypto giveaway, then `word='crypto giveaway'`.
 So, the script will starting with word you entered in twitter.
 After that there is function called `SCAN`. It takes an argument as a integer. The number of tweets you need  in every iteration. In my case it is set as 10.
 Then the `SCAN` function searches the twitter with the word you have given and takes first 10(numbers) of tweets as input.
 Then a loop will be executed which will scan every tweet from those 10 tweets.
 Now from each tweet the text will be separated by the punctuation marks given.(you can change those according to your use) And will be stored in a list called finaltext.

 1. `FOLLOW`: If the list finaltext contains word FOLLOW(in any form) then the follow function will be executed. Which taked one argument as list. which is final text.
    Then it search the list, whether it contains any username(starts with @) or not. If yes the searches the username, gets the user_id as return and follows by the user_id.
    Sometimes a tweet is not the main post(it is retweeted by someone else), if thats the case then another username gets added in the username list as `[RT @abc:]`. So if first       the username contains : in `username[0][-1]` then it gets popped out.
 2. `LIKE`: If the list finaltext contains word LIKE(in any form) then the like function will be executed. Which taked one argument id. which is tweet id stored at first. Then         likes the post. If liked previously then it doesnot dilike the post.
 3. `RETWEET`: If the list finaltext contains word RETWEET(in any form) then the retweet function will be executed. Which taked one argument id. which is tweet id stored at          first.Then retweets the post. If retweeted previously then it doesnot dilike the post.
 4. `TAG`: If the finaltext list contains a word like TAG(in any form), then it tags two of your friends. you can change the username entered in the tag function with your own         friend's usernames. 
 
 Sometime it happens that a previsited tweet appears and it tags again in the same tweet. To avoid that created two empty list in scan function. 
 If only both of the lists are empty then it tags two people your mention. If any one the list is not empty it means the script has visited the tweet before thats why either liked it or retweeted it. thats why any one of the like() or retweet() funtion is throwing an error which is being stored in any of those empty list. Then only tag() function will not be executed.
 
 
 

`Still in V.1. No doubt needs a lot of improvements. If anyone wants to collaborate to improve the script,Do fork the repo and add your ideas. I will be more than happy to implement those in the original repo.`
 

