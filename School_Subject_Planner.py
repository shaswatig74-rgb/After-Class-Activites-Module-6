# Creating a tuple of student details
student_profile = ("Aarav", "Grade 6", "Section A", 6)
# Accessing Tuple Elements
student_name = student_profile[0]
student_grade = student_profile[1]
student_section = student_profile[2]
student_total_subjects = student_profile[3]
print("First 2 details of student profile:", student_profile[0:2])
# Creating Subject Sets
monday_subjects = {"Math", "Science", "English", "Computer", "Art"}
tuesday_subjects = {"Math", "History", "English", "Sports", "Music"}
# Modifying Sets
monday_subjects.add( "Library") 
monday_subjects.discard("Art")
tuesday_subjects.add("Art")
tuesday_subjects.discard( "Music")
# Using Set Operations
all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
unique_subjects_monday = monday_subjects.difference(tuesday_subjects)
all_unique_subjects = monday_subjects.symmetric_difference(tuesday_subjects)
# Printing the Final Summary
print("Student Details:", student_profile)
print("Updated Subject Sets:", monday_subjects , "and", tuesday_subjects)
print("Common Subjects:", common_subjects)
print("All Unique Subjects:", all_unique_subjects)





