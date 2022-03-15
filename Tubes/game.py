class Game:
    def __init__(self, id) :
        self.p1Went = False
        self.p2Went = False
        self.ready= False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :parameter p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        """
        Fungsi untuk ngedeteksi kalo semua player udah suit game
        """
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else :
            self.p2Went = True

    def connected(self):
        """
        Fungsi untuk ngedeteksi kalo semua player udah join game
        """
        return self.ready

    def bothWent(self):
        """
        Fungsi untuk ngedeteksi kalo semua player udah suit game
        """
        return self.p1Went and self.p2Went

    def winner(self):
        """
        Fungsi untuk nentuin player mana yang menang
        P : Paper
        R : Rock 
        S : Scissors
        """
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        if p1 == p2:
            winner = -1
        elif p1+p2 in ('PR', 'RS', 'SP'):
            winner = 0
        else:
            winner = 1

        return winner

    def resetGame(self):
        """
        Fungsi untuk reset game
        """
        self.p1Went = False
        self.p2Went = False