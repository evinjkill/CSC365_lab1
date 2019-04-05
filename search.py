from student import Student

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
    print("List of Commands:\n")
    print("   S[tudent]: <lastname> [B[us]]")
    print("   T[eacher]: <lastname>")
    print("   B[us]: <number>")
    print("   G[rade]: <number> [H[igh]|L[ow]]")
    print("   A[verage]: <number>")
    print("   I[nfo]")
    print("   Q[uit]\n")
    
def main_loop(students):
    
    while(True):
        option = input("Option: ")
        option = option.split()
        
        command = option[0]
        # Check commands with no arguments first 
        if(command == "I" or command == "Info"):
            pass
        elif(command == "Q" or command == "Quit"):
            break
        elif(len(option) < 2):
            print("Command requires arguments\n")
        elif(command == "S" or command == "Student"):
            pass
        elif(command == "T" or command == "Teacher"):
            search_teacher(students, option[1])
        elif(command == "B" or command == "Bus"):
            search_bus(students, option[1])
        elif(command == "G" or command == "Grade"):
            search_grade(students, option[1])
        elif(command == "A" or command == "Average"):
            pass
        
        else:
            pass
            #Invalid input
            
            
def search_teacher(students, lastname):
    print("Students belonging to teacher: ")
    for student in students:
        if(student.t_last == lastname):
            print("   " + student.last + "," + student.first)
    
def search_grade(students, grade):
    print("Students in grade level " + grade)
    for student in students:
        if student.grade == grade:
            print("   " + student.last + "," + student.first)
            
def search_bus(students, bus):
    print("Students who take bus " + bus)
    for student in students:
        if student.bus == bus:
            print("   " + student.last + "," + student.first + "," + student.grade + "," + student.classroom)

if __name__ == "__main__":
    main()