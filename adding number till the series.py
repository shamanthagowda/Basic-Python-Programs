num=int(input('enter the number'))
n=0
for i in range(1, num+1):
    for j in range(0,i+1):
        n+=j
print(n)        
