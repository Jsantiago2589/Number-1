def main ():
    farhrenheit = float(input("What is the temperature? "))
    f= (farhrenheit)
    b= (farhrenheit-32)*(5/9)
    print ("Your temperature is", f ,"in Fahrenheit")
    print ("Which means that your temperature in", b ,"in Celsius")
    question= input("would you like to put in another temperature? ")
    if question == "yes":
        main()
    elif question == "no":
        print ("Thank you. Please use this program again soon.")
main ()