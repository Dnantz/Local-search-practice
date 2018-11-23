import nqueens, random, math

## function determines new T value and returns it based off the given decay rate
def f(T, decay_rate):
    T = T*decay_rate
    return T

## function checks to see if the T has crossed the given threshold and returns boolean
def check(T, thresh):
    if(T>thresh):
        return False
    else:
        return True

## function solves and returns the acceptance probablity (e^(Delta/T))
def accept(delta, T):
    prob = 0
    dT = delta/T
    prob = math.e ** dT
    return prob

## function performs simulated anneal search and returns best heurustic valued board state
def simAnneal(current, T, decay_rate, thresh):
    while(True):
        T = f(T, decay_rate)
        if(check(T, thresh)):
            return current
        if(nqueens.numAttackingQueens(current) == 0):
            return current
        next = nqueens.getSuccessorStates(current)[random.randint(0, len(nqueens.getSuccessorStates(current)) - 1)]
        delta = nqueens.numAttackingQueens(current) - nqueens.numAttackingQueens(next)
        if (delta > 0):
            current = next
        else:
            if (accept(delta, T) > .5):
                current = next            
    return current

## function prints cycles through board sizes, decay/threshold pairs, and initial state runs
## function prints these values orderly, and runs simAnneal function to find best best board for each run
## function deterines best board by lowest num of conflicting queens, and is printed at end of each run
## function then finds the average hueristic value of each run in the pair and prints it to console
def main():
    pairs = [[0.9, 0.000001, '0.000001'], [0.75, 0.0000001, '0.0000001'], [0.5, 0.00000001, '0.00000001']] 
    boardNum = 10
    boardSize = 4
    for s in range(3):
        print '################### BOARD SIZE: {} ###################'.format(boardSize)
        s = []
        for b in range(boardNum):
            b = nqueens.Board(boardSize)
            b.rand()
            s.append(b)
        for p in pairs:
            total = 0
            print '####### Decay: {}  T Threshold: {} #######'.format(p[0], p[2])
            for r in range(boardNum):
                print '#####Run {}#####'.format(r)
                print "Initial board: "
                temp = s[r] 
                T = 100
                temp.printBoard()
                print "h-value: {}".format(nqueens.numAttackingQueens(temp))     
                temp = simAnneal(temp, T, p[0], p[1])
                value = nqueens.numAttackingQueens(temp)
                total += value
                print "Final board:"    
                temp.printBoard()
                print "Final board h-value: {}".format(value)
            print '####### Average h-value for pair: {} #######'.format(float(total)/boardNum)
        boardSize = boardSize + boardSize
        if (boardSize < 17):
            raw_input('Press \'Enter\' to move on to next board size')


main()