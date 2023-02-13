try:
    def myageinmonths():
        age =int(input("Enter your age"))
        months_lived =age * 12
        print(f"you have lived for {months_lived} months")

    myageinmonths()
except:
   print("Not a number")
