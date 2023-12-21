class Square:
    def __init__(self, pos, type, score, max_pieces, red_pieces, black_pieces, distribution):
        self.pos = pos 
        self.type = type
        self.score = score
        self.max_pieces = max_pieces
        self.red_pieces = red_pieces
        self.black_pieces = black_pieces
        self.distribution = distribution
        pass

    def is_full(self):
        return self.get_total_pieces() == self.max_pieces
    
    def add_piece(self, piece, pos):
        if piece == "1":
            self.red_pieces+= 1
        else:
            self.black_pieces+= 1
        self.distribution[pos] = piece
    
    def remove_piece(self, piece, pos):
        if piece == "1":
            self.red_pieces-= 1
        else:
            self.black_pieces-= 1
        self.distribution[pos] = 0

    def get_total_pieces(self):
        return self.black_pieces + self.red_pieces

    def get_score(self, piece):
        if piece == "1":
            return self.red_pieces * self.score
        
        else:
            return self.black_pieces * self.score
        
    def get_empty_pos(self):

        empty_pos = []
        for i in range(self.max_pieces):
            if self.distribution[i] == 0:
                empty_pos.append(i)
        
        return empty_pos
    
    def get_pos_pieces(self, piece):
        pos_pieces = []
        for i in range(self.max_pieces):
            if self.distribution[i] == piece:
                pos_pieces.append(i)
        
        return pos_pieces
    
    def __str__(self):
        return f"Square(pos={self.pos}, type={self.type}, score={self.score}, max_pieces={self.max_pieces}, red_pieces={self.red_pieces}, 
        black_pieces={self.black_pieces}, distribution={self.distribution})"

