# Evin Killian, Tyler Campanile

from student import Student
from teacher import Teacher

def main():
    file = open("list.txt", "r")
    students = create_students(file)
    t_file = open("teachers.txt", "r")
    teachers = create_teachers(t_file)
    students = assign_teachers(students, teachers)
    teachers = complete_teacher_list(students, teachers)
    print_prompt()
    main_loop(students, teachers)
    

def create_students(file):
    students_file = file.readlines()
    students = []
    for student_line in students_file:
        student = student_line.split(",")
        student_obj = Student(student[0], student[1], student[2], student[3], student[4], student[5])
        student_obj.t_first = student_obj.t_first.replace('\n', '')
        students.append(student_obj)
        
    return students
    
    
def create_teachers(file):
    teacher_file = file.readlines()
    teachers = []
    for teacher_line in teacher_file:
        teacher = teacher_line.split(",")
        teacher_obj = Teacher(teacher[0], teacher[1], teacher[2])
        teacher_obj.classroom = teacher_obj.classroom.replace('\n', '')
        teachers.append(teacher_obj)        
    return teachers

def assign_teachers(students, teachers):
    for teacher in teachers:
        for i, student in enumerate(students):
            if int(student.classroom) == int(teacher.classroom):
                student.t_first = teacher.first
                student.t_last = teacher.last
                students[i] = student
                
    
    return students
    
def complete_teacher_list(students, teachers):
    for i, teacher in enumerate(teachers):
        for student in students:
            if int(student.classroom) == int(teacher.classroom):
                teacher.grade = student.grade
                teachers[i] = teacher
    return teachers
    
    
def print_prompt():
    print("List of Commands:\n")
    print("   S[tudent] <lastname> [B[us]]")
    print("   T[eacher] <lastname>")
    print("   B[us] <number>")
    print("   G[rade] <number> [H[igh]|L[ow]]")
    print("   A[verage] <number>")
    print("   C[lassroom] <number>")
    print("   An[alysis] <G[rade]|T[eacher]|B[us]>")
    print("   I[nfo]")
    print("   E[nrollment]")
    print("   Q[uit]\n")
    
def main_loop(students, teachers):
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
        elif command == "E" or command == "Enrollment":
            classroom_enrollment(students)
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
            search_grade(students, teachers, option[1], low, high)
        elif command == "A" or command == "Average":
            gpa = average_gpa(students, option[1])
            print("   grade level: " + str(option[1]) + "\n   gpa average: " + str(gpa))
        elif command == "C" or command == "Classroom":
            search_classroom(students, teachers, option[1])
        elif command == "An" or command == "Analytics":
            if option[1] == "G" or option[1] == "Grade":
                analyze_grade(students)
            elif option[1] == "T" or option[1] == "Teacher":
                analyze_teacher_avg_gpa(students, teachers)
        else:
            pass
            #Invalid input
            
            
def search_teacher(students, lastname):
    print("Students belonging to teacher: ")
    for student in students:
        if(student.t_last == lastname):
            print("   " + student.last + "," + student.first)
    
def search_grade(students, teachers, grade, low, high):
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
        print("Teachers whom teach grade level " + grade)
        for teacher in teachers:
            if teacher.grade == grade:
                print("   " + teacher.last + "," + teacher.first)
        
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
        if int(student.grade) == int(grade):
            size += 1
            gpa_sum += float(student.gpa)
   
    if size > 0:
        gpa_avg = gpa_sum / size
    #print("   grade level: " + str(grade) + "\n   gpa average: " + str(gpa_avg))
    return gpa_avg
    

    
def sort_classroom(student):
    return int(student.classroom)
    
    
def classroom_enrollment(students):
    students.sort(key = sort_classroom)
    print("Enrollment by classroom: ")
    count = 0
    classroom = -1
    for student in students:
        if int(student.classroom) != classroom:
            if classroom != -1:
                print("   Room: " + str(classroom) + ", Students: " + str(count))
            classroom = int(student.classroom)
            count = 1
        else:
            count += 1
    print("   Room: " + str(classroom) + ", Students: " + str(count))
        
       
def analyze_grade(students):
    print("Average gpa by grade: ")
    for i in range(1, 7):
        gpa = average_gpa(students, i)
        print("Grade: " + str(i) + ", Average gpa: " + str(gpa))
    return

#NR1 & NR2 C[lassroom] <Number>
def search_classroom(students, teachers, classroom):
    print("   STUDENTS")
    for student in students:
       if int(classroom) == int(student.classroom):
           print("   " + student.last + ", " + student.first)
           
    print("\n   TEACHERS")
    for teacher in teachers:
       if int(classroom) == int(teacher.classroom):
          print("   " + teacher.last, ", " + teacher.first)
          
def analyze_teacher_avg_gpa(students, teachers):
    for teacher in teachers:
        print(teacher.last + ", " + teacher.first + "  avg gpa: ", end="")
        sum_gpa = 0
        num_teaches = 0
        for student in students:
            if student.t_last == teacher.last and student.t_first == teacher.first:
                num_teaches += 1
                sum_gpa += float(student.gpa)
        
        if num_teaches > 0:
            print(f'{sum_gpa/num_teaches:.2f}')
        else:
            print(0.00)
          
        
if __name__ == "__main__":
    main()
