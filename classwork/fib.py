def feb(n):
    """ This gives fibnocci series nos
this is multi line checking"""
    a,b=0,1
    while a < n:
       print a,
       a,b = b,a+b
def evenorodd(N):
    for num1 in range(2, N):
        if num1 % 2 == 0:
            print("Found an even number", num1)
            continue
        else:
            print("Found a number", num1)

