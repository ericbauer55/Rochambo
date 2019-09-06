class Rochambo:
    def __init__(self):
        self.y = 'RR'  # initial moves string

    def wins(self, opponent):
        numWins = 0  # initialize running sum
        x = opponent  # relabel input
        self.generateMoves(x)  # generate moves into self.y
        for i in range(len(x)):
            if (self.beats(self.y[i], x[i])):
                numWins += 1
        return numWins

    @staticmethod
    def beats(a, b):
        # this determines if @a beats @b in rock, paper, scissors
        # @a, @b are both strings and only 'R', 'P', 'S'
        if b == 'R' and a == 'P':
            return True
        elif b == 'P' and a == 'S':
            return True
        elif b == 'S' and a == 'R':
            return True
        else:
            # for a given opponent play @b, there is only one @a play that wins.
            # any other combination is a tie or a loss
            return False

    def generateMoves(self, x):
        # this generates the predicted move into self.y given x
        self.y = 'RR' # reset the move set of each time
        valid_moves = 'RPS'  # string array of possible moves
        for i in range(2, len(x)):
            if x[i - 1] == x[i - 2]:
                xEst = x[i - 1]  # the estimated new x is the same as the past two
            else:  # the past two are different
                # HOW do I find which one of @moves is not used?
                moves = valid_moves
                moves = moves.replace(x[i - 1], '', 1)
                moves = moves.replace(x[i - 2], '', 1)
                xEst = moves  # opponent predicted to use remaining move
            xEstIndex = valid_moves.find(xEst)  # index of estimated move in move list
            # the move one to the right in a circular list always beats the preceding item
            self.y += valid_moves[(xEstIndex + 1) % len(valid_moves)]


if __name__ == '__main__':
    z = Rochambo()
    x = 'RPPPRRPSSSRRRSRSPPSSPRRPSRRRRSPPPPSSPSSSSSRSSSRPRR'
    z.generateMoves(x)
    print("Opponent: {}\nYou:\t  {}".format(x, z.y))
    print("Number of Your Wins: {}".format(z.wins(x)))