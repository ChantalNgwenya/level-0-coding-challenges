def area_of_triangle(num1,num2,num3):
    semi_perimeter = (num1 + num2 + num3) /2  
    
    area = (semi_perimeter* ( semi_perimeter-num1)* (semi_perimeter - num2)* (semi_perimeter -num3))** 0.5
    
    if( num1 < 0  or num2 < 0 or num3 < 0 or num1+num3 <=num2 or num2+num3 <=num1 ):
        print ("Not a triangle, its area is %f" %area)
        
    else:
        print("Area of a triangle is %f" %area)

area_of_triangle(5,6,7)
