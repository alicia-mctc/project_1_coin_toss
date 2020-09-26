"""
What is the chances of tossing a coin and 
having the coin lands on its heads or tails?

"""
import random # get random from library

def checktoss():
    
    n = int(input("Number of times to toss coin?  "))# Ask user how many times to toss a coin
    print("I want to toss the coin :  ", n)
    
    result_list = []  # create empty list to hold coin's results
    heads = 'H'
    tails = 'T'

    for k in range(n):
        toss = random.randint(1,2)
        if (toss == 1):
            print ("Heads", k)
            result_list.append(heads)

        else:
            print("Tails", k)
            result_list.append(tails)

    print(result_list)  # str not needed
    print(str(result_list.count(heads)) + " heads and " + str(result_list.count(tails)) + " tails ")

checktoss()           
    
    

    
