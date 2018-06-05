import datetime

class utils():
    """description of class"""
    tzOffset = (datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds()/3600

    teamAbbrs = [
        'ATL', 'CHA', 'MIA', 'ORL', 'WAS',
        'BOS', 'BKN', 'NYK', 'PHI', 'TOR',
        'CHI', 'CLE', 'DET', 'IND', 'MIL',
        'GSW', 'LAC', 'LAL', 'PHX', 'SAC',
        'DAL', 'HOU', 'MEM', 'NOP', 'SAS',
        'DEN', 'MIN', 'OKC', 'POR', 'UTA'
        ]
    teamSubs = [
        'atlantahawks', 'charlottehornets', 'heat', 'orlandomagic', 'washingtonwizards', 
        'bostonceltics', 'gonets', 'nyknicks', 'sixers', 'torontoraptors', 
        'chicagobulls', 'clevelandcavs', 'detroitpistons', 'pacers', 'mkebucks', 
        'warriors', 'laclippers', 'lakers', 'suns', 'kings', 
        'mavericks', 'rockets', 'memphisgrizzlies', 'nolapelicans', 'nbaspurs', 
        'denvernuggets', 'timberwolves', 'thunder', 'ripcity', 'utahjazz'
        ]
    teamArenas = [
        'Philips Arena', 'Time Warner Cable Arena', 'American Airlines Arena', 'Amway Center', 'Verizon Center',
        'TD Garden', 'Barclays Center', 'Madison Square Garden', 'Wells Fargo Center', 'Air Canada Centre',
        'United Center', 'Quicken Loans Arena', 'Little Caesars Arena', 'Bankers Life Fieldhouse', 'BMO Harris Bradley Center', 'Oracle Arena', 'Staples Center', 'Staples Center', 'Talking Stick Resort Arena', 'Golden 1 Center',
        'American Airlines Arena', 'Toyota Center', 'FedExForum', 'Smoothie King Center', 'AT&T Center',
        'Pepsi Center', 'Target Center', 'Chesapeake Energy Arena', 'Moda Center', 'Vivint Smart Home Arena'
        ]

    def today():
        return datetime.datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    

    ### EXTRA GAME INFO HELPERS
    def getGameStartTimeLocal(gameStartTimeUTC):
        startTimeUTC = datetime.datetime.strptime(gameStartTimeUTC, '%Y-%m-%dT%H:%M:%S.%fZ')
        return startTimeUTC + datetime.timedelta(hours=utils.tzOffset)

    def getGameOpponentSub(oppTricode):
        for i in range(0,30):
            if utils.teamAbbrs[i] == oppTricode:
                return '/r/' +utils.teamSubs[i]
        return '/r/NBA'

    def getGameArena(tricode):
        for i in range(0,30):
            if utils.teamAbbrs[i] == tricode:
                return utils.teamArenas[i]
        return 'Outer Space Arena'