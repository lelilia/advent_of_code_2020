player1 = [9, 2, 6, 3, 1]
player2 = [5, 8, 4, 7, 10]

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.gameover = False
        self.winner = None
        self.seen = {}

    def __repr__(self):
        return f'<Game: \n\tplayer1 {self.player1}\n\tplayer2 {self.player2}'

    def play_round(self):
        while not self.gameover:
            if len(self.player1) == 0 or len(self.player2) == 0:
                self.gameover = True
                self.score()
            else:
                card1 = self.player1.pop(0)
                card2 = self.player2.pop(0)

                if card1 > card2:
                    self.player1.extend([card1, card2])
                else:
                    self.player2.extend([card2, card1])

    def play_recursive(self):
        while not self.gameover:
            if len(self.player1) == 0:
                self.winner = 'player2'
                self.gameover = True
                return
            if len(self.player2) == 0:
                self.winner = 'player1'
                self.gameover = True
                return

            #seen = ','.join(self.player1) + '\n' + ','.join(self.player2)
            seen = (tuple(self.player1), tuple(self.player2))
            if seen in self.seen:
                self.winner = 'player1'
                self.gameover = True
                return
            else:
                self.seen[seen] = True

            card1 = self.player1.pop(0)
            card2 = self.player2.pop(0)



            if card1 > len(self.player1) or card2 > len(self.player2):
                if card1 > card2:
                    self.player1.extend([card1, card2])
                else:
                    self.player2.extend([card2, card1])
            else:
                subgame = Game(self.player1[:card1].copy(), self.player2[:card2].copy())
                subgame.play_recursive()
                if subgame.winner == 'player1':
                    self.player1.extend([card1, card2])
                else:
                    self.player2.extend([card2, card1])


    def score(self):
        score = 0
        if len(self.player1) > 0:
            score = sum([(index + 1) * card for index, card in enumerate(self.player1[::-1])])
        else:
            for index, card in enumerate(self.player2[::-1]):
                score += (index+1) * card
        print(score)
        return score



if __name__ == '__main__':
    p1, p2 = open('input/day22.txt').read().split('\n\n')

    p1 = p1.split('\n')[1:]
    p1 = [int(i) for i in p1]
    p2 = p2.split('\n')[1:]
    p2 = [int(i) for i in p2]


    game = Game(p1.copy(), p2.copy())

    game.play_round()


    game2 = Game(p1, p2)


    game2.play_recursive()

    game2.score()