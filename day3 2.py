total_bill=float(input("enter the bill amt:"))
num_people=int(input("enter the number of people:"))
share_person=total_bill/num_people
print(f"total bill:{total_bill}.each person pays{share_person:.2f}")
print("data type of total bill:",type(total_bill))
print("datatype of num_people:",type(num_people))
print("datatype of share_person:",type(share_person))