
x = 5
y =6
z = 7

def area_of_triangle(x,y,z,):
    if( x < 0  or y < 0 or z < 0 or x+z <=y or y+z <=x ):
        print ("Not a triangle")
        return
    s = (x + y + z) /2  
    
    area = (s* ( s-x)* (s - y)* (s -z))** 0.5
    print("Area of a triangle is %f" %area)

area_of_triangle(x,y,z)
