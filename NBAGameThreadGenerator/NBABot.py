from Data import Data
from Teams import Teams
from Scoreboard import Scoreboard
from MarkDownGenerator import MarkDownGenerator
from Reddit import Reddit

from utils import utils

import datetime
import time
import sys
import urllib

class NBABot(object):

    def sleep(self, numSeconds):
        curTime = datetime.datetime.now()

        print('Waking at ' + str(curTime + datetime.timedelta(seconds=numSeconds)))
        time.sleep(numSeconds)

    def update_gamethreads(self):
        self.data.refreshAll()
        self.teams.refresh(self.data.jsonTeams, self.data.jsonStandings)
        self.scoreboard.refresh(self.data.jsonScoreboard, self.teams)
        self.reddit.refreshThreads()
    
        todaysGames = '#NBA Games for ' + datetime.datetime.strftime(datetime.datetime.today(), '%m/%d/%Y') + '\r\n\r\n'

        todaysGames += '##Game Threads may only be posted 1 hour prior to tip off at the earliest.\r\n\r\n'

        todaysGames += '###Please limit yourself to one game thread or post game thread per day.\r\n\r\n'

        for game in self.scoreboard.games:
            vTeam = self.teams.getTeamById(game.vTeamId)
            hTeam = self.teams.getTeamById(game.hTeamId)
            threadTitle = MarkDownGenerator.getGameThreadTitle(game, vTeam, hTeam)
            threadBody = MarkDownGenerator.getGameThreadBody(game, vTeam, hTeam)

            game = vTeam.city + ' ' + vTeam.nickname + ' @ ' + hTeam.city + ' ' + hTeam.nickname + ' - '

            gameThreadID = self.reddit.subredditThreads.findThread(utils.today(), 'gamethread', vTeam.nickname, hTeam.nickname)
            if gameThreadID == None:
                gameThread = '[Create Game Thread](https://www.reddit.com/r/NBA/submit?selftext=true&' + urllib.parse.urlencode({'title': threadTitle, 'text': threadBody}) + ')'
            else:
                gameThread = '[Game Thread](/r/nba/comments/' + gameThreadID + ')'

            postGameThreadID = self.reddit.subredditThreads.findThread(utils.today(), 'postgamethread', vTeam.nickname, hTeam.nickname)
            if postGameThreadID == None:
                postGameThread = ''
            else:
                postGameThread = ' - [Post Game Thread](/r/nba/comments/' + postGameThreadID + ')'


            todaysGames += game + gameThread + postGameThread + '\r\n\r\n'

        self.reddit.updateWiki('game_thread_generator', todaysGames)

    def __init__(self):
        self.data = Data()
        self.teams = Teams()
        self.scoreboard = Scoreboard()
        self.reddit = Reddit('nba')
