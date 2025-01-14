def is_prime(s):
    if s<2:
        return False
    for v in range(2,s):
        if s%v==0:
            return False
        return True
num=int(input("ENTER THE NUMBER:"))
if is_prime(num):
        print(f"(num) IS A PRIME NUMBER:")
else:
        print(f"(num) IS NOT A PRIME NUMBER:")       

