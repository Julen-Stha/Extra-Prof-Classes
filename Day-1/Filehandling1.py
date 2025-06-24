f = open("data.txt","r")
content = f.read()
print(content)
f.close()

f = open("data.txt","a")
f.write("hello, world")
f.close()


#content manager "with" automatically closes the file, cleaner and safer sytax
with open("data.txt","r") as f:
    for line in f:
        print(line.strip()) #removes whitespaces