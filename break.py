#break (if during the exexution of the loop python interpreter encounters break, it immediately stops the loop execution and exits out of it)


candies =10
for i in range(candies):
    print("give candies to friends")
    if  candies-i==5:
     print("only 5 candies left, stopping distribution")
    break