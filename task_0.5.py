
x = float(input("Enter first side:")
y =float(input("Enter second side:"))
z = float(input("Enter third side"))

def area_of_triangle(x,y,z,):
    if( x < 0  or y < 0 or z < 0 or x+z <=y or y+z <=x ):
        print ("Not a triangle")
        return
    s = (x + y + z) /2  # calculates the semi-perimeter
    # It calculates the area
    area = (s* ( s-x)* (s - y)* (s -z))** 0.5
    print("Area of a triangle is %f" %area)

area_of_triangle(x,y,z)
