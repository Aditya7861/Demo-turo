# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

user1 = input("Enter Your Name:-")
user2 = input("Enter Your Name:-")
user1_input = input("Enter your choice:-");
user2_input = input("Enter your choice:-");

def game_controler():
    if(user1_input == "Rock" and user2_input == "scissors"):
        return "{} wins".format(user1)
    elif(user1_input == "scissor" and user2_input == "paper"):
        return "{} wins".format(user1)
    elif (user1_input == "paper" and user2_input == "rock"):
        return "{} wins".format(user1)
    elif(user1_input == "scissors" and user2_input =="rock"):
        return "{} loose".format(user1)
    elif (user1_input == "paper" and user2_input == "scissors"):
        return "{} loose".format(user1)
    elif (user1_input == "rock" and user2_input == "paper"):
        return "{} loose".format(user1)
    else:
        return "Try again"
print(game_controler())
