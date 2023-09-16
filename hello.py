import art

art.tprint("Hello \nWorld!")

print("Hey! I'm Python. \nNice to meet you!")
print("I'm going to calculate some numbers for you.")
print("Barbara's age is \t", 42)
print('Barbara\'s age is', 42)

print("3 eggs cost" + str(10))
print("10")
cost = 12
print("3 eggs cost", cost)
print("3 eggs cost " + str(cost))
price = "3"
print("3 eggs cost " + price)
print("3 eggs cost " , int(price)*3)
print("3 eggs cost " + str(int(price)*3))
print("Multiplying strings: \n" * 3) #string will be printed 3x
print("1" + "2" *9) 
print("1" + "0" * 9)

x =5
print(type(x))
print(x)

x = "hello"
print(x)

y=10

y = y + 5

print(y)

abc123= 123

print(abc123)

abc123=None
print(abc123)

del abc123
#print(abc123) will delete the variable

multi = """This is a multi-line string.
This is the second line.
This is the third line. \n""" #triple quotes allow multi-line strings
print(multi)

print("This is a multi-line string.\nThis is the second line.\nThis is the third line.\n")

print(f"my results are {(0.1+0.2) :0.2f}")

name = "Barbara"
age = 33
print(name)
print(age)

print("Simple math operations:")
print(3+4)
print(2 *(3+4))
print(5/2)
print(6/2)
#Double slash division returns rounded integer
print(5//2) #we'll only see the quotient
print(5%2)
print(-5*3)
print(3/4)
print(0.1 + 0.2)
print(0.1 + 0.3)
print(0.2 + 0.2)
print(0.2 + 0.1)