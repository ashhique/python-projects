#FunctionSample1
def hey():
    print("Hello World")
hey()
print("-------------------------------")
#Print name & age using function

def name(name):
    print("Your name is "+name)

def age(age):
    print("You're " + str(age) + " year old")

name("Ashik")
age(19)
print("-------------------------------")
#name & job using tuple

def name(*values):
    print("Name:"+values[0]+"Job:"+values[1])
name("Ashik \n","Web designer")
print("----------------------------------")

#global variable & Local variable

num=10  #global variable
def loco():
    num=5 #local variable
    num=num+1
    print(num)

print(num)
loco()
print("----------------------------------")

#keyword argument

def keke(state,city,country="india"): #country as default value
    print(state,city,country)

keke(city="Pathanamthitta,",state="Kerala,", country="USA") #position doesn't matter
#country is  changeable from here
print("----------------------------------")

#Return value

def add(num1,num2):
    sum=num1+num2
    return sum
result=add(10,10)
print(result)
print("----------------------------------")

#dictionary Sample

data={"name":"Ashik mon","age":19,"place":"Pathanamthitta","job":"Python developer"}
print(data)
print(data.get("job"))

print("----------------------------------")



