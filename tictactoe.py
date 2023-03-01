import random

spielplan = [['','',''],['','',''],['','','']]
planmeta = [[0,0,0],[0,0,0],[0,0,0]]
rowsums = [0,0,0,0,0,0,0,0]


# TODO:
# Liste von noch freien Positionen (verhindert zufällige Suche, bis freie Position erwischt wird. Erleichtert Verifikation eines Zugs)
# ...

turn = 1
turnplayer = [0,0,0,0,0,0,0,0,0]

symbol=' '

def zeigplan():
    print('\n')
    for row in range (3):
        print(f'{spielplan[row][0]} | {spielplan[row][1]} | {spielplan[row][2]}')
        if row < 2:
            print('- + - + -')
    print('\n')

def markturningameplan(mark,x,y):
    spielplan[x][y]=mark
    if mark=='X':
        planmeta[x][y] = 1
    else:
        planmeta[x][y] = -1
    
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
    
    if turnsum == 6:
        for reihenelement in range(3):
            if spielplan[reihenelement][reihenelement]==' ':
                markturningameplan(mark,reihenelement,reihenelement)
                break
    if turnsum == 7:
        for reihenelement in range(3):
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
            print('der zug war quatsch')
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

############################################################################

print('\n Let\'s play TicTacToe! Input your turn like this:\n')
for row in range(3):
    for col in range(3):
        spielplan[row][col] = row*3 + col + 1

zeigplan()

for row in range(3):
    for col in range(3):
        spielplan[row][col] = ' '


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
    if turn % 2 == 0:
        symbol = 'O'
    else:
        symbol = 'X'
    zeigplan()
    playturn(turnplayer[turn-1],symbol)
    reihensummieren()
    if max(rowsums)==3 or min(rowsums)==-3:
        print('\nWe have a winner!')
        break
    turn = turn+1
    
zeigplan()
print('Das Spiel ist zuende\n')