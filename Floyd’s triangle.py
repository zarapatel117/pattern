rows=int(input("enter the number of rows you want:"))
num = 1
print("floyds triangle")

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end="")
        num= num+1
    print()    
