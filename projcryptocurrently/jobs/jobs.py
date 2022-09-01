from distutils.sysconfig import customize_compiler
from django.conf import settings
import tweepy
import pandas as pd
from sentiment_analyzer import extraction, cleaner, manipulation, analysis
from sentiment_analyzer.extraction import create_api, search_tweets, search_to_df
from jobs.save import return_save
import json
from datetime import datetime
from sentiment_analyzer.analyzer import analyzerOutput


def schedule_extract():
    t=datetime.now()
    # print(t)
    if t.minute==30 and t.second==00:
        print("Getting sentiments...")
        consumer_key, consumer_key_secret, access_token, access_token_secret = extraction.create_var()
        save_destination = return_save()
        coin = ["Bitcoin","BNB","Ethereum","Tether","USD Coin","XRP"]
        for x in range(0,len(coin)):
            print("Extracting " + coin[x] + " tweets")
            api = create_api(consumer_key, consumer_key_secret, access_token, access_token_secret)
            search_results = search_tweets(api,coin[x], ignore_rt=True, max_tweets=400)
            tweets = search_to_df(search_results)
            tweets.to_csv(save_destination + coin[x] + ".csv", index=False)

        cleaner.clean()
        manipulation.run()
        analysis.run_analysis()

def analyzerValues():
    # get current and previous values
    outList = []
    tim = datetime.now()
    if tim.hour%2 == 0:
        current_address = "out2/"
        previous_address = "out/"
    else:
        current_address = "out/"
        previous_address = "out2/"

    outList.append([analyzerOutput("bitcoin", current_address), analyzerOutput("ethereum", current_address), analyzerOutput("xrp", current_address), analyzerOutput("usdcoin", current_address), analyzerOutput("binance", current_address), analyzerOutput("tether", current_address)])
    
    outList.append([analyzerOutput("bitcoin", previous_address), analyzerOutput("ethereum", previous_address), analyzerOutput("xrp", previous_address), analyzerOutput("usdcoin", previous_address), analyzerOutput("binance", previous_address), analyzerOutput("tether", previous_address)])

    return outList