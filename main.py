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



