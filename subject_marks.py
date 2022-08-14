marathi_marks = int(input("Enter marathi mark "))

science_marks = int(input("Enter science marks "))

physics_marks = int(input("Enter physics marks "))

chemistry_marks = int(input("Enter chemistry marks "))

mathematics_marks = int(input("Enter mathematics marks "))

biology_marks = int(input("Enter biology marks "))


print ("Your marathi mark is ", marathi_marks)
print ("your science mark is ", science_marks )
print ("your physics mark is ", physics_marks )
print ("your chemistry mark is ", chemistry_marks )
print ("your mathematics mark is ", mathematics_marks )
print ("your biology mark is ", biology_marks )

total_marks = marathi_marks + science_marks + physics_marks + biology_marks + chemistry_marks + mathematics_marks 
out_off = 600
percentage = total_marks/out_off*100
print ("your total mark is ", total_marks, 'out of', out_off )
print ("your percentage is ", percentage, "%")