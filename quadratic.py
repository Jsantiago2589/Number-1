print ("Welcome to the Program! Please enter the value of A,B,C and X at the corresponding prompt")
a= float(input("Enter your first number for a"))
b= float(input("Enter your second number for b"))
c= float(input("Enter your third number for c"))
x= float(input("Enter your forth number for x"))
quadratic= ((a*x**2)+(b*x)+c)
print ("The following quadratic was entered:", a,"X",x,"^2+",b,"X",x,"+",c)
print ("The value of the quadratic is", quadratic)