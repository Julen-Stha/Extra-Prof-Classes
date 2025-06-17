word = "python"
revelword = ["_"]* len(word)
print(" ".join(revelword))

limit = 5
print(f'Attempts={limit}')
while limit>0:
    data = input("Enter guess:")
    if data in word:
        print("Correct guess")
        for i in range(len(word)):
            if word[i] == data:
                revelword[i] = data
                answer= "".join(revelword)
        print(answer)
       
        if word==answer:
            print("You have guessed the word")
            break

    else:
        limit-=1
        if limit !=0:    
            print("Wrong guess")
            print(f'Attempt left={limit}')
        else:
            print("Better luck next time")