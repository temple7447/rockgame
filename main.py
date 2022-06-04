import random

def game():
      
    if player == computeraction:
        print(draw)
        
    elif (player == "R" and computeraction == "S"):
        print('Rock beats Scissors and the winner is player')
        
    elif (player == "P" and computeraction == "R"):
        print('Paper beats Rock and the winner is player')
        
    elif (player == "S" and computeraction == "P"):
        print('Scissors beats Paper and the winner is player')
        
    elif (player == "S" and computeraction == "R"):
        print('Rock beats Scissors and the winner is computer')
        
    elif (player == "R" and computeraction == "P"):
        print('Paper beats Rock and the winner is computer')
        
    elif (player == "P" and computeraction == "S"):
        print('Scissors beats Paper and the winner is computer')
    else:
        print('you value you enter is not correct')



while True:
    draw = "it’s a tie and the winner is computer"



    computer = ["R","P","S"]
    player = input("Enter any of this option R,P,S: ")

    computeraction = random.choice(computer)
    print(computeraction)
      
    game()
    
    player_again = input ('play again? (y/n):  ')
    if player_again.lower() != 'y':
        break
    
    