list = [12,24,35,70,88,120,155]
list = [x for (i,x) in enumerate(list) if i not in (0,4,5)]
print list
