# n=5

# for i in range(n):
#     if i==0 or i==n-1:
#         for j in range(n):
#             print("*",end=" ")
#         print()
#     else:
#         for j in range(n-1-i):
#             print(" ", end=" ")
#         print("*")


# class Animal:
#     def eat(self):
#         print("eating")

# class Dog(Animal):
#     def bark(self):                         #single inheritance
#         print("barking")

# d=Dog()
# d.eat()
# d.bark()


# class camera:
#     def photo(self):
#         print("taking photo")
# class phone:
#     def call(self):                           #multiple inheritance-multiple parent-one child
#         print("calling")
# class smartphone(camera,phone):
#     pass
# s=smartphone()
# s.photo()
# s.call()


# class person:
#     def speak(self):
#         print("speaking")

# class student(person):
#     def study(self):
#         print("studying")                       #multi level inheritance-parent-child-grandchild

# class collegestudent(student):
#     pass

# c=collegestudent()
# c.speak()
# c.study()


# class animal:
#     def eat(self):
#         print("eating")
# class dog(animal):                     #hierarchy inheritance-one patent-multi child
#     pass
# class cat(animal):
#     pass
# d=dog()
# c=cat()

# d.eat()
# c.eat()


# class person:
#     def work(self):
#         print("working")
# class student(person):
#     def study(self):
#         print("studying")                   #hybrid inheritance-use of more than 1 type of inheritance
# class employee(person):
#     def earn(self):
#         print("earning")
# class intern(student,employee):
#     pass

# i=intern()
# i.work()
# i.study()
# i.earn()

# from abc import ABC, abstractmethod
# class car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class BMW(car):
#     def start(self):
#         print("car started")

# c=BMW()
# c.start()


# print("****** \n"
# "    *\n" \
# "")


# class bank:
#     def __init__(self):
#         self.balance=1000

# account=bank()
# account.balance=-5000
# print(account.balance)

# class bank:
#     def __init__(self):
#         self.__balance=1000
#     def set_balance(self,amount):
#         if amount>=0:
#             self.__balance=amount

#     def get_balance(self):
#         return self.__balance

# account=bank()
# account.set_balance(-5000)
# print(account.get_balance())



# class bank:
#     def __init__(self):
#         self.__balance=1000

#     @property
#     def balance(self):
#         return self.__balance

#     @balance.setter
#     def balance(self,amount):
#         if amount>=0:
#             self.__balance=amount
#         else:
#             property("invalid balance. balance can't be negative")

# account=bank()
# print("initial balance : ",account.balance)

# account.balance=5000
# print("updated balance : ", account.balance)

# account.balance=2000
# print("final balance : ",account.balance)
        

# for i in range(1,6):
#     a=i
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a=a+1
#     print()


# l=[]
# num_list=int(input("how many numbers you want to add to the list ? "))
# for i in range(num_list):
#     number=int(input(f"enter your {i+1} number : "))
#     l.append(number)

# print(l)



             

