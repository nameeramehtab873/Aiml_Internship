def calc_rectangle(length,width):
    area = length*width 
    perimeter = 2*(length+width)
    return area,perimeter
length=int(input("enter length:"))
width=int(input("enter width"))
area,perimeter=calc_rectangle(length,width)
print(f"area:{area},perimeter:{perimeter}")