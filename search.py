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
            find_students(students, option)
        elif(command == "T" or command == "Teacher"):
            search_teacher(students, option[1])
        elif(command == "B" or command == "Bus"):
            search_bus(students, option[1])
        elif(command == "G" or command == "Grade"):
            low = False
            high = False
            if(len(option) > 2):
                if(option[2] == "H" or option[2] == "High"):
                    high = True
                elif(option[2] == "L" or option[2] == "Low"):
                    low = True
            search_grade(students, option[1], low, high)
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
    
def search_grade(students, grade, low, high):
    s_first = ""
    s_last = ""
    min_gpa = 5.0
    max_gpa = -1.0
    s_bus = ""
    t_first = ""
    t_last = ""
    
    if high == False and low == False:
        print("Students in grade level " + grade)
        for student in students:
            if student.grade == grade:
                print("   " + student.last + "," + student.first)
        
    elif low == True:
        print("Student with lowest gpa in grade level " + grade)
        for student in students:
            if student.grade == grade and float(student.gpa) < min_gpa:
                s_first = student.first
                s_last = student.last
                min_gpa = float(student.gpa)
                s_bus = student.bus
                t_first = student.t_first
                t_last = student.t_last
                
        print("   " + s_last + "," + s_first + "," + str(min_gpa) + "," + t_last + "," + t_first + "," + s_bus)
        
    else:
        print("Student with highest gpa in grade level " + grade)
        for student in students:
            if student.grade == grade and float(student.gpa) > max_gpa:
                s_first = student.first
                s_last = student.last
                max_gpa = float(student.gpa)
                s_bus = student.bus
                t_first = student.t_first
                t_last = student.t_last
                
        print("   " + s_last + "," + s_first + "," + str(max_gpa) + "," + t_last + "," + t_first + "," + s_bus)
                
            
        
            
def search_bus(students, bus):
    print("Students who take bus " + bus)
    for student in students:
        if student.bus == bus:
            print("   " + student.last + "," + student.first + "," + student.grade + "," + student.classroom)

def find_students(students, options):
    if len(options) == 3:
    #R5: S[tudent] <lastname> B[us]
        if options[2] == "B" or options[2] == "Bus":
            last_name = options[1]
            for student in students:
                if last_name == student.last:
                    print(student.last + ", " + student.first + ", " + student.bus)

    #R4: S[tudent]: <lastname>
    elif len(options) == 2:
        last_name = options[1]
        for student in students:
            if last_name == student.last:
                print(student.last + ", " + student.first + ", " + student.grade + ", " + student.classroom + ", " +
                          student.t_last + ", " + student.t_first)
    else:
        pass
        # invalid input

        
        
        
if __name__ == "__main__":
    main()
