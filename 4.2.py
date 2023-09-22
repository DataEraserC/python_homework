input_str = input("please input here:")
a=b=c=d=0
for char in input_str:
    if (ord('a') <=ord(char)<= ord('z')) or (ord('A') <=ord(char)<= ord('Z')):
        a += 1
        continue
    elif ord('0') <= ord(char) <= ord('9'):
        b += 1
        continue
    elif ord(' ') == ord(char):
        c += 1
        continue
    else:
        d += 1
        continue
print("English char total is",a)
print("digital char total is",b)
print("space char total is",c)
print("other char total is",d)
