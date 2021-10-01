import tweepy
import time
import re

# Your own bot account's keys got from twitter developer page
consumer_key= 'XXXXXXXXXXXXXXXX'
consumer_secret= 'XXXXXXXXXXXXXXXXXXX'
key= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
secret= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#   Formalities 😏
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)


word='valorant giveaway' # This is the word which will be searched in twitter(change it according to your needs)

def scan(number):
    tweet_count=0
    tweets=tweepy.Cursor(api.search,word).items(number) # the function which will search the word,
                                                    # item=no of tweets to take at first iteration
    for tweet in tweets:
                l=[]    # Empty list if we get any error from  def like()
                r=[]    # Empty list if we get any error from  def retweet()
                text=[]
                finaltext=[]
                id=tweet.id
                text = re.split('\n| |-|✅|✔|,', tweet.text) # Splits the tweet text by these characters
                for i in text:
                    if i!='':
                        finaltext.append(i) # A finallist(without null values), in which all operations will be done
             
                
                if 'follow' in finaltext or 'Follow' in finaltext or 'FOLLOW' in finaltext:
                    follow(finaltext) # If follow word(in any form) found in tweet text then execute
                if 'like' in finaltext or 'Like' in finaltext or 'LIKE' in finaltext:
                    l=like(id)        # If Like word(in any form) found in tweet text then execute
                if 'retweet' in finaltext or 'Retweet' in finaltext or 'RT' in finaltext or 'RETWEET' in finaltext:
                    r=retweet(id)     # # If retweet word(in any form) found in tweet text then execute
                if 'Tag' in finaltext or 'tag' in finaltext or 'TAG' in finaltext:
                    if l==[] or r==[]: # If empty list that means the post has not been visited earlier so then tag
                        tag(id)
                    else:       # If not empty then it has error from retweet or like.
                                # That means it is visited once and tagged 2 friends once. So no tag 
                        continue
                tweet_count=tweet_count+1 # How many tweets have been visited
                print(tweet_count)
                


def follow(text):       # To Follow the usernames which are mentioned in the post (needs improvement)
        username=[]
        i=0
        for j in range(len(text)):
            if text[j][i]=='@':
                username.append(text[j])

        if username[0][-1]==':': # If retweeted by someone then his/her username will also be added with 'RT @abc:'
                                 # So if retweeted post then dont follow the retweeter
            username.pop(0)
        for k in username:
            print(k)       # usernames to follow,(some user names is not coming out as full usernames)(need to fix)
            try:
                 user=api.get_user(k).id
                 api.create_friendship(user)    
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
          
               
def like(id):       # To Like the post if only it is mentioned in the giveaway rules
    try:
        api.create_favorite(id)
    except tweepy.TweepError as e:
        return e.reason



def retweet(id):     # To Retweet the post if only it is mentioned in the giveaway rules
    try:
        api.retweet(id)
    except tweepy.TweepError as e:
        return e.reason

    
    

def tag(id):        # Tag Two friends if it is mentioned in the post
    try:
        api.update_status(status = '@rono_jana @SounakJana', in_reply_to_status_id = id , auto_populate_reply_metadata=True)
    except tweepy.TweepError as e:
        print(e.reason)

                
                
                             
while True: 
    scan(10) # change the item as per your need in my case it is kept 10,
           # That means it will take first 10 tweets according to the search word
    
    time.sleep(15) # Then take 15 second break then again iterate. To minimize account blocking possibility