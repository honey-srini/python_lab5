def reverse(n):
    if n<10:
        print(n)
        return n
    else:
        print(n%10,end="")
        reverse(n//10)

num=int(input("Enter the number:"))
reverse(num)
