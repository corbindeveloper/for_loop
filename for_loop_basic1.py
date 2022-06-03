# BASIC
x = 0
for x in range(0,151):
   print(x)


# MULTIPLES OF FIVE
n = 5
for n in range(5,1001,5):
   print(n)


# COUNTING THE DOJO WAY
y = 1
for y in range(1, 101):
   if (y % 10 == 0):
      print("Coding Dojo")
   elif ( y % 5 == 0):
      print("Coding")
   else:
      print(y)


# WHOA HUGE
i = 0
z = i
for i in range(1, 500000, 2):
   z = z + i
print(z)


# COUNTDOWN BY FOURS
v = 0
for v in range(2018, 0, -4):
   if (v % 2 == 0):
      print(v)


# FLEXIBLE COUNTER
lowNum = 2
highNum = 9
mult = 3

for lowNum in range(lowNum, highNum + 1, 1):
   if(lowNum % mult == 0):
      print(lowNum)