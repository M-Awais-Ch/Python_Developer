#List comprehentions

a=[2,12,2,15,2,6,756,42,33,6]
c=[23,4,2,44,334,53,4]
b=[i**3 for i in a]
print(b)

print([x for x in a if x%2==0])


# Dictionary comprehentions

a=[2,12,2,15,2,6,756,42,33,6,5678,32,2]
c=[23,4,2,44,334,53,4,'w',4,65,7]
print({x:x**2 for x in a })
print({x:x**2 for x in a if x%3==0 })
print({x:y for (x,y) in zip(a,c)})

