studentData = {}
studentAvg = {}

def add_student(studentName):
    global studentData, studentAvg
    studentMathGrade = float(input("Enter student math grade: "))
    studentScienceGrade = float(input("Enter student science grade: "))
    studentEnglishGrade = float(input("Enter student english grade: "))
    studentData[studentName] = studentMathGrade, studentScienceGrade, studentEnglishGrade
    studentAvg[studentName] = (studentMathGrade + studentScienceGrade + studentEnglishGrade) / 3
    print(studentName + "" + str(studentAvg[studentName]))
    questions()
    

 
def questions():
    start = input("Do you want to add a student? (yes/no): ")
    if start == 'yes':
        studentName = input("Enter student name: ") 
        add_student(studentName)
    elif start == 'no':
        question1 = input("Would you like to display a student's average grade? (yes/no): ")
        if question1 == 'yes': 
            studentName = input("Enter student name to display: ")
            print(studentAvg[studentName])
            questions()
    else: 
        print("okay have a nice day!")

questions()