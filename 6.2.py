def has_duplicate(list):
    count = {}
    for item in list:
        count[item] = count.get(item,0) + 1
    for k in count:
        if(count[k]>=2):
            return True
    return False
list1 = [123,234,345,456]
list2 = [123,234,345,456,123]
print(list1,"has" if has_duplicate(list1) else "has not", "duplicate")
print(list2,"has" if has_duplicate(list2) else "has not", "duplicate")
