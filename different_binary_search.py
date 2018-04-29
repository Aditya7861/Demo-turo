def binary_search(lisst,item):
    flag = True
    while flag:
        if(lisst[len(lisst)//2]==item):
            print("item found")
            flag = False
        if(lisst[len(lisst)//2]<item):
            lisst = lisst[len(lisst)//2:]
        if(lisst[len(lisst)//2]>item):
            lisst = lisst[:len(lisst)//2]
        if(len(lisst)==1 and lisst[0]!=item):
            flag = False
            print("item Not FOund")
if __name__ == "__main__":
    binary_search([1,3,5,7,9,12,17,23,30,40,45,47,50,51,54,58,67,89,78,87,98],67)

