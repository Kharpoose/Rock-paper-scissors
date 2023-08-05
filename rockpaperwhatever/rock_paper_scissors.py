import random



def play():
    user = input("What is your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n").upper()
    computer = random.choice(['R', 'P', 'S'])
    print(f"Here my attack {computer}")
    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'


def is_win (player, opponent):

    if(player == 'R' and opponent == 'S') or (player == 'P' and opponent == 'R') \
          or (player == 'S' and opponent == 'P'):
        return True
    

print(play())    