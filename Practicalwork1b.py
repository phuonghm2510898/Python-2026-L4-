students = []
courses = []
marks = {}

def input_student():
    nt = int(input("Enter number of students: "))

    for i in range(nt):
        print(f"Student {i+1}: ")
        sid = input("Student ID: ")
        sname = input("Name: ")
        sdob = input("Date of Birth: ")

        Student = {
            "id": sid,
            "name": sname,
            "dob": sdob,
        }

        students.append(Student)

def input_course():
    nc = int(input("Enter number of course: "))
    for i in range(nc):
        print(f"\nSubject {i+1}: ")
        cid = input("Course ID: ")
        cname = input("Course name: ")

        Course = {
            "id" : cid,
            "name" : cname,
        }
        courses.append(Course)

        # Cách khác: courses.append({"id": c_id, "name": name})

def input_marks():
    print("\n Enter grades: ")
    cid = input ("Course ID (required): ")
    course_ids = [c["id"] for c in courses]
    if cid not in course_ids:
        print ("Not found")
        return

    marks[cid] = {}

    for s in students: 
        mark = float (input(f"Enter grade {s['name']} (ID: {s['id']}): "))
        marks[cid][s['id']] = mark     



def list_courses():
    print("\nList of courses: ")
    for c in courses:
        print(f"ID: {c['id']} \nName: {c['name']}")

def list_students():
    print("\nList of students: ")
    for s in students:
        print(f"ID: {s['id']} \nName: {s['name']} \n DOB {s['dob']}")

def show_student_marks():
    print("\nMarks: ")
    c_id = input("Course ID: ")
    
    if c_id not in marks:
        print("No data! ")
        return

    print(f"Academic record {c_id}:")
    for s in students:
        s_id = s['id']
        mark = marks[c_id].get(s_id, "No data")
        print(f"  {s['name']} (ID: {s_id}): {mark}")
