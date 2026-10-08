import random
def play():
    try:
        user = input("choose:'r' for rock,'p' for paper ,'s' for scissior >>> ").strip().lower()
        if user not in ['r','p','s']:
            raise ValueError(f'{user} is not a valid choice!')
        computer = random.choice(['r','p','s'])
        print(f"compouter chose '{computer}'")

        if user==computer:
             return 'Its a tie!'
        elif is_win(user,computer):
             return 'You won!'
        else:
             return 'You lost!'
    except ValueError as e:
        print(f"Error: {e} Please enter 'r', 'p', or 's'.")

def is_win(player , opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
        return True
    return False
print(play())
