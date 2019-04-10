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
        student_obj.t_first = student_obj.t_first.replace('\n', '')
        students.append(student_obj)
        
    return students
    
    
def print_prompt():
    print("List of Commands:\n")
    print("   S[tudent] <lastname> [B[us]]")
    print("   T[eacher] <lastname>")
    print("   B[us] <number>")
    print("   G[rade] <number> [H[igh]|L[ow]]")
    print("   A[verage] <number>")
    print("   I[nfo]")
    print("   Q[uit]\n")
    
def main_loop(students):
    
    while(True):
        option = input("Option: ")
        option = option.split()
        if len(option) > 0:
            command = option[0]
        else:
            command = "INVALID"
        # Check commands with no arguments first 
        if command == "I" or command == "Info":
            print_info(students)
        elif command == "Q" or command == "Quit":
            break
        elif len(option) < 2 and command != "INVALID":
            print("Invalid or incomplete command\n")
        elif command == "S" or command == "Student":
            find_students(students, option)
        elif command == "T" or command == "Teacher":
            search_teacher(students, option[1])
        elif command == "B" or command == "Bus":
            search_bus(students, option[1])
        elif command == "G" or command == "Grade":
            low = False
            high = False
            if len(option) > 2:
                if option[2] == "H" or option[2] == "High":
                    high = True
                elif option[2] == "L" or option[2] == "Low":
                    low = True
            search_grade(students, option[1], low, high)
        elif command == "A" or command == "Average":
            average_gpa(students, option[1])
        
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
                    print("   " + student.last + ", " + student.first + ", " + student.bus)

    #R4: S[tudent]: <lastname>
    elif len(options) == 2:
        last_name = options[1]
        for student in students:
            if last_name == student.last:
                print("   " + student.last + ", " + student.first + ", " + student.grade + ", " + student.classroom + ", " +
                          student.t_last + ", " + student.t_first)
    else:
        pass
        # invalid input

        
def print_info(students):
    for x in range(7):
        count = 0
        for student in students:
            if int(student.grade) == x:
                count += 1
        print("   Grade " + str(x) + ": " + str(count) + " Students")
        
#R10 A[verage] <Number>
def average_gpa(students, grade):
    gpa_sum = 0
    gpa_avg = 0
    size = 0
   
    for student in students:
        if student.grade == grade:
            size += 1
            gpa_sum += float(student.gpa)
   
    if size > 0:
        gpa_avg = gpa_sum / size
    print("   grade level: " + str(grade) + "\n   gpa average: " + str(gpa_avg))
        
if __name__ == "__main__":
    main()
