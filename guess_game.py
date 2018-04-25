import random
original_num = random.randint(2,89)
print(original_num)
def guess_checker(count):
    user_guess = int(input("Enter your guess no:-"))
    if(user_guess < original_num):
        print("Your guess Number is low")
        count = count +1
        guess_checker(count)
    elif(user_guess > original_num):
        print("your guess Number is High")
        count = count +1
        guess_checker(count)
    elif(user_guess == original_num):
        print("You Guessed Corect number")
        print("Yout took these  turn {} to correct guess".format(count))
        exit
guess_checker(count =0)
