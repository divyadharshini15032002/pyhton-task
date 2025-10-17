int=(input("enter a values:").split())
vowels="aeiouAEIOU"
for name in int:
    count=sum(1 for ch in 'names' if ch in vowels)
    print(f"{name}: {count} vowels")
