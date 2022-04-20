
num1 = 5
num2 = 6
num3 = 7

def area_of_triangle(num1,num2,num3):
    if( num1 < 0  or num2 < 0 or num3 < 0 or num1+num3 <=num2 or num2+num3 <=num1 ):
        print ("Not a triangle")
        return
    sum = (num1 + num2 + num3) /2  
    
    area = (sum* ( sum-num1)* (sum - num2)* (sum -num3))** 0.5
    print("Area of a triangle is %f" %area)

area_of_triangle(num1,num2,num3)
