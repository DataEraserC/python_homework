input_str = input("please input")
count = {"digital":0,"alpha":0,"space":0,"other":0}
for char in input_str:
    if ord('0')<=ord(char)<=ord('9'):
        count['digital'] += 1
        continue
    if char.isalpha():
        count['alpha'] += 1
        continue
    if char == " ":
        count['space'] += 1
        continue
    count['other'] += 1 
print(count)

