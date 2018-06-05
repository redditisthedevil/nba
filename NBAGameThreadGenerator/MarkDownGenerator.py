from utils import utils
import datetime

class MarkDownGenerator():
    """Generate Markdown for Schedule, Standings and GameThreads"""

    def getGameThreadTitle(game, vTeam, hTeam):
        gameStartTimeLocal = utils.getGameStartTimeLocal(game.startTimeUTC)
        gameDate = gameStartTimeLocal.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
        gameDateMD = datetime.datetime.strftime(gameDate, '%B %d, %Y')

        title = 'GAME THREAD: {0} {1} ({2}) @ {3} {4} ({5}) - ({6})'.format(
            vTeam.city,
            vTeam.nickname,
            vTeam.record,
            #PLAYOFFS game.vTeamRecord,
            hTeam.city,
            hTeam.nickname,
            #PLAYOFFS game.hTeamRecord,
            hTeam.record,
            gameDateMD
        )

        return title


    def getGameThreadBody(game, vTeam, hTeam):


        body = '''
##General Information

**TIME**     |**MEDIA**                            |**LOCATION**        |**MISC**
:------------|:------------------------------------|:-------------------|:-------------------------
{0} Eastern |**Game Preview**: [NBA.com]({4}) | {8}               | 
{1} Central |**Game Matchup**: [NBA.com]({5}) | {9}**Team Subreddits**|
{2} Mountain|**Play By Play**: [NBA.com]({6})| {10}          |
{3} Pacific |**Box Score**: [NBA.com]({7}) | {11}          |

-----

[Reddit Stream](https://reddit-stream.com/comments/auto) (You must click this link from the comment page.)
        '''.format(
            ###REPLACE FOR LOCAL TIME
            datetime.datetime.strftime(utils.getGameStartTimeLocal(game.startTimeUTC) + datetime.timedelta(hours=3), '%I:%M %p'),
            datetime.datetime.strftime(utils.getGameStartTimeLocal(game.startTimeUTC) + datetime.timedelta(hours=2), '%I:%M %p'),
            datetime.datetime.strftime(utils.getGameStartTimeLocal(game.startTimeUTC) + datetime.timedelta(hours=1), '%I:%M %p'),
            datetime.datetime.strftime(utils.getGameStartTimeLocal(game.startTimeUTC), '%I:%M %p'),
            
            'http://www.nba.com/games/' + game.startDateEastern + '/' + vTeam.tricode + hTeam.tricode + '#/preview',
            'http://www.nba.com/games/' + game.startDateEastern + '/' + vTeam.tricode + hTeam.tricode + '#/matchup',
            'http://www.nba.com/games/' + game.startDateEastern + '/' + vTeam.tricode + hTeam.tricode + '#/pbp',
            'http://www.nba.com/games/' + game.startDateEastern + '/' + vTeam.tricode + hTeam.tricode + '#/boxscore',

            hTeam.arena,
            '',
            vTeam.subreddit,
            hTeam.subreddit
        )
        
        return body