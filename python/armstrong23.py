number=int(input("ENTER THE NUMBER:-"))
result=0
temp = number
while temp!=0:
    digit= temp % 10
    result= result+digit**3
    temp=temp//10
print(result)    
if number == result:
    print(number,"is an ARMSTRONG NUMBER.")
else:
    print(number,"is not an ARMSTRONG NUMBER.")    