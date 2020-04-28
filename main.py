import random


class RockPaperScissors:
    def __init__(self):
        self.beats = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}
        self.choiceList = list(self.beats.keys())

    def get_username(self):
        self.username = input("Enter your name:")
        print("Hello, " + self.username)

    def get_user_rating(self):
        with open("rating.txt", "r") as f:
            lines = f.read().splitlines()
            self.ratings = dict()
            for line in lines:
                user, rating = line.split()
                self.ratings[user] = int(rating)
            if self.username not in self.ratings.keys():
                self.ratings[self.username] = 0

    def update_user_rating(self):
        with open("rating.txt", "w") as f:
            for key, value in self.ratings.items():
                print(key, value, file=f)

    def play(self):
        self.comp_choice = random.choice(self.choiceList)
        self.user_choice = input()
        if self.user_choice == "!exit":
            return "Bye!"
        elif self.user_choice == "!rating":
            return "Your rating: " + str(self.ratings[self.username])
        elif self.user_choice not in self.choiceList:
            return "Invalid input"
        elif self.user_choice == self.comp_choice:
            self.ratings[self.username] += 50
            return "There is a draw (" + self.user_choice + ")"
        elif self.user_choice in self.beats[self.comp_choice]:
            return "Sorry, but computer chose " + self.comp_choice
        else:
            self.ratings[self.username] += 100
            return "Well done. Computer chose " + self.comp_choice + " and failed"

    def get_gameList(self):
        inputList = input()
        if inputList != '':
            gameList = [*map(str, inputList.split(','))]
            gameListLen = len(gameList)
            gameList = gameList + gameList
            self.beats = dict()
            for i in range(0, gameListLen):
                self.beats[gameList[i + gameListLen]] = gameList[i + gameListLen - (gameListLen) // 2:i + gameListLen]
            self.choiceList = list(self.beats.keys())
        print("Okay, let's start")

    def start(self):
        self.get_username()
        self.get_gameList()
        self.get_user_rating()
        while True:
            verdict = self.play()
            print(verdict)
            if verdict == 'Bye!':
                break
        # self.update_user_rating()


game = RockPaperScissors()
game.start()