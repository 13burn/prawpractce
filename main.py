#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:21:28 2020

@author: Bardo
"""

import praw
import info

reddit = praw.Reddit(client_id =info.client_id,
                     client_secret = info.client_secret,
                     username = info.username,
                     password = info.password,
                     user_agent = "me")

print(reddit.random_subreddit())

sub = reddit.subreddit("mexico")

htmx = sub.hot(limit =30)

for submi in htmx:
    print(submi.author)
    try:
        coms = submi.comments
        for aus in coms:
            print(aus.author)
    except:
        print("no comments")
    
    

