class Player:
    def __init__(self, piece = "N/A"):
        self.piece = piece
        self.name = "unknown"
        self.positions = []

    def __str__(self):
        return "{} is playing as {}.".format(self.name, self.piece)

    def askName(self):
        self.name = input("Enter your name: ")
        while self.name.strip() == "":
            print("Invalid name! ")
            self.name = input("Enter your name: ")
        
    def choosePiece(self):
        self.piece = input("Choose your piece (X/O): ")
        if self.piece == "X" or self.piece == "O":
            return self.__str__()
        else:
            self.piece = "N/A"
            return "Invalid piece!"

    def addPos(self, num):
        self.positions.append(int(num))
        self.positions.sort()

class Computer:
    def __init__(self, piece = "N/A"):
        self.piece = piece
        self.positions = []
        self.name = "Computer"

    def __str__(self):
        return "The computer is playing as {}.".format(self.piece)

    def addPos(self, num):
        self.positions.append(int(num))
        self.positions.sort()

class Play:
    def __init__(self):
        self.rowone = "   |   |   "
        self.rowtwo = "   |   |   "
        self.rowthree = "   |   |   "
        self.spacerbottom = "\n___|___|___\n"
        self.spacertop = "\n   |   |   \n"
        self.board = (self.spacertop + self.rowone + self.spacerbottom
                      + self.spacertop + self.rowtwo + self.spacerbottom
                      + self.spacertop + self.rowthree + self.spacertop)
        self.wins = [[1,2,3], [1,5,9], [1,4,7], [2,5,8], [3,5,7], [3,6,9], [4,5,6], [7,8,9]]
        self.start = (self.spacertop + " 1 | 2 | 3 " + self.spacerbottom
                      + self.spacertop + " 4 | 5 | 6 " + self.spacerbottom
                      + self.spacertop + " 7 | 8 | 9 " + self.spacertop)
        
    def __str__(self):
        return self.start

    def playerChoice(self, player):
        space = input("{}, choose space 1-9 to place your piece: ".format(player.name))
        return space

    def computerChoice(self, computer, player):
        if len(player.positions) == 1:
            choice = player.positions[0]
            if 5 not in player.positions and 5 not in computer.positions:
                return "5"
            else:
                if 1 != choice:
                    return "1"
                elif 3 != choice:
                    return "3"
                elif 7 != choice:
                    return "7"
                elif 9 != choice:
                    return "9"

        elif len(player.positions) == 2:
            for win in self.wins:
                if player.positions[0] in win and player.positions[1] in win:
                    first = player.positions[0]
                    second = player.positions[1]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
            if 1 not in player.positions and 1 not in computer.positions:
                return "1"
            elif 3 not in player.positions and 3 not in computer.positions:
                return "3"
            elif 7 not in player.positions and 7 not in computer.positions:
                return "7"
            elif 9 not in player.positions and 9 not in computer.positions:
                return "9"

        elif len(player.positions) == 3:
            for win in self.wins:
                if computer.positions[0] in win and computer.positions[1] in win:
                    first = computer.positions[0]
                    second = computer.positions[1]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in player.positions: 
                        return str(tempwin[0])
            for win in self.wins:
                if player.positions[0] in win and player.positions[1] in win:
                    first = player.positions[0]
                    second = player.positions[1]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
                if player.positions[0] in win and player.positions[2] in win:
                    first = player.positions[0]
                    second = player.positions[2]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
                if player.positions[1] in win and player.positions[2] in win:
                    first = player.positions[1]
                    second = player.positions[2]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
            if 1 not in player.positions and 1 not in computer.positions:
                return "1"
            elif 3 not in player.positions and 3 not in computer.positions:
                return "3"
            elif 7 not in player.positions and 7 not in computer.positions:
                return "7"
            elif 9 not in player.positions and 9 not in computer.positions:
                return "9"

        elif len(player.positions) == 4:
            for win in self.wins:
                if computer.positions[0] in win and computer.positions[1] in win:
                    first = computer.positions[0]
                    second = computer.positions[1]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in player.positions: 
                        return str(tempwin[0])
                if computer.positions[0] in win and computer.positions[2] in win:
                    first = computer.positions[0]
                    second = computer.positions[2]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in player.positions: 
                        return str(tempwin[0])
                if computer.positions[1] in win and computer.positions[2] in win:
                    first = computer.positions[1]
                    second = computer.positions[2]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in player.positions: 
                        return str(tempwin[0])
            for win in self.wins:     
                if player.positions[0] in win and player.positions[1] in win:
                    first = player.positions[0]
                    second = player.positions[1]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
                if player.positions[0] in win and player.positions[2] in win:
                    first = player.positions[0]
                    second = player.positions[2]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
                if player.positions[0] in win and player.positions[3] in win:
                    first = player.positions[0]
                    second = player.positions[3]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
                if player.positions[1] in win and player.positions[2] in win:
                    first = player.positions[1]
                    second = player.positions[2]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
                if player.positions[1] in win and player.positions[3] in win:
                    first = player.positions[1]
                    second = player.positions[3]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
                if player.positions[2] in win and player.positions[3] in win:
                    first = player.positions[2]
                    second = player.positions[3]
                    tempwin = []
                    for num in win:
                        tempwin.append(num)
                    tempwin.remove(first)
                    tempwin.remove(second)
                    if tempwin[0] not in computer.positions: 
                        return str(tempwin[0])
            if 1 not in player.positions and 1 not in computer.positions:
                return "1"
            elif 3 not in player.positions and 3 not in computer.positions:
                return "3"
            elif 7 not in player.positions and 7 not in computer.positions:
                return "7"
            elif 9 not in player.positions and 9 not in computer.positions:
                return "9"
            elif 2 not in player.positions and 2 not in computer.positions:
                return "2"
            elif 4 not in player.positions and 4 not in computer.positions:
                return "4"
            elif 6 not in player.positions and 6 not in computer.positions:
                return "6"
            elif 8 not in player.positions and 8 not in computer.positions:
                return "8"
        
        
    def placePiece(self, player, space):
        if space == "1":
            self.rowone = " {} |".format(player.piece) + self.rowone[4:]
            self.board = self.board[:13] + self.rowone + self.board[24:]
            player.addPos(space)
            return self.board
        elif space == "2":
            self.rowone = self.rowone[:4]+ " {} |".format(player.piece) + self.rowone[8:]
            self.board = self.board[:13] + self.rowone + self.board[24:]
            player.addPos(space)
            return self.board
        elif space == "3":
            self.rowone = self.rowone[:8]+ " {} ".format(player.piece)
            self.board = self.board[:13] + self.rowone + self.board[24:]
            player.addPos(space)
            return self.board
        elif space == "4":
            self.rowtwo = " {} |".format(player.piece) + self.rowtwo[4:]
            self.board = self.board[:50] + self.rowtwo + self.board[61:]
            player.addPos(space)
            return self.board
        elif space == "5":
            self.rowtwo = self.rowtwo[:4]+ " {} |".format(player.piece) + self.rowtwo[8:]
            self.board = self.board[:50] + self.rowtwo + self.board[61:]
            player.addPos(space)
            return self.board
        elif space == "6":
            self.rowtwo = self.rowtwo[:8]+ " {} ".format(player.piece)
            self.board = self.board[:50] + self.rowtwo + self.board[61:]
            player.addPos(space)
            return self.board
        elif space == "7":
            self.rowthree = " {} |".format(player.piece) + self.rowthree[4:]
            self.board = self.board[:87] + self.rowthree + self.board[98:]
            player.addPos(space)
            return self.board
        elif space == "8":
            self.rowthree = self.rowthree[:4]+ " {} |".format(player.piece) + self.rowthree[8:]
            self.board = self.board[:87] + self.rowthree + self.board[98:]
            player.addPos(space)
            return self.board
        elif space == "9":
            self.rowthree = self.rowthree[:8]+ " {} ".format(player.piece)
            self.board = self.board[:87] + self.rowthree + self.board[98:]
            player.addPos(space)
            return self.board
        else:
            return "Invalid move."

    def win(self, player, computer):
        totalPos = player.positions + computer.positions
        if len(totalPos) == 9:
            return "It's a tie between {} and {}!".format(player.name, computer.name)
        
        p1 = player.positions
        if len(p1) == 3:
            if p1 in self.wins:
                return "{} wins!".format(player.name)
        if len(p1) == 4:
            p1 = [[p1[0], p1[1], p1[2]], [p1[0], p1[1], p1[3]],
                  [p1[0], p1[2], p1[3]],
                  [p1[1], p1[2], p1[3]]]
        elif len(p1) == 5:
            p1 = [[p1[0], p1[1], p1[2]], [p1[0], p1[1], p1[3]], [p1[0], p1[1], p1[4]],
                  [p1[0], p1[2], p1[3]], [p1[0], p1[2], p1[4]],
                  [p1[0], p1[3], p1[4]],
                  [p1[1], p1[2], p1[3]], [p1[1], p1[2], p1[4]],
                  [p1[1], p1[3], p1[4]],
                  [p1[2], p1[3], p1[4]]]
            
        p2 = computer.positions
        if len(p2) == 3:
            if p2 in self.wins:
                return "{} wins!".format(computer.name)
        if len(p2) == 4:
            p2 = [[p2[0], p2[1], p2[2]], [p2[0], p2[1], p2[3]],
                  [p2[0], p2[2], p2[3]],
                  [p2[1], p2[2], p2[3]]]
        elif len(p2) == 5:
            p2 = [[p2[0], p2[1], p2[2]], [p2[0], p2[1], p2[3]], [p2[0], p2[1], p2[4]],
                  [p2[0], p2[2], p2[3]], [p2[0], p2[2], p2[4]],
                  [p2[0], p2[3], p2[4]],
                  [p2[1], p2[2], p2[3]], [p2[1], p2[2], p2[4]],
                  [p2[1], p2[3], p2[4]],
                  [p2[2], p2[3], p2[4]]]
        for combo in p1:
            if combo in self.wins:
                return "{} wins!".format(player.name)
        for combo in p2:
            if combo in self.wins:
                return "{} wins!".format(computer.name)
        return "Continue playing."
                
player = Player()
player.askName()
while player.piece == "N/A":
    print(player.choosePiece())

computer = Computer()
if player.piece == "X":
    computer.piece = "O"
else:
    computer.piece = "X"
print(computer)

play = Play()
print(play)
while play.win(player, computer) == "Continue playing.":
    p1choice = play.playerChoice(player)
    resultP1 = play.placePiece(player, p1choice)
    print(resultP1)
    while resultP1 == "Invalid move.":
        p1choice = play.playerChoice(player)
        resultP1 = play.placePiece(player, p1choice)
        print(resultP1)
    play.win(player, computer)
    if play.win(player, computer) == "Continue playing.":
        cChoice = play.computerChoice(computer, player)
        resultP2 = play.placePiece(computer, cChoice)
        print(resultP2)
        while resultP2 == "Invalid move.":
            resultP2 = play.placePiece(computer, cChoice)
            print(resultP2)
        if play.win(player, computer) != "Continue playing.":
            print(play.win(player, computer))
    else:
        print(play.win(player, computer))
        break
