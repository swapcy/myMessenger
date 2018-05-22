
import oauth2 as oauth
import json
import hidden


secret = hidden.oauth()

CONSUMER_KEY = secret['consumer_key']
CONSUMER_SECRET = secret['consumer_secret']
ACCESS_KEY = secret['token_key']
ACCESS_SECRET = secret['token_secret']
GIPHY_TOKEN = secret['giphy_token']


consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

search_tweets_url = 'https://api.twitter.com/1.1/search/tweets.json'
giphy_url = 'https://api.giphy.com/v1/gifs/search?api_key='+GIPHY_TOKEN
giphy_random = 'https://api.giphy.com/v1/gifs/random?api_key='+GIPHY_TOKEN
count='5'
def extractTweets(param='IPL'):
    tdetails = dict()
    elements = []
    template = dict()
    print("Grabbing tweets for "+param)
    parameter = param
    search_tweets = search_tweets_url+'?q='+parameter+'&result_type=top&count='+count
    giphy_search_url = giphy_url+'&q='+param+'&limit='+count+'+&offset='+count+'&rating=R&lang=en'
    giphy_random_url = giphy_random+'&tag=&rating=R'
    try:
        output = []
        response, data = client.request(search_tweets)
        giphy = client.request(giphy_search_url)
        jgiphy = json.loads(giphy[1])
        jgif = jgiphy['data']
        #gif = jgif['images']['original_still']['url']
        gif =[]
        for jg in jgif:
            gif.append(jg['images']['original_still']['url'])


        print('Here are the top '+count+' tweets on :{0} \n '.format(' '+param))
        output.append('Here are the top '+count+' tweets on :{0} \n '.format(' '+param))
        tweets = json.loads(data)
        for index,tweet in enumerate(tweets['statuses']):                    
            if(tweet['entities']['urls']!=[]):
                url = tweet['entities']['urls'][0]['expanded_url']
            else:
                url = 'https://media.giphy.com/media/xT0BKFyZt9MMx9xkpW/giphy.gif'
            
            tdetails['subtitle'] = tweet['user']['screen_name']
            tdetails['title'] = tweet['text']
            tdetails['image_url'] = gif[index]#tweet['user']['profile_image_url']
            tdetails['default_action'] = {"type": "web_url","url": url, "messenger_extensions": False,"webview_height_ratio": "Full"}
            tdetails['buttons']= [{"type":"web_url","url":gif[index],'title':"Random GIF"}]
            elements.append(tdetails)        
            print("index: ",index)                
            print("gif: ",gif[index])                
            print('text: ',tdetails['title'])
            tdetails=dict()
            #print('\n'+tweet['user']['screen_name']+' : '+tweet['text']+'\n')
            #output.append(tweet['user']['screen_name']+' : '+tweet['text'])            
            #for count in range(20):
            #print('-',end='')
            #print('\n\n')
        
        template['message']={'attachment':{'type': 'template','payload':{'template_type':'generic','elements':elements}}}
        output.append(template['message'])
        #print(output)
        return output
    except Exception as e:
        print('Something went wrong :( '+str(e))
        return ['Something went wrong! :(']
    else:
        print(':D')
        return ['Else :D']
    finally:
        pass


#extractTweets(param='ipl')

'''with open('data.txt', 'w') as outfile:
     json.dump(tweets, outfile, sort_keys = True, indent = 4)'''




