value = int(input(""))

for i in range(1,value+1):
    for j in range(1,i+1):
        print("*"*j,end=" ")
    print(end="\n")
