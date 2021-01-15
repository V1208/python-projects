x=int(input("Enter the number"))
if((x%2)==0):
    minimum=x   
y=1
while(y<10):
    x=int(input("Enter the number"))
    if((x%2)!=1):
        minimum=x
        if(minimum>x):
            minimum=x
    y=y+1
print(minimum)
 
