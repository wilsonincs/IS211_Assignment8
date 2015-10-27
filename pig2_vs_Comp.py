
import random
import sys
import argparse
import time


#define player class

class Player(object):

        def __init__(self):

            self.score = 0
            self.roll = True
            self.hold = False
            self.turn = False
            self.scoreAtspecificTurn = 0

        def deciding(self):

            decision = raw_input('%s: Would you like to Hold or Roll ? (h/r)?' % self.name)
            decision = str(decision)

            if decision != "h" or "r":
                print "wrong input, enter again your decision"
                self.deciding

            else:
                if decision == 'h' or decision == 'H':
                    self.hold = True
                    self.roll = False

                elif decision == 'r' or decision == 'R':
                    self.hold = False
                    self.roll = True

#The Die class has integer attributes from 1 to 6
class Die(object):

        def __init__(self):
            self.value = int()

        def roll(self):
            self.value = random.randint(1,6)        #the roll function generates number between 1 and 6


#define computer class which takes player as a parameter

class Computer(Player):

	def deciding(self):

		minimum = 25
		maximum = 100 - self.score
		if(minimum < maximum):
			limit = minimum
		else:
			limit = maximum

		if(self.scoreAtspecificTurn < limit):
			print "Roll the die"
			self.hold = False
			self.roll = True
		else:
			print "Hold the die"
			self.hold = True
			self.roll = False

class PlayerFactory():
	def __init__(self):
		return None

	def createplayer(self,playertype):
		if playertype == 'human':
			return Player()
		elif playertype == 'computer':
			return Computer()

class Game(object):

    def __init__(self,player1,player2,die):

        self.scoreAtspecificTurn = 0
        self.player1 = player1
        self.player1.score = 0
        self.player1.scoreAtspecificTurn = self.scoreAtspecificTurn
        self.player1.name = "Player 1"

        self.player2 = player2
        self.player2.score = 0
        self.player2.scoreAtspecificTurn = self.scoreAtspecificTurn
        self.player2.name = "Player 2"
        self.die = Die()

        coinplay = random.randint(1,2)

        if coinplay == 1:
            self.current_player = player1
            print "Coin result in player 1 decision, player 1 can begin"

        elif coinplay == 2:
            self.current_player = player2
            print "Coin result in player 1 decision, player 2 can begin "

        else:
            print "no one's side selection, flip again"

        self.turn()


    def newturn(self):

        self.scoreAtspecificTurn = 0
        if self.player1.score >= 100:

            print "End of the game player 1 wins!"
            print "Final player 1 score:",self.player1.score
            self.gamends()
            main()

        elif self.player2.score >= 100:

            print "End of the game player 2 wins!"
            print "Final player 2 Score:",self.player2.score
            self.gamends()
            main()

        else:
            if self.current_player == self.player1:
                self.current_player = self.player2
            elif self.current_player == self.player2:
                self.current_player = self.player1
            else:
                print "error , try flipping again"

            print "Flip the coin for a new turn player : ", self.current_player.name
            self.turn()

    def turn(self):

        print "Current Player 1 Score:", self.player1.score
        print "Current Player 2 Score:", self.player2.score

        self.die.roll()

        if(self.die.value == 1):
            print "you got 1 , points = 0 !"
            self.scoreAtspecificTurn = 0
            self.newturn()

        else:

            self.scoreAtspecificTurn += self.die.value
            print "Dice shows you a:",self.die.value
            print "Your current score is:", self.scoreAtspecificTurn

            self.current_player.deciding()
            if(self.current_player.hold == True and self.current_player.roll == False):
                self.current_player.score = self.current_player.score + self.scoreAtspecificTurn
                self.newturn()
            elif(self.current_player.hold == False and self.current_player.roll == True):
                self.turn()

    def gamends(self):
        self.player1 = None
        self.player2 = None
        self.die = None
        self.scoreAtspecificTurn = None


class TimedGameProxy(Game):

    def __init__(self,player1,player2,die):

        self.player1 = player1
        self.player1.score = 0
        self.player1.scoreAtspecificTurn = self.scoreAtspecificTurn
        self.player1.name = "Player 1"

        self.player2 = player2
        self.player2.score = 0
        self.player2.scoreAtspecificTurn = self.scoreAtspecificTurn
        self.player2.name = "Player 2"

        self.scoreAtspecificTurn = 0
        self.die = Die()
        self.start_time = time.time()

        coinplay = random.randint(1,2)

        if coinplay == 1:
            self.current_player = player1
            print "Coin result in player 1 decision, player 1 can begin"

        elif coinplay == 2:
            self.current_player = player2
            print "Coin result in player 1 decision, player 2 can begin "

        else:
            print "no one's side selection, flip again"
        self.turn()


    def newturn(self):

        self.scoreAtspecificTurn = 0

        if self.player1.score >= 100:
            print "End of the game player 1 wins!"
            print "Final player 1 score:",self.player1.score
            self.gamends()
            main()

        elif self.player2.score >= 100:
            print "End of the game player 2 wins!"
            print "Final player 2 Score:",self.player2.score
            self.gamends()
            main()

        else:
            if self.current_player == self.player1:
                self.current_player = self.player2
            elif self.current_player == self.player2:
                self.current_player = self.player1
            else:
                print "error , try flipping again"

            print "Flip the coin for a new turn player : ", self.current_player.name
            self.turn()

    def turn(self):

        self.actual_time = time.time()
        if(self.actual_time - self.start_time >= 60):
            self.timeisover()

        else:
            print "Current Player 1 Score:", self.player1.score
            print "Current Player 2 Score:", self.player2.score
            self.die.roll()

            if(self.die.value == 1):
                print "you got 1 , points = 0 !"
                self.scoreAtspecificTurn = 0
                self.newturn()

            else:
                self.scoreAtspecificTurn += self.die.value
                self.player1.scoreAtspecificTurn = self.scoreAtspecificTurn
                self.player2.scoreAtspecificTurn = self.scoreAtspecificTurn
                print "Dice shows you a:",self.die.value
                print "Your current score is:", self.scoreAtspecificTurn

                self.current_player.deciding()
                if(self.current_player.hold == True and self.current_player.roll == False):
                    self.current_player.score = self.current_player.score + self.scoreAtspecificTurn
                    self.newturn()
                elif(self.current_player.hold == False and self.current_player.roll == True):
                    self.turn()

    def timeisover(self):

        print "End of the game, the time is over!"
        print "-------------------------------"
        print "The final score for Player 1 is:", self.player1.score
        print "The final score for Player 1 is:", self.player2.score

        if self.player1.score > self.player2.score:
            print "Player 1 scored more, therefore he wins"
            self.endgame()
            main()

        elif self.player2.score > self.player1.score:
            print "Player 1 scored more, therefore he wins"
            self.gamends()
            main()
        else:
            print "Scores between players are the same, it is a tie"
            self.gamends()
            main()


parser = argparse.ArgumentParser()
parser.add_argument('--player1', help='human or computer')
parser.add_argument('--player2', help='human or computer')
parser.add_argument('--timed', help='time on game')
args = parser.parse_args()



if not args.player1:
	player1choice = 'human'
else:
	player1choice = args.player1

if not args.player2:
	player2choice = 'human'
else:
	player2choice = args.player2


def main():

    start = raw_input("Would you like to start a new game?, Yes(Y) or No(N)?")
    if start == 'Y' or start == 'y':
        playerfactory = PlayerFactory()
        player1 = playerfactory.createplayer(player1choice)
        player2 = playerfactory.createplayer(player2choice)
        die = Die()

        if not args.timed:
            newgame = Game(player1,player2,die)
        else:
            newgame = TimedGameProxy(player1,player2,die)

    elif start == 'N' or start == 'n':
        print "Ok bye"
        sys.exit()

    else:
        print "Type (Y) or (N) for choices also (y) or (n)"


if __name__ == '__main__':
    main()