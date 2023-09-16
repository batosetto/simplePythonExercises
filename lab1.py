
x = 4
y = 2
print(x+y)

car_name = "Mercedes"
num_wheels = 4

print("I wish I had " + car_name + " and it would have " + str(num_wheels) + " wheels.")

name = "Barbara Tosetto"

num_apples = 24
num_friends = 7
print("My name is " + name + " and I have " + str(num_apples) + " apples. \nI have " + str(num_friends) + " friends and I'll share my apples with them.")
print(f"The total apple per friend is: {num_apples/num_friends :0.2f}")

billTotal = 120
num_people = num_friends
print("\nTotal number of people: " + str(num_people) + f"\nTotal bill: {billTotal :.2f} " + f"\nTotal bill per person is: {billTotal/num_people :.2f}")
print(f"""\nTotal number of people: {int(num_people):.2f} 
Total bill: {int(billTotal):.2f} 
Cost per person: {int(billTotal/num_people):.2f}""")

dessert_cost = 6.55
total_desert_cost = dessert_cost * num_people
print(f""" \nTotal number of people: {int(num_people):.2f} 
Dessert cost: {int(dessert_cost):.2f} 
Total cost of desserts:: {int(total_desert_cost):.2f}""")





