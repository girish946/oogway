#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os
import feedparser
import json
import urllib2


class FeedParser(object):

    def __init__(self, listFile = '.oogway/sitelist'):

        if(os.path.isfile(listFile)):
             self.siteListJson = open(listFile).read()
             self.sites = json.loads(self.siteListJson)
             
             
    def getRssFeedOf(self, site= None ):

        if site and site in self.sites:

            rssXMLData = urllib2.urlopen(self.sites[site]).read()
            rssData = feedparser.parse(rssXMLData)
            return rssData
        else:

            return ''

    def getCompleteFeed(self):

        self.feed = {}
        for i in self.sites:

            self.feed[i] = []
            entries = self.getRssFeedOf(i).entries
            for j in entries:
                self.feed[i].append((j.title, j.link,))

        return self.feed


