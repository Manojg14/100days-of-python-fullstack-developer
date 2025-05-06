"""
def vehicle(two_wheeler,four_wheeler):
    if two_wheeler %2 == 0 :
        wheeler2 = two_wheeler / 2
        print(f"Two wheeler required {int(wheeler2)}")

    else:
        print("Invalid Input!!")

    if four_wheeler % 2 == 0:
        wheeler4 = four_wheeler / 4
        print(f"Two wheeler required {int(wheeler4)}")

    else:
        print("Invalid Input!!")

    print("total wheels required to make a vehicles " ,int(wheeler2 + wheeler4))

two_wheeler = int(input("enter you required Two Wheeler:"))
four_wheeler = int(input("Enter you required four Wheeler:"))

print(vehicle(two_wheeler,four_wheeler)) """

"""
def vehicle_wheels(vehicle,wheeles):

    if wheeles < 2 or wheeles %2 != 0 or vehicle >= wheeles:
        print("INVALID INPUT")

    else:
        four_wheeler = (wheeles - 2 * vehicle) / 2
        two_wheeler = vehicle - four_wheeler
        print(f" TW = {two_wheeler} FW = {four_wheeler}")



print(vehicle_wheels(int(input("enter a vehicle:")),int(input("enter a wheeles:"))))
"""

def letter(name):
    count1 = count2 = 0

    for Letter in name:
        if Letter == '*':
            count1 += 1
        elif Letter == '#':
            count2 += 1
    if count1 > count2:
        print(f"positive integer {count1+count2}")
    elif count2 > count1:
        print(f"negative integer {count2+count1}")
    else:
        print(f"{count1-count2}number of * and # are equal")




print(letter(input("enter name:")))




