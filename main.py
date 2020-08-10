#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:21:28 2020

@author: Bardo
"""

import praw
import info
import json
from time import sleep

running = True
counter = 0

#try except to read and wirite the file
def main():
    try:
        with open('data/data.json', 'r') as myfile:
            obj = myfile.read()
            data=json.loads(obj.encoding("utf-8"))
            print("+++++++++++++++++++ file open +++++++++++++++++++++++")
    except:
        data={}
        data["subs"]=info.targets
        for target in info.targets:
            data[target] = []
        print("----------------- open failed ----------------------")
        
    
    reddit = praw.Reddit(client_id =info.client_id,
                         client_secret = info.client_secret,
                         username = info.username,
                         password = info.password,
                         user_agent = "me")
    
    print(reddit.random_subreddit())
    
    for subreddit in data["subs"]:
    
        sub = reddit.subreddit(subreddit)
        
        ht = sub.new(limit =30)
        print("-------- scanning r/{} -------".format(subreddit))
        for submi in ht:
            try:
                data[subreddit].append(str(submi.author))
                
                try:
                    coms = submi.comments
                    for aus in coms:
                        data[subreddit].append(str(aus.author))
                        #print(aus.author)
                except:
                    print("no comments")
            except:
                print("unable to perform action")
        data[subreddit] = list(set(data[subreddit]))
        print("------- {} users saved(total) -------".format(len(data[subreddit] )))
        
        
    try:
        with open('data/data.json', 'w') as outfile:
            json.dump(data, outfile)
    except:
        print("Cannot save info")
        
while (running):
    sleep(30)
    main()
    print("----- round {} -----".format(counter))
    counter += 1
    if counter == 10:
        running=False