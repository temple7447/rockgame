import random

draw = "it’s a tie and the winner is computer"



computer = ["R","P","S"]
player = input("Enter any of this option R,P,S: ")

computeraction = random.choice(computer)
print(computeraction)

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
    
    