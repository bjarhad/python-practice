angle_1 = int(input("Enter your first angle "))
angle_2 = int(input("Enter your second angle "))
angle_3 = int(input("Enter your third angle "))

if (angle_1 < 90) and (angle_2 < 90) and (angle_3 <90):
    print("triangle is accute angle")
elif (angle_1 >90) or (angle_2 >90 ) or (angle_3 >90):
    print("triangle is obtuse angle")
elif (angle_1 == 90) or (angle_2 == 90) or (angle_3 == 90):
    print ("traingle is right angle")
