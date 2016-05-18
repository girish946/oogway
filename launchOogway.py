#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys
import os
from rssFeedParser import FeedParser



if __name__ == '__main__':

    allFeeds = FeedParser()
    count = 0
    feed = {}
    for i in allFeeds.sites:
        feed[i] = []
        entries = allFeeds.getRssFeedOf(i).entries
        for j in entries:

            #print j.title
            #print j.link
            count+=1
            feed[i].append((j.title, j.link,))

    

    #print feed
    #print count

