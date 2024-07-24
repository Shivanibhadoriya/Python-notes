x=5;

print(float(x));
#5.0

print(str(x)+"hello");
#5hello

x=2.34;

print(int(x));
#2

x="2.35";

#print(int(x));
#ValueError: invalid literal for int() with base 10: '2.35'

print(float(x));
#2.35

print(int(float(x)))
#2

x=True;

print(str(x));  #True

print(int(x));  #1

print(float(x)); #1.0

print(complex(x));

x="abc"

#print(int(x)); #ValueError: invalid literal for int() with base 10: 'abc'

x="abc12";

#print(int(x)); #ValueError: invalid literal for int() with base 10: 'abc12'

x = "1231b";

#print(int(x)); #invalid literal for int() with base 10: '1231b'
