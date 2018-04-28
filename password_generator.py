import random
# password Generator
type = input("Enter the type of password ")


Abc = ["A","B","C","D","E","F","G","H"]
abc = ["a",'b',"c","d","e","f","g","h"]
oneTwo = ["1","2","3","4","5","6","7","8","9","0"]
special_sym = ["!","@","#","$","^","&","*"]

def create_pass(type):
    if type=="weak":
        weak_pass()
    if type=="strong":
        strong_pass()

def weak_pass():
    word = " "
    for i in range(len(Abc)//2):
        word += Abc[random.randint(0,len(Abc)-1)]
        word += abc[random.randint(0,len(abc)-1)]
    
    print(word)

def strong_pass():
    passd = " "
    for i in range(0,2):
        passd += Abc[random.randint(0,len(Abc)-1)]
        passd += abc[random.randint(0,len(Abc)-1)]
        passd += oneTwo[random.randint(0,len(Abc)-1)]
        passd += special_sym[random.randint(0,len(Abc)-1)]
    print(passd)

create_pass(type)
