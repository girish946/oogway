import json

class SiteListManager(object):

    def __init__(self, siteListFile = '.oogway/sitelist'):

        self.siteListFile = siteListFile
        self.sites = json.loads(open(self.siteListFile).read())

    def addSite(self, domain = None, rssLink = None):

        if domain and rssLink:
            self.sites[domain] = rssLink
            with open(self.siteListFile, 'w') as writeSL:
                writeSL.write(json.dumps(self.sites))


    def removeSite(self, domain = None):

        if domain:
            self.sites.pop(domain)
            with open(self.siteListFile, 'w') as writeSL:
                writeSL.write(json.dumps(self.sites))




