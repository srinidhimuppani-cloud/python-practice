python_marks = int(input("Enter Python marks:"))
c_marks = int(input("Enter C marks:"))
java_marks = int(input("Enter Java marks:"))
maths_marks = int(input("Enter Maths marks: "))
english_marks = int(input("Enter English marks:"))
total = python_marks + c_marks + java_marks + maths_marks + english_marks
percentage = total / 5
print("Total Marks:", total)
print("Percentage:",percentage)
if percentage >= 90:
    grade = "A+"
elif  percentage >= 80:
    grade = "A" 
elif  percentage >= 70:
    grade = "B"   
elif  percentage >= 60:
    grade = "C"
elif  percentage >= 50:
    grade = "D"     
else:
    grade = "F"
print("Grade:",grade)
if percentage >= 50:
    result = "PASS"
else:
    result = "FAIL" 
print("Result:",result)                       
             
             