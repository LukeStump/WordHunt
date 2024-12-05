# The Main file of the Game
import board
import game


def playTest():
    gameBoard = board.makeBoard("OATRIHPSHTNRENEI",4,4)
    g = game.Game(gameBoard)
    g.timer.start_time()
    while(True):
        v = g.scorePlayerInput()
        print("--->",v)

playTest()