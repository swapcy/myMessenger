
import oauth2 as oauth
import json
import hidden


secret = hidden.oauth()

CONSUMER_KEY = secret['consumer_key']
CONSUMER_SECRET = secret['consumer_secret']
ACCESS_KEY = secret['token_key']
ACCESS_SECRET = secret['token_secret']

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

search_tweets_url = 'https://api.twitter.com/1.1/search/tweets.json'

#print(response)

#print(data)


def extractTweets(param='IPL'):
    parameter = param
    search_tweets = search_tweets_url+'?q='+parameter+'&result_type=recent&count=5'
    try:
        output = []
        response, data = client.request(search_tweets)
        print('Here are the recent 5 tweets on :{0} \n '.format(' '+param))
        output.append('Here are the recent 5 tweets on :{0} \n '.format(' '+param))
        tweets = json.loads(data)
        for tweet in tweets['statuses']:
            #print('\n'+tweet['user']['screen_name']+' : '+tweet['text']+'\n')
            output.append(tweet['user']['screen_name']+' : '+tweet['text'])
            
            output.append('-------')
            #for count in range(20):
             #   print('-',end='')
        print(output)
        return output
    except Exception as e:
        print('Something went wrong :(')
        return ['Something went wrong! :(']
    else:
        print(':D')
        return ['Else :D']
    finally:
        pass


#extractTweets(param='ipl')
    





'''with open('data.txt', 'w') as outfile:
     json.dump(tweets, outfile, sort_keys = True, indent = 4)'''




