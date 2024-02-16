class Scoreboard:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0

    def update_score(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1

    def get_score(self):
        return self.player1_score, self.player2_score

    def reset_score(self):
        self.player1_score = 0
        self.player2_score = 0


# Приклад використання:
if __name__ == "__main__":
    scoreboard = Scoreboard()
    scoreboard.update_score(1)  # гравець 1 забиває гол
    scoreboard.update_score(2)  # гравець 2 забиває гол
    print("Поточний рахунок:", scoreboard.get_score())  # вивід поточного рахунку
    scoreboard.reset_score()  # скидання рахунку
    print("Рахунок після скидання:", scoreboard.get_score())  # вивід рахунку після скидання
