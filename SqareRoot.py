import cmath

num=int(input("Enter number by your choice to find square root :"))
square_root=float(num**0.5)
print(square_root)


#another way
square_root1=cmath.sqrt(num)
print("square root of {} is {}".format(num,square_root1.real))