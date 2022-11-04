a=18

guess_count=0

while guess_count<4:
    guess_count+=1
    n=int(input("guess the number\n"))
    if a<n:
        print("enter a smaller number\n")
    elif a>n:
        print("enter a greater number\n")
    else:
        print("congrats! you guessed the number\n")
        break
print("you lose")
print("the number was"+ a)
   

