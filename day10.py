# Simple Inheritance
class Animal:
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")

class Dog(Animal):
    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof Woof")

# dog1 = Dog()
# dog1.whoAmI()
# dog1.bark()

# a1 = Animal()
# a1.whoAmI()

# Multi Level Inheritance
class Vehicle:
    def details(self):
        print("Vehicle")

class Car(Vehicle):
    def details(self):
        print("Car")

class BMW(Car):
    def details(self):
        print("BMW")

# Multiple Inheritance
class A:
    def method1(self):
        print("A")

class B:
    def method1(self):
        print("B")

class C:
    def method3(self):
        print("C")

class D(A, B, C):
    # def method1(self):
    #     print("D")

    def method4(self):
        print("Class D")

x1 = D()
# x1.method1()
# x1.method3()

x2 = A()

# Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
    
class Dog(Animal):
    def bark(self):
        print("Dog Barking")

class Cat(Animal):
    def meow(self):
        print("Cat Meowing")

dog1 = Dog()
# dog1.bark()
# dog1.speak()

cat1 = Cat()
# cat1.meow()
# cat1.speak()

# Hybrid Inheritance
class A:
    def method1(self):
        print("A")

class B(A):
    def method2(self):
        print("B")
    
class C(B):
    def method3(self):
        print("C")
    
class D(B):
    def method4(self):
        print("D")

# Polymorphism
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sayhello(self):
        print("Hello everyone")

class Smith(Person):
    def sayhello(self):
        print(f"Hello, my name is {self.name}, and my age is {self.age}")

s1 = Smith("Smith", 20)
p1 = Person("Smith", 20)
# p1.sayhello()
# s1.sayhello()


#Encapsulation
class Student:
    def __init__(self, name):
        self.name = name #Public

    def display(self):
        print(self.name)
	
s1 = Student("Allen")
# print(s1.name)
# s1.display()

class Student1:
    def __init__(self, name):
        self._name = name #Protected

    def display(self):
        print(self._name)

s2 = Student1("Allen")
# print(s2._name)
# s2.display()

class Student3:
    def __init__(self, name):
        self.__name = name #Private

    def display(self):
        print(self.__name)

s3 = Student3("Allen")
# print(s3.__name)
# s3.display()

# Error
#Syntax Error
# for i range(10):
#     print(i)

# Runtime Error
def division(a,b):
    print(a/b)

# division(10,2)
# division(10,0)

#Logical Error
# def addition(a,b):
#     print( a - b)

# addition(10,40)

# Indentation Error
    # if True:
    # print("True")

# Exception Handling
# try:
#     statement
# except:
#     statement
# finally:
#     statement

try: 
    division(10,2)
except:
    print("Division by 0 is not possible")
finally:
    print("Finally Block")