#string is a data type used to represent text
from pexpect.replwrap import python

from basics import fname

greeting="hello world"
course=('python')
print(greeting)
print(course)
#string methods
#upper
print(greeting.upper())
print(greeting.lower())
print(greeting.title())
#len
print(len(course))
print(len(greeting))
print(len("mark"))
fname="Mary"
lname="Jane"
print(fname+" "+lname)
#escape characters
print("hello good morning,\how are you")
print("name\course")
print('hello')
print('mary said "hi" to you')
print("we are learning \"python\"")
print("she said\"hello\"")
print(""" this is an example of a multiline string""")
text="python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
message="hello"
print(message[0])
print(message[1])
print(message[2])
mytext="fullstack"
print(mytext[0:4])
print(mytext[4:9])
#replace
sentence="I love html"
print(sentence.replace("html","python"))