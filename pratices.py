"""
Write a Python program that:

Asks the user to enter the number of students, n.
For each student:
Take the student's name as input.
Take the number of subjects for that student.
For each subject, take the subject name and the mark scored.
Store all this data in a dictionary of dictionaries, where:
The key is the student's name.
The value is another dictionary containing {subject_name: mark} pairs.
After collecting all data, print it in this format:
   Student: Ravi
     Math: 85
     Science: 90
   
   Student: Priya
     Math: 78
     Science: 88

Bonus (optional, once basic version works):

Calculate and print each student's total and average marks.
Find and print the student with the highest average (the "topper").
Find each student's highest scoring subject.

"""


students={}
number_student = int(input("Enter the Student Count :"))

for i in range(0,number_student):
    student_name = input("Enter the Student Name :")
    number_subject = int(input("Enter the Subject Count :"))

    mark ={}

    for j in range(0,number_subject):
        subject = input("Enter the Subject Name :")
        score = int(input(f"Enter the mark for {subject}:"))
        mark[subject] = score

    students[student_name] = mark  


print(mark)