"""Demonstrate the features of the package with a small interactive execution

The "import __init__ as nimgame" simulates, as if the "nimgame" package was
imported after installation, so that elements like the Nim class can be used as
"nimgame.Nim"
"""


def run():
    import __init__ as nimgame
    from source.playing.cli import ansi


    try:
        while True:
            testtype = input(
                'Press '
                '"m" for running multiple games'
                '; '
                '"p" for playing an interactive game'
                '; '
                '"w" for running the web server'
                '; [p]: '
            ) or 'p'
            ansi.clean_prev_line()

            if testtype=='m':
                #do the test with 1000 games
                gamecount = 1000
                #request 10% Computer and 20% Player error rate
                error_rate = nimgame.ErrorRate(Computer=10, Player=20)
                #run all tests
                from tests import testruns
                testruns.run_many_games(gamecount, error_rate)
                break
            
            elif testtype=='p':
                nimgame.play_CLI()
                break
            
            elif testtype=='w':
                nimgame.playweb()
                break

    except KeyboardInterrupt:
        #Ctrl-C happens when input is waiting, so delete that prompt
        ansi.clean_this_line()
        print('Game terminated by the user pressing Ctrl-C')
        exit(2)
        
    except Exception as e:
        print(e)
        exit(1)

    exit(0)


if __name__ == '__main__':
    run()
