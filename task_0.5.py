def area_of_triangle(num1,num2,num3):
    if( num1 < 0  or num2 < 0 or num3 < 0 or num1+num3 <=num2 or num2+num3 <=num1 ):
        print ("Not a triangle")
        return None
    semi_perimeter = (num1 + num2 + num3) /2  
    
    area = (semi_perieter* ( semi_perimeter-num1)* (semi_perimeter - num2)* (semi_primeter -num3))** 0.5
    print("Area of a triangle is %f" %area)

area_of_triangle(5,6,7)
