from operator import truediv

fname="John"
course="html"
print("my name is",fname,"I am learning",course)
#string formating f formating
print(f"my name is {fname} and I am learning {course}")
#Operators(symbol that performs functions)
#arithmetic operators
a=20
b=30
sum=a+b
print(f"the sum of {a} and {b} is {sum}")
sub=-10
print(f"the subtraction between {a} and {b} is equals to {sub} ")
#multiplication = *
#division= /
prod=a*b
print(f"the product of {a} and {b} equals to {prod}")
div=a/b
print(f"the division of {a} and {b} equals to {div}")
#modulus (the remainder after division)
mod=b%a
print(f"modulus of {b} and {a} is {mod}")
#Exponential **
print(f"power {a**b}")
#comparison operators(compare 2 values and determine whether true or false
#eg == < > >= <=
x=100
y=50
print(f"is {x}={y}? {x==y}")
print(f"is {x}<{y}?{x<y}")
print(f"is {y}>={x}? {y>=x}")
print(f"is {x}> {y}? {x>y}")
#
c=5
print(c>3 and c<10)
print(c<3 and c<10)
d=True
print(d)
print(not (b))