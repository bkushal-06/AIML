## 1. Print Statement
print ("hello world")


## 2. Loops
# Using a for loop to print numbers 1 to 5
for i in range(1, 6):
    print(f"Number: {i}")
# Using a while loop to print numbers 1 to 5
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1


## 3. Conditional Statements
# Check if a number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

## 4. Tuples
thistuple = "brand"
print(thistuple)
x="python "
y="is "
z="awesome "
print (x+y+z)
thisdict ={"brand":"ford","model":"mustang","year":1964}
print(thisdict)
for i  in range (10,2):
 print(i)
 
## 5. Dictionary
# Creating a dictionary with student names and their scores
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Accessing dictionary elements
for student, score in students.items():
    print(f"{student} scored {score} marks")
