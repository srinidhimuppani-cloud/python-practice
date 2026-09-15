name = input("Enter Student Name:")
roll_no = input("Enter Roll Number:")
python_marks = int(input("Enter Python marks (0-100):"))
while python_marks < 0 or python_marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    python_marks = int(input("Enter Python marks (0-100):"))
c_marks = int(input("Enter C marks (0-100):"))
while c_marks < 0 or c_marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    c_marks = int(input("Enter C marks (0-100):"))
java_marks = int(input("Enter Java marks (0-100):"))
while java_marks < 0 or java_marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    java_marks = int(input("Enter Java marks (0-100):"))
maths_marks = int(input("Enter Maths marks (0-100): "))
while maths_marks < 0 or maths_marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    maths_marks = int(input("Enter Maths marks (0-100): "))
english_marks = int(input("Enter English marks (0-100):"))
while english_marks < 0 or english_marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    english_marks = int(input("Enter English marks (0-100):"))
total = python_marks + c_marks + java_marks + maths_marks + english_marks
percentage = total / 5
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
if percentage >= 50 and python_marks >= 35 and c_marks >= 35 and java_marks >=35 and maths_marks >= 35 and english_marks >= 35:
    result = "PASS"
else:
    result = "FAIL"
print("\n------STUDENT RESULT -----")
print("Name:",name)
print("Roll Number:",roll_no)
print("Python Marks:",python_marks)
print("C Marks:",c_marks)
print("Java Marks",java_marks)
print("Maths Marks:",maths_marks)
print("English Marks:",english_marks)
print("Total Marks:", total)
print("Percentage:",percentage)    
print("Grade:",grade) 
print("Result:",result)
if result == "PASS":
    print("Congratulations! you passed.")
else:
    print("Better luck next time!")                           
             
             