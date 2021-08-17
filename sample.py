# Starting with traditional Hello World! greet.
print("Hello world!")

#Simple add method
def add(number1,number2):
    return number1 + number2

#test input numbers
num1 = 5
num2 = 8

print(F'Add {num1} and {num2}')
print(F'{num1} + {num2} = {add(num1,num2)}')

person1 = {"name": "Pradeep", "age": 36, "gender":"male"}

class Person:
    def __init__(this,name,age,gender):
        this.name = name
        this.age = age
        this.gender = gender
    def display(this):
        print(F'Name :- {this.name}\nAge :- {this.age}\nGender :- {this.gender}\n')

people = [Person("Pradeep", 36,"male"),Person("Sushma", 34,"female"),Person("Tanuj", 6,"male"),Person("Tanay", 6,"male")]

#print(people)
#print(person1)

print(F'Person details \n')
for person in people:
    person.display()
    
#for i in range(0,10,2):
#    print(i)

print(type(num1))
print(type("num1"))
print(type(True))