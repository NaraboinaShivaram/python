t=4,5,6
print(t)
t+=1,2,3
print(t)
print(len(t))
print(3 in t)
print(t[3])
print(t.count(3))
m=t.index(4)
print(m)

d={1:'one',2:'two',3:'four'}
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d.get(2))
d1={3:'three'}
d.update(d1)
print(d)
print(3 in d)
m=len(d)
print (m)
m=d.pop(1)
print(m)
del (d[2])
print(d)


l=[3,5,4,5,'list']
print(l)
l.insert(0,[1,2])
print(l)
l.append(2)
print(l)
l.remove(5)
print(l)
m=len(l)
print(m)
m=l.pop(1)
print(m)
print(l)
del (l[2])
print(l)
l1=[1,2,3,4]
l.extend(l1)
print(l)
