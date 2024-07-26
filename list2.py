l1 = [1,2,3,4,5]
l1.append(8);
print(l1)

#[1, 2, 3, 4, 5, 8]
print(l1.append(10));
#None
l2=3;
l2.append(4)
"""
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l2.append(4)
AttributeError: 'int' object has no attribute 'append'
"""
l2 = [1,2,3];
l1.append(l2);
l1
"""[1, 2, 3, 4, 5, 8, 10, [1, 2, 3]]
[1, 2, 3, 4, 5, 8, 10, [1, 2, 3]]
[1, 2, 3, 4, 5, 8, 10, [1, 2, 3]]
"""
l1.append("shivani");
l1
#[1, 2, 3, 4, 5, 8, 10, [1, 2, 3], 'shivani']
l1.insert(9,10);
l1
#[1, 2, 3, 4, 5, 8, 10, [1, 2, 3], 'shivani', 10]
l1.insert(-1,12)
l1
#[1, 2, 3, 4, 5, 8, 10, [1, 2, 3], 'shivani', 12, 10]
l1.remove()
"""
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l1.remove()
TypeError: list.remove() takes exactly one argument (0 given)
"""
l1.remove(2);
l2
#[1, 2, 3]
l1
"""[1, 3, 4, 5, 8, 10, [1, 2, 3], 'shivani', 12, 10]"""
l1.append(2)
l1.inserr(2)
"""
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l1.inserr(2)
AttributeError: 'list' object has no attribute 'inserr'. Did you mean: 'insert'?
"""
l1.insert(2);
"""
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l1.insert(2);
TypeError: insert expected 2 arguments, got 1
"""
l1.insert(2,2);
l1
#[1, 3, 2, 4, 5, 8, 10, [1, 2, 3], 'shivani', 12, 10, 2]
l1.remove(2);
l1
#[1, 3, 4, 5, 8, 10, [1, 2, 3], 'shivani', 12, 10, 2]












l1.remove(9);
"""
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    l1.remove(9);
ValueError: list.remove(x): x not in list
"""
l1.remove(l2);
l1
#[1, 3, 4, 5, 8, 10, 'shivani', 12, 10, 2]
print(l1.remove('shivani'))
#None
l1.pop();
#2
l1.pop(3);
#5
l1
#[1, 3, 4, 8, 10, 12, 10]
l2.clear();
l2
#[]
l1.reverse();
l1
#[10, 12, 10, 8, 4, 3, 1]
l1.reverse();
r1 = range(1,5,1);
r1
#range(1, 5)
r1.reverse();
"""
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    r1.reverse();
AttributeError: 'range' object has no attribute 'reverse'
"""
l1.index(10);
#4
l1.index(100);
"""Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    l1.index(100);
ValueError: 100 is not in list
"""
l1.index();
"""
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    l1.index();
TypeError: index expected at least 1 argument, got 0
"""
l1
#[1, 3, 4, 8, 10, 12, 10]
[ 3+4 for var in l1]
#[7, 7, 7, 7, 7, 7, 7]
[ 2*i+1 for i in range(5)]
#[1, 3, 5, 7, 9]
n = int(input("enter any number ");
        
#SyntaxError: invalid syntax
n = int(input("enter any number"));
        
#enter any number5
n = int(input("enter any number"))
        
#enter any numberdf
"""
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    n = int(input("enter any number"))
ValueError: invalid literal for int() with base 10: 'df'
"""
n = int(input("enter any number")) [ 2*i+1 for i in range(n)]
        
#SyntaxError: invalid syntax
n = int(input("enter any number")); [ 2*i+1 for i in range(n)]
        
#enter any number3
[1, 3, 5]
n = int(input("enter any number")); [ 2*i+1 for i in range(n)]
        
"""enter any number100
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199]
"""
