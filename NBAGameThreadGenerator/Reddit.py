import praw
import prawcore
import datetime
import urllib

from utils import utils

class Reddit(object):
    """Perform various operations on Reddit"""
    reddit = None
    subreddit = ''
    subredditThreads = None

    def updateWiki(self, wikiPage, wikiContents):
        currentWiki = self.reddit.subreddit(self.subreddit).wiki[wikiPage].content_md

        if currentWiki != wikiContents:
            self.reddit.subreddit(self.subreddit).wiki[wikiPage].edit(wikiContents)

    def refreshThreads(self):
        self.subredditThreads.refresh(self.reddit.subreddit(self.subreddit).new(limit=200))

    def __init__(self, subreddit):
        self.reddit = praw.Reddit(user_agent='NBA Game Thread Generator')
        self.subreddit = subreddit
        self.subredditThreads = SubredditThreads()

class Thread(object):
    threadType = ''
    threadDate = None
    threadTitle = ''
    threadID = ''

    def __init__(self, thread):
        self.threadType = str(thread.link_flair_css_class)
        self.threadDate = (datetime.datetime.fromtimestamp(thread.created) + datetime.timedelta(hours=utils.tzOffset)).replace(hour = 0, minute = 0, second = 0, microsecond = 0)
        self.threadTitle = thread.title
        self.threadID = thread.id

class SubredditThreads(object):

    def refresh(self, threads):
        self.subThreads.clear()
        for thread in threads:
            self.subThreads.append(Thread(thread))

    def __init__(self):
        self.subThreads = []

    def findThread(self, threadDate, threadType, vTeamName, hTeamName):
        for thread in self.subThreads:
            if thread.threadType == threadType and thread.threadDate == threadDate and all(x in thread.threadTitle for x in [hTeamName, vTeamName]):
                return thread.threadID