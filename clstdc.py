# #Coustamze List
# class mylist:
#     def __init__(self):
#         self.val = []
#
#     def add(self, item):
#         self.val.append(item)
#     def get(self,index):
#         return self.val[index]
#     def __repr__(self):
#         return str(self.val)
# a=mylist()
# print(a)
# a.add(3)
# a.add(43)
# a.add(54)
# print(a)
# print(a.get(2))

#Coustamize Dict
class mydict:
    def __init__(self):
        self.item={}
    def add(self,key,value):
        self.item[key]=value
    def get(self,key):
        return self.item.get(key)
    def __repr__(self):
        return str(self.item)
a=mydict()
print(a)
a.add("roll",65)
a.add(1,"Awais")
print(a)
print(a.get(1))