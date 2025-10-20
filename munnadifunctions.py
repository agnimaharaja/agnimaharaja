class munnadifunctions():
    def display_subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def OddEven():
        num1=int(input("Enter a number :"))
        if((num1%2)==0):
            print(f"{num1} is Even number")
        else:
            print(f"{num1} is Odd number")
    def Elegible():
        Gen=input("Your Gender :")
        Age=int(input("Your Age :"))
        if((Gen=="Male")&(Age>=21)):
            print("Elgible")
        elif((Gen=="Female")&(Age>=18)):
            print("Elgible")
        else:
            print("NOT ELIGIBLE")
    def Percentage(Subject1,Subject2,Subject3,Subject4,Subject5):
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=Total/5
        print("Subject1="f"{Subject1}")
        print("Subject2="f"{Subject2}")
        print("Subject3="f"{Subject3}")
        print("Subject4="f"{Subject4}")
        print("Subject5="f"{Subject5}")
        print("Total :"f"{Total}")
        print("Percentage :"f"{Percentage}")
    def triangle():
        Hgt=32
        Brd=34
        ArFrm=(Hgt*Brd)/2
        print("Height:"f"{Hgt}")
        print("Breadth:"f"{Brd}")
        print("Area Formula: (Height*Breadth)/2")
        print("Area of Triangle:"f"{ArFrm}")
        Hgt1=2
        Hgt2=4
        Brd1=4
        PerFrm=(Hgt1+Hgt2+Brd1)
        print("Height1:"f"{Hgt1}")
        print("Height2:"f"{Hgt2}")
        print("Breadth:"f"{Brd1}")
        print("Perimeter formula: Height1+Height2+Breadth1")
        print("perimeter of Triangle:"f"{PerFrm}")