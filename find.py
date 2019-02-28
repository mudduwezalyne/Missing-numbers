a = [1,2,3,5,6,7,9]
b = [x for x in range(a[0], a[-1] + 1)]
a = set(a)
print (list(a ^ set(b)))
