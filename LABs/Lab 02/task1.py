def area_of_trapezoid(base_1, base_2, height):
    """This function calculates the area of trapezoid"""
    area = ((base_1 + base_2) * height) / 2
    print("Area of trapezoid is: ", area)
    
def area_of_parallelpgram(base, height):
    """This function calculates the area of parallelogram"""
    area = base * height
    print("Area of parallelpgram is: ", area)
 
Pi = 3.14   
def surface_area_of_cylinder(radius,height):
    """This function calculates the surface volume of cylinder"""
    surface_area = Pi*(radius**2)*height 
    print("Surface area of cylinder is: ", surface_area)
    
def area_of_cylinder(radius, height):
    """This function calculates the area of cylinder"""
    area = 2*Pi*radius*(radius + height)
    print("The area of cylinder is: ", area)
    
def main():
    area_of_trapezoid(2, 3, 5)
    area_of_parallelpgram(4, 6)
    surface_area_of_cylinder(4, 14)
    area_of_cylinder(7, 3)
    
main()
