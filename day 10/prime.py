numbers=int(input("enter a values:"))
def is_prime(n):
     if n < 2:
      return False
for i in range(2,int(n ** 0.5) + 1):
     if  n  % i == 0:
         return False
         return  True
prime_count=sum(1 for num in munber if is_prime(num))
print("Nmuber of prime in the set:",prime_count)
                    
