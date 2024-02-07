class Bishops:
    def move(self):
        print('bishops move diagonally')

class Knights:
    def move(self):
        print('knoghts move two squares vertically and horizonatlly')

#common interface
def move_test(chess_piece_obj):
    chess_piece_obj.move()

#driver code
bishop = Bishops()
knight = Knights()

#passing the obj
move_test(bishop)
move_test(knight)

