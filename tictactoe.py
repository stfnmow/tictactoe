import random
import itertools



def zeigplan():
    print('\n')
    for row in range (3):
        print(f'{spielplan[row][0]} | {spielplan[row][1]} | {spielplan[row][2]}')
        if row < 2:
            print('- + - + -')
    print('\n')

def markturningameplan(mark,x,y):
    spielplan[x][y]=mark
    planmeta[x][y] = 1 if mark=='X' else -1
    
def decideturn(mark):
    turnsum=-1
    for sum in range(len(rowsums)):
        if abs(rowsums[sum]) == 2:
            turnsum=sum
            break
    
    # Wenn keine Zeile, Spalte oder Diagonale 2 gleiche Marker bei freiem dritten Platz hat,
    # wähle zufällig eine Position als Zug. Verifiziere, dass die Position noch frei ist.
    if turnsum == -1:
        while True:
            choice = random.randint(1,9)
            if spielplan[(choice-1) // 3][(choice-1) % 3]==' ':
                markturningameplan(mark,(choice-1) // 3,(choice-1) % 3)
                break

    # sonst, wenn in eine der 2 Zeilen oder Spalten ein Zweier vorliegt, setze den Zug dort...                
    for reihe in range(3):
        if turnsum == reihe:
            for reihenelement in range(3):
                if spielplan[reihe][reihenelement]==' ':
                    markturningameplan(mark,reihe,reihenelement)
                    break
        if turnsum == reihe+3:
            for reihenelement in range(3):
                if spielplan[reihenelement][reihe]==' ':
                    markturningameplan(mark,reihenelement,reihe)
                    break
    
    # sonst, wenn in einer der beiden Diagonalen ein Zweier vorliegt, setze dort.
    for reihenelement in range(3):
        if turnsum == 6:
            if spielplan[reihenelement][reihenelement]==' ':
                markturningameplan(mark,reihenelement,reihenelement)
                break
        elif turnsum == 7:
            if spielplan[reihenelement][2-reihenelement]==' ':
                markturningameplan(mark,reihenelement,2-reihenelement)
                break

def playturn(player,mark):
    global spielplan
    global planmeta
    if player==3:
        decideturn(mark)
    else:
        spot=int(input(f'Player {player}, please input your next movement: '))
        while spielplan[(spot-1) // 3][(spot-1) % 3] != ' ':
            print('That place is already taken! Please try again.')
            spot=int(input(f'Player {player}, please input your next movement: '))
        
        markturningameplan(mark,(spot-1) // 3, (spot-1) % 3)

def reihensummieren():
    global rowsums
    for row in range(3):
        rowsums[row]=planmeta[row][0] + planmeta[row][1] + planmeta[row][2]
    
    for col in range(3):
        rowsums[col+3]=planmeta[0][col] + planmeta[1][col] + planmeta[2][col]
    
    rowsums[6]=planmeta[0][0] + planmeta[1][1] + planmeta[2][2]
    rowsums[7]=planmeta[2][0] + planmeta[1][1] + planmeta[0][2]

def initializeBoard(fill):
    for row, col in itertools.product(range(3), range(3)):
        spielplan[row][col] = ' ' if fill=='empty' else  row*3 + col + 1

############################################################################
############################################################################
############################################################################

# TODO:
# Liste von noch freien Positionen (verhindert zufällige Suche, bis freie Position erwischt wird. Erleichtert Verifikation eines Zugs)
# Falsche eingaben (außerhalb von 1-9) abfangen
# ...



spielplan = [['','',''],['','',''],['','','']]



print('\n Let\'s play TicTacToe! Input your turn like this:\n')
initializeBoard('numbers')
zeigplan()

playagain = True
while playagain:
    initializeBoard('empty')


    planmeta = [[0,0,0],[0,0,0],[0,0,0]]
    rowsums = [0,0,0,0,0,0,0,0]
    turn = 1
    turnplayer = [0,0,0,0,0,0,0,0,0]

    symbol=' '



    mode=int(input('please input mode: 1 for player vs cpu, 2 for two players: '))
    if mode==1:
        beginner=int(input('Who starts? 1 for you, 2 for me: '))
        if beginner==1:
            turnplayer = [1,3,1,3,1,3,1,3,1]
        else:
            turnplayer = [3,1,3,1,3,1,3,1,3]

    else:
        turnplayer = [1,2,1,2,1,2,1,2,1]


    while turn <= 9:
        symbol = 'O' if turn % 2 == 0 else 'X'
        zeigplan()
        playturn(turnplayer[turn-1],symbol)
        reihensummieren()
        if max(rowsums)==3 or min(rowsums)==-3:
            print('\nWe have a winner!')
            break
        turn = turn+1

    zeigplan()
    print('End of Game\n')

    playagain = bool(int(input('Do you want to play another round? 1 for yes, 0 for no: ')))

print('kthxby')
