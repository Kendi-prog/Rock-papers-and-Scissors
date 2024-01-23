import random

def play_time():
    user = input("What is your choice? 'r' is for rock, 'p' is for paper, and 's' is for scissors:")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie😂."
    
    if winner(user, computer):
        return "You won🎉🎉!!"
    
    return "You Lost😪!!"

def winner(player, opponent):
    #r>s, s>p, p>r
    if (player == 'r' and opponent == 's' ) or (player == 's' and opponent == 'p') \
     or (player == 'p' and opponent == 'r') :
        return True
    

print(play_time())