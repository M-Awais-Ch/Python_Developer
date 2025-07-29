a=[3331,45,8,56,4,3,7]
for index, value in enumerate(a,start=1):
    print(index,value)


print(list(map(lambda x:x*2,a)))

print(list(filter(lambda x:x%2==0,a)))


from functools import reduce
print(reduce(lambda x,y:x+y,a))
print("hi")
print("hello")
