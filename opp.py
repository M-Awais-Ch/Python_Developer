#inheritence
# class student:
#     def stu(self):
#         roll=int(11)
#         name=str("Awais")
#         print(roll,"\n",name)
# class teacher(student):
#     def teach(self):
#         id=int(1)
#         name=str("Muhammad Idrees")
#         print(id,"\n",name)
# #b=student
# a=teacher()
# print(a.stu())


#Abstruction
#
# from abc import ABC,abstractmethod
# class tech(ABC):
#     @abstractmethod
#     def data(self):
#         pass
#     @abstractmethod
#     def intro(self):
#         pass
# class school(tech):
#     def data(self):
#         return "Muhammad Awais"
#     def intro(self):
#         return 1
# a=school()
# print(a.intro())
# print(a.data())


#polymorphism

class school:
    def data(self):
        print("show school Data")
class teacher:
    def data(self):
        print('show teacher Data')
class student:
    def data(self):
        print("show student Data")
def detail(dat):
    print('show the details of :',dat.data())
a=teacher()
b=student()
c=school()
detail(b)


#Encapsulation

class school:
    def __init__(self,name,id,depar):
        self.department=depar
        self.__name=name
        self.__id=id
    def name_det(self,new_name):
        if self.__name==new_name:
            print(True)
        else:
            print("wrong name")
    def id_det(self,new_id):
        if new_id>self.__id:
            print("True Id")
        else:
            print("Id is wrong")
a=school('Muhammad Awais',1,"CS")
print(a.department)
print(a)
print(a.id_det(7))
print(a.id_det(0))
print(a.name_det('Muhammad Idrees'))
print(a.name_det('Muhammad Awais'))





