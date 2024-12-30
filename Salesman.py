t = int(input())
for i in range(t):
    x = int(input())
    if x <= 100:
        print(x)
    elif 100 < x <= 1000:
        print(x - 25)
    elif 1000 < x <= 5000:
        print(x - 100)
    else:
        print(x - 500)

T = int(input())
for tc in range(T):
    n, x = map(int, input().split(' '))
    pizza = n * x // 4
    if n * x % 4 == 0:
        print(pizza)
    else:
        print(pizza + 1)
        

for i in range(int(input())):
    x,y=map(int,input().split())
    if y/x*100>=50:
        print ("YES")
    else:
        print("NO")
        
        
k=int(input())
for i in range(k):
    a=list(map(int,input().split()))
    if a[0]*a[1]<=a[2]*a[3]:
        print("Yes")
    else:
        print("No")
        


for _ in range(int(input())):
    n = int(input())
    print(15*n)


t=int(input())
for i in range(t):
    n=input()
    n=int(n)
    print(n*10)
    
    
import math
hlo=int(input())
for love in range(hlo):
    lv1,lv2=map(int,input().split())
    if lv1/lv2<1:
        print("0")
    else:
        print(math.ceil((lv1-lv2)/4))
        

n=int(input())
for i in range(n):
    c=list(map(int,input().split()))
    if c[0]>c[1]:
        print("CAR")
    elif c[1]>c[0]:
        print("BIKE")
    else:
        print("SAME")
        
for i in range(int(input())):
    a,b = map(int, input().split(" "))
    c,d = map(int, input().split(" "))
    if(c>=a and d>=b):
        print("Possible")
    else:
        print("Impossible")
        
        
a,b,c,x= map(int,input().split())
if a == x:
    print('yes')
elif b == x:
    print('yes')
elif c == x:
    print('yes')
else:
    print('no')

