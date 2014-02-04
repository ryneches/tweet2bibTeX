#!/usr/bin/env python
import twitter
from datetime import datetime
from secret_stuff import *
api = twitter.Api()

api = twitter.Api(  consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token_key,
                    access_token_secret=access_token_secret)

bibtemplate = """
@ONLINE{_KEY_,
    author = {_LASTNAME_, _FIRSTNAME_},
    title = {_TITLE_},
    month = {_MONTH_},
    year = {_YEAR_},
    url = {_URL_}
}
"""

def tweet2bibTeX( tweetlink, key=False ) :
    id = tweetlink.split('/')[-1]
    tweet = api.GetStatus(id).AsDict()
    author = tweet['user']['name']
    user   = tweet['user']['screen_name']
    date   = tweet['created_at']
    text   = tweet['text']
    date   = datetime.strptime( date, '%a %b %d %H:%M:%S +0000 %Y' )
    month  = date.strftime("%B")
    year   = date.strftime("%Y")
    lname  = author.split()[-1]
    fname  = author.split()[:-1][0]
   
    if not key : key = user + year
    return bibtemplate.replace('_KEY_', key ) \
        .replace('_FIRSTNAME_', fname )       \
        .replace('_LASTNAME_', lname )        \
        .replace('_TITLE_', text)             \
        .replace('_YEAR_', year )             \
        .replace('_MONTH_', month )           \
        .replace('_URL_', tweetlink ) 
