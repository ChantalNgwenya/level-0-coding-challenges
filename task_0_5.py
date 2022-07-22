def area_of_triangle(num1,num2,num3):
    semi_perimeter = (num1 + num2 + num3) /2  
    
    area = (semi_perimeter* ( semi_perimeter-num1)* (semi_perimeter - num2)* (semi_perimeter -num3))** 0.5
    return area

print(area_of_triangle(5,6,7))
