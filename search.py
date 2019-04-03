

def main():
    
    file = open("students.txt", "r")
    students = create_students(file)
    
    print_prompt()
    main_loop(students)
    

def create_students(file):
    students_file = file.readlines()
    
    students = []
    for student_line in students_file:
        student = student_line.split(",")
        student_obj = Student(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7])
        students.append(student_obj)
        
    return students
    
    
def print_prompt():
    
    
def main_loop(students):
    
    
    while(true):
        option = input("Option: ")
        
        if(option == "S" or option == "Student"):
            
        elif(option == "T" or option == "Teacher"):
            
        elif(option == "B" or option == "Bus"):
            
        elif(option == "G" or option == "Grade"):
            
        elif(option == "A" or option == "Average"):
            
        elif(option == "I" or option == "Info"):
            
        elif(option == "Q" or option == "Quit"):
            
        else:
            #Invalid input
            
            
        
    