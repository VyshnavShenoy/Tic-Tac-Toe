import random
import sys
import itertools


class Mode:

    def __init__(self):
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.cor = ['012', '345', '678', '036', '147', '258', '048', '246']
        self.x_no = 0
        self.o_no = 0

    def input_(self):
        while True:
            try:
                a, b = map(int, input("Enter the coordinates: ").split())
            except:
                print("You should enter numbers!")
                continue
            if a > 3 or b > 3 or a < 1 or b < 1:
                print("Coordinates should be from 1 to 3!")
                continue
            elif self.cells[a-1][b-1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            if self.x_no > self.o_no:
                self.cells[a-1][b-1] = "O"
                self.o_no += 1
            else:
                self.cells[a-1][b-1] = "X"
                self.x_no += 1
            return

    def easy(self):
        while True:
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            if self.cells[a-1][b-1] != " ":
                continue
            if self.x_no > self.o_no:
                self.cells[a-1][b-1] = "O"
                self.o_no += 1
            else:
                self.cells[a-1][b-1] = "X"
                self.x_no += 1
            return

    def medium(self):
        li_ = []
        move = "X"
        opp = "O"
        if self.x_no > self.o_no:
            move = "O"
            opp = "X"
            # self.o_no += 1
        else:
            pass
            # self.x_no += 1
        for i in range(3):
            li_.extend((self.cells[i]))
        for i in self.cor:
            count = 0
            for j in range(3):
                if li_[int(i[j])] == move:
                    count += 1
            if count == 2:
                if li_[int(i[0])] == " " or li_[int(i[1])] == " " or li_[int(i[2])] == " ":
                    li_[int(i[0])] = move
                    li_[int(i[1])] = move
                    li_[int(i[2])] = move
                    self.cells = []
                    for k in range(3):
                        self.cells.append(li_[3 * k:3 * (k + 1)])
                    if move == "O":
                        self.o_no += 1
                    else:
                        self.x_no += 1
                    return
        self.easy()

    def hard(self):
        li_ = []
        move = "X"
        opp = "O"
        if self.x_no > self.o_no:
            move = "O"
            opp = "X"
            # self.o_no += 1
        else:
            pass
            # self.x_no += 1
        for i in range(3):
            li_.extend((self.cells[i]))
        for i in self.cor:
            count = 0
            for j in range(3):
                if li_[int(i[j])] == move:
                    count += 1
            if count == 2:
                if li_[int(i[0])] == " " or li_[int(i[1])] == " " or li_[int(i[2])] == " ":
                    li_[int(i[0])] = move
                    li_[int(i[1])] = move
                    li_[int(i[2])] = move
                    self.cells = []
                    for k in range(3):
                        self.cells.append(li_[3 * k:3 * (k + 1)])
                    if move == "O":
                        self.o_no += 1
                    else:
                        self.x_no += 1
                    return
            count = 0
            pos = 0
            for j in range(3):
                if li_[int(i[j])] == opp:
                    count += 1
                if li_[int(i[j])] == " ":
                    pos = j
            if count == 2 and li_[int(i[pos])] == " ":
                li_[int(i[pos])] = move
                self.cells = []
                for k in range(3):
                    self.cells.append(li_[3 * k:3 * (k + 1)])
                if move == "O":
                    self.o_no += 1
                else:
                    self.x_no += 1
                return

        self.easy()

    def display_(self):
        print("---------")
        for i in range(3):
            print(f"| {self.cells[i][0]} {self.cells[i][1]} {self.cells[i][2]}|")
        print("---------")

    def check(self):
        li_ = []
        for i in range(3):
            li_.extend((self.cells[i]))
        for i in self.cor:
            if li_[int(i[0])] == "X" and li_[int(i[1])] == "X" and li_[int(i[2])] == "X":
                print("X wins")
                sys.exit()
            elif li_[int(i[0])] == "O" and li_[int(i[1])] == "O" and li_[int(i[2])] == "O":
                print("O wins")
                sys.exit()
        if self.x_no + self.o_no == 9:
            print("Draw")
            sys.exit()


class Tic(Mode):
    def main(self):
        while True:
            try:
                print("Modes: user, easy, medium, hard")
                b, c = input("Input command(format-'mode mode'): ").split()
            except:
                print("Bad parameters")
                continue
            self.display_()
            for i in itertools.cycle([b, c]):
                if i == "user":
                    self.input_()
                elif i == "easy":
                    print('Making move level "easy"')
                    self.easy()
                elif i == "medium":
                    print('Making move level "medium"')
                    self.medium()
                else:
                    print('Making move level "hard"')
                    self.hard()
                self.display_()
                self.check()


t1 = Tic()
t1.main()