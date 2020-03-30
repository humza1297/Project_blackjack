import random
class game:
    # here b= bricks , d= diamond , s= spade, h= hearts
    def __init__(self):
        self.cards = {'b_two': 2, 'b_three': 3, 'b_four': 4, 'b_five': 5, 'b_six': 6, 'b_seven': 7, 'b_eight': 8, 'b_nine': 9,
            'b_ten': 10, 'b_joker': 10, 'b_queen': 10, 'b_king': 10, 'b_ace': 1 or 11
        , 's_two': 2, 's_three': 3, 's_four': 4, 's_five': 5, 's_six': 6, 's_seven': 7, 's_eight': 8, 's_nine': 9,
            's_ten': 10, 's_joker': 10, 's_queen': 10, 's_king': 10, 's_ace': 1 or 11,
            'd_two': 2, 'd_three': 3, 'd_four': 4, 'd_five': 5, 'd_six': 6, 'd_seven': 7, 'd_eight': 8, 'd_nine': 9,
            'd_ten': 10, 'd_joker': 10, 'd_queen': 10, 'd_king': 10, 'd_ace': 1 or 11,
            'h_two': 2, 'h_three': 3, 'h_four': 4, 'h_five': 5, 'h_six': 6, 'h_seven': 7, 'h_eight': 8, 'h_nine': 9,
            'h_ten': 10, 'h_joker': 10, 'h_queen': 10, 'h_king': 10, 'h_ace': 1 or 11, }
        self.val= 21
        self.player_card=[]
        self.player_val=0
    def chck_win(self):
        if self.player_val == 21:
            return True

    def player(self):

        i=0
        while i!=len(self.player_card):
            self.player_card.append(random.choice(list(self.cards.keys())))
            self.player_val=self.player_val + self.cards[self.player_card[i]]
            i+=1
        if self.player_val==self.val:
            print("You have won.")
        else:
            val=input("Do you want to hit or stay: ").lower()
            if val=="hit":
                self.player_card.append(random.choice(list(self.cards.keys())))
                chck_win()
            else:


    def dealer(self):

