set1=input("enter a values:")
set1=set(set1.split())
set2=input("enter a values:")
set2=set(set2.split())
sym_diff=set1.symmetric_difference(set2)
print(sym_diff)


