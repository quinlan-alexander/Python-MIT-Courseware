#Homework 1 Exercise 1.9
#Checking legal Python variable names

#and = "and"
#print and

_and = "_and"
print _and

var = "var"
print var

var1 = "var1"
print var1

#1var = "1var"
#print 1var

#my-name = "my-name"
#print my-name

your_name = "your_name"
print your_name

COLOR = "COLOR"
print COLOR

#Homework 1 Exercise 1.10
#Checking the type of the values stored in each of the variables

a = False
print type(a)

b = 3.7
print type(b)

c = 'Alex'
print type(c)

d = 7
print type(d)

e = 'True'
print type(e)

f = 17
print type(f)

g = '17'
print type(g)

h = True
print type(h)

i = '3.14159'
print type(i)

#Homework 1 Exercise 1.12
#Checking Boolean Operations

a = False
b = True
c = False

print b and c
print b or c
print not a and b
print (a and b) or not c
print not b and not (a or c)

#Homework 1 Exercise 1.13
#Checking Conditionals

print "location is Massachusetts and pay = 50000"
location = "Massachusetts"
pay = 50000

if location == "U.S.S. Enterprise":
    print "So long, suckers!  I'll take it!"
elif location == "Massachusetts":
    if pay < 100000:
        print "No way"
    else:
        print "I'll take it!"
elif location == "California" and pay > 40000:
    print "I'll take it!"
elif pay > 60000:
    print "I'll take it!"
else:
    print "No thanks, I can find something better."

print "location is Iowa and pay = 50000"
location = "Iowa"
pay = 50000

if location == "U.S.S. Enterprise":
    print "So long, suckers!  I'll take it!"
elif location == "Massachusetts":
    if pay < 100000:
        print "No way"
    else:
        print "I'll take it!"
elif location == "California" and pay > 40000:
    print "I'll take it!"
elif pay > 60000:
    print "I'll take it!"
else:
    print "No thanks, I can find something better."

print "location is California and pay = 50000"
location = "California"
pay = 50000

if location == "U.S.S. Enterprise":
    print "So long, suckers!  I'll take it!"
elif location == "Massachusetts":
    if pay < 100000:
        print "No way"
    else:
        print "I'll take it!"
elif location == "California" and pay > 40000:
    print "I'll take it!"
elif pay > 60000:
    print "I'll take it!"
else:
    print "No thanks, I can find something better."

print "location is U.S.S. Enterprise and pay = 1"
location = "U.S.S. Enterprise"
pay = 1

if location == "U.S.S. Enterprise":
    print "So long, suckers!  I'll take it!"
elif location == "Massachusetts":
    if pay < 100000:
        print "No way"
    else:
        print "I'll take it!"
elif location == "California" and pay > 40000:
    print "I'll take it!"
elif pay > 60000:
    print "I'll take it!"
else:
    print "No thanks, I can find something better."

print "location is California and pay = 25000"
location = "California"
pay = 25000

if location == "U.S.S. Enterprise":
    print "So long, suckers!  I'll take it!"
elif location == "Massachusetts":
    if pay < 100000:
        print "No way"
    else:
        print "I'll take it!"
elif location == "California" and pay > 40000:
    print "I'll take it!"
elif pay > 60000:
    print "I'll take it!"
else:
    print "No thanks, I can find something better."

#Homework 1 Exercise 1.14
#Understanding loops

#1
num = 10
while num > 3:
    print num
    num = num - 1

#2
divisor = 2
for i in range (0, 10, 2):
    print i / divisor

#3
num = 10
while True:
    if num < 7:
        break
    print num
    num -= 1

#4
count = 0
for letter in 'Snow!':
    print 'Letter #', count, 'is', letter
    count += 1
