r,c=map(int,input().split())
e=0
o=0
for i in range(r):
   d=list(map(int,input().split()))
   if i%2==0:
       e+=sum(d)
   else:
       o+=sum(d)
print(e,o)