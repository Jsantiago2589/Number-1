def prime(a):
    z = 2
    while z < a :
        if a % z == 0:
            return False
        z += 1
    return True

z = 2
while z <= 100 :
    if prime(z):
        print(z, "is a Prime Number")
    z= z+1

