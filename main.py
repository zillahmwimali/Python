a={6,7,8,9,10}
b={5,6,7,8,9}
a.add(4)
print(a)
b.add(3)
print(b)
c=a.union(b)
print(c)
a.difference(b)
print(a)
b.difference(a)
print(b)
d=a.intersection(b)
print (d)

lst=[11,100,99,1000,999,99]
lst.insert(0,-1)
print(lst)
print(lst[1])
print(len(lst))
print(lst[6])
print(lst.count(99))
sum=0
for n in lst:
 sum+=n
 print(sum)

 for p in range(2020,2070):
  if p%4==0:
   print(p)
for x in range(1000,2000):
 if x%7==0:
   print(x)

 for d in range(30,50):
   if d%2!=0:
    print(d)

x=[]
for y in range(100,200):
 if y%7==0:
  x.append(y)
print(x)
for m in range(1,50):
 if m%5==0 and m%3==0:
  print("PurpleWhite")








