#Binary search

name = input("What is your name?\n")
print("Nice to meet you,", name,"!")
print("The program guesses a number from 0 to N")
n = int(input("Enter the N:  \n"))
what = 0
low = 0
high = n
while low <= high:
    mid = (low + high) // 2
    print(mid)
    what = input("more, less, equals? \n")
    if what == "more":
        low = mid
        mid = (low + high) // 2
    elif what == "less":
        high = mid
        mid = high // 2
    elif what == "equals":
        print("Success", mid)
        break
