"""
x=-2;
if x>0:
    print("hello");
      print("world");
    print("I am shivani");
print("end");
"""


#enter a number and check given number is positive or negative
"""
x= int(input("enter a number"));
if x>=0 :
    print("number is positive");
if (x<0):
    print("number is not positive");
"""

#enter given number even or odd using single line else if
"""
x = int(input("enter a number"))
print("even") if x%2 == 0 else print("odd");
"""


x = int(input("enter a number"));
i=2;
while i<=x//2 and x%i != 0 :
    i += 1;
if(i>x//2) :
    print("number is prime");
else:
    print("number is not prime" , i);
    
