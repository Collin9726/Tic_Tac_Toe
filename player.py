class Player:
    # moves_made_list=[]
    moves_av_list=[1,2,3,4,5,6,7,8,9]
    
    def show_av_moves(self):
        print(self.moves_av_list)   

    def move_made(self, move):
        Player.moves_av_list.remove(move)
        # Player.moves_made_list.append(move)  

    def validate_move(self, move):
        if move in Player.moves_av_list:
            return True
        else:
            return False        

# obj1=Player()
# obj1.show_av_moves()
# obj1.move_made(5)
# obj1.show_av_moves()
# print(obj1.moves_made_list)
# print(obj1.validate_move(4))