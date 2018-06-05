from utils import utils

class Game(object):

    def __init__(self, jsonGame, teams):
        self.seasonStageId = jsonGame['seasonStageId']
        self.gameId = jsonGame['gameId']
        self.statusNum = jsonGame['statusNum']
        self.startTimeUTC = jsonGame['startTimeUTC']
        self.startDateEastern = jsonGame['startDateEastern']
        self.vTeamId = jsonGame['vTeam']['teamId']
        self.vTeamScore = jsonGame['vTeam']['score']
        self.vTeamRecord = jsonGame['vTeam']['seriesWin'] + '-' + jsonGame['vTeam']['seriesLoss']
        self.hTeamId = jsonGame['hTeam']['teamId']
        self.hTeamScore = jsonGame['hTeam']['score']
        self.hTeamRecord = jsonGame['hTeam']['seriesWin'] + '-' + jsonGame['hTeam']['seriesLoss']

class Scoreboard(object):
    """Todays Games"""

    def refresh(self, jsonScoreboard, teams):
        self.games.clear()

        for jsonGame in jsonScoreboard['games']:
            self.games.append(Game(jsonGame, teams))

    def __init__(self):
        self.games = []

        