a=input("enter a elements:")
set=set(a.split())
frozen=frozenset(set)
print("set:",set)
print("frozen set:",frozen)
if item in frozen:
    print(item,"yes is frozen.")
else:
    print(item,"no dose not frozen.")
    
