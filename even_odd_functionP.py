num = int(input("Enter the Number: "))
def even_odd(num):  #function dedine for print even odd
    if num%2==0:
        print(num,"Even", end = " And ")
    else:
        print(num,"odd")

for num in range(num):
    even_odd(num) #function call even_odd
