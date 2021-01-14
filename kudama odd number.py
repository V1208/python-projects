x=int(input("Enter the number"))
minimum=x
y=1
while(y<10):
    x=int(input("Enter the number"))
    if(minimum>x):
        minimum=x
    y=y+1
print(minimum)
