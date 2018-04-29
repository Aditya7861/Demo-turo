import random
def cow_and_bull():
    flag = True;
    cow = 0
    bull = 0
    print("Wellcome to cow and Bull game")
    rand_no = str(random.randint(999,9999))
    print(rand_no)
    while flag:
        numb = input("Enter Number")
        for i in range(4):
            if numb[i] in rand_no:
                if(numb[i]==rand_no[i]):
                    cow =cow +1
                else:
                    bull = bull +1
                    print(bull)
            if numb == rand_no:
                flag = False
        print("{} cow , {} bull".format(cow,bull))



##solution of this problem
##https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html



if __name__ =="__main__":
    cow_and_bull()
