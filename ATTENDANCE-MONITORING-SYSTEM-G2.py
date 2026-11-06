# ============================================================

# FRESHMEN BSIT STUDENT ATTENDANCE MONITORING

# PHINMA Cagayan de Oro City

# ============================================================

# Beginner-friendly version using basic Python only.

# Records stay in memory and reset when the program closes.

# Attendance has no time limit.

students = []

attendance_records = []

active_session = []

# Text file used to save the records.
# It uses only basic string/list operations.
DATA_FILE = "attendance_records.txt"


def save_records(student_list, record_list, session):
    file = open(DATA_FILE, "w")
    file.write("STUDENTS\n")

    for student in student_list:
        file.write("STUDENT|" + str(student[0]) + "|" + str(student[1]) + "|" + str(student[2]) + "|" + str(student[3]) + "|" + str(student[4]) + "\n")

    file.write("ATTENDANCE\n")

    for record in record_list:
        file.write("ATTENDANCE|" + str(record[0]) + "|" + str(record[1]) + "|" + str(record[2]) + "|" + str(record[3]) + "|" + str(record[4]) + "\n")

    file.write("SESSION\n")

    if len(session) == 2:
        file.write("SESSION|" + str(session[0]) + "|" + str(session[1]) + "\n")

    file.close()


def load_records(student_list, record_list, session):
    try:
        file = open(DATA_FILE, "r")
        lines = file.readlines()
        file.close()

        student_list.clear()
        record_list.clear()
        session.clear()

        for line in lines:
            line = line.strip()

            if line.startswith("STUDENT|"):
                values = line.split("|")
                if len(values) == 6:
                    student_list.append([values[1], values[2], values[3], values[4], values[5]])

            elif line.startswith("ATTENDANCE|"):
                values = line.split("|")
                if len(values) == 6:
                    record_list.append([values[1], values[2], values[3], values[4], values[5]])

            elif line.startswith("SESSION|"):
                values = line.split("|")
                if len(values) == 3:
                    session.append(values[1])
                    session.append(values[2])

    except:
        return


def show_line():

    print("------------------------------------------------------------")



def ask_required(prompt):
    value = input(prompt).strip()
    while value == "":
        print("INVALID INPUT: This field cannot be empty. Please try again.")
        value = input(prompt).strip()
    return value


def ask_person_name(prompt):
    value = ask_required(prompt)
    while not any(letter.isalpha() for letter in value) or not all(letter.isalpha() or letter.isspace() or letter in ".-'’" for letter in value):
        print("INVALID NAME: Use letters, spaces, apostrophes, periods, or hyphens only.")
        value = ask_required(prompt)
    return value


def ask_identifier(prompt):
    value = ask_required(prompt)
    while not all(letter.isalnum() or letter == "-" for letter in value) or not any(letter.isalnum() for letter in value):
        print("INVALID ID: Use letters, numbers, and hyphens only, with no spaces.")
        value = ask_required(prompt)
    return value


def ask_date(prompt):
    value = ask_required(prompt)
    valid = False
    while not valid:
        if len(value) == 10 and value[4] == "-" and value[7] == "-" and value[0:4].isdigit() and value[5:7].isdigit() and value[8:10].isdigit():
            year = int(value[0:4])
            month = int(value[5:7])
            day = int(value[8:10])
            if month >= 1 and month <= 12:
                days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    days[1] = 29
                if day >= 1 and day <= days[month - 1] and year >= 1:
                    valid = True
        if not valid:
            print("INVALID DATE: Enter a real date using YYYY-MM-DD, for example 2026-10-24.")
            value = ask_required(prompt)
    return value


def ask_subject(prompt):
    value = ask_required(prompt)
    while not any(letter.isalpha() for letter in value):
        print("INVALID SUBJECT: Enter a subject name containing letters.")
        value = ask_required(prompt)
    return value


def ask_menu_choice(prompt, minimum, maximum):

    choice = input(prompt).strip()

    while not choice.isdigit() or int(choice) < minimum or int(choice) > maximum:

        print("INVALID INPUT: Choose a number from", minimum, "to", maximum, ".")

        choice = input(prompt).strip()

    return choice



def find_student(student_id, student_list):

    result = -1

    for num in range(len(student_list)):

        if student_list[num][0] == student_id:

            result = num

    return result



def find_attendance(student_id, subject, attendance_date, record_list):

    result = -1

    for num in range(len(record_list)):

        if (record_list[num][0] == student_id and

            record_list[num][1] == subject and

            record_list[num][2] == attendance_date):

            result = num

    return result



def show_student_details(student):

    show_line()

    print("Student ID :", student[0])

    print("Full Name  :", student[1])

    print("Course     :", student[2])

    print("Year Level :", student[3])

    print("Section    :", student[4])

    show_line()



def show_students(student_list):

    print("\n================ STUDENT LIST BY SECTION ================")

    if len(student_list) == 0:

        print("No students registered yet.")

    else:

        print("Total Students:", len(student_list))



        # Collect each section once, so students can be grouped together.

        section_list = []

        for student in student_list:

            section = student[4]

            if section not in section_list:

                section_list.append(section)



        # Display all students belonging to each section.

        for section in section_list:

            print("\n============================================================")

            print("SECTION:", section)

            print("============================================================")

            section_count = 0

            for student in student_list:

                if student[4] == section:

                    section_count = section_count + 1

                    print("\nStudent Number:", section_count)

                    show_student_details(student)

            print("Total students in", section, ":", section_count)



def show_students_by_section(student_list):

    print("\n================ FIND STUDENTS BY SECTION ================")

    if len(student_list) == 0:

        print("No students registered yet.")

        return



    section_name = ask_required("Enter Section Name: ")

    found = 0

    print("\n============================================================")

    print("STUDENTS IN SECTION:", section_name)

    print("============================================================")



    for student in student_list:

        if student[4] == section_name:

            found = found + 1

            print("\nStudent Number:", found)

            show_student_details(student)



    if found == 0:

        print("No students found in this section.")

    else:

        print("Total students in", section_name, ":", found)





def add_student(student_list):

    print("\n================ REGISTER NEW STUDENT ================")

    student_id = ask_identifier("Enter Student ID: ")

    position = find_student(student_id, student_list)

    if position != -1:

        print("That Student ID is already registered.")

    else:

        name = ask_person_name("Enter Full Name: ")

        course = "BSIT"

        year_level = "1st Year"

        section = ask_required("Enter Section: ")

        student_list.append([student_id, name, course, year_level, section])
        save_records(student_list, attendance_records, active_session)

        print("Freshman student registered successfully.")

        show_student_details(student_list[len(student_list) - 1])



def search_student(student_list):

    print("\n==================== SEARCH STUDENT ====================")

    student_id = ask_identifier("Enter Student ID: ")

    position = find_student(student_id, student_list)

    if position == -1:

        print("Student not found. Check the Student ID and try again.")

    else:

        print("Student found.")

        show_student_details(student_list[position])



def edit_student(student_list):

    print("\n===================== EDIT STUDENT =====================")

    student_id = ask_identifier("Enter Student ID to edit: ")

    position = find_student(student_id, student_list)

    if position == -1:

        print("Student not found.")

    else:

        student = student_list[position]

        show_student_details(student)

        print("Press Enter to keep the current value.")

        name = input("Full Name [" + student[1] + "]: ")

        section = input("Section [" + student[4] + "]: ")

        if name != "":

            student[1] = name

        if section != "":

            student[4] = section

        print("Student information updated successfully.")

        show_student_details(student)



def close_expired_session(student_list, record_list):

    # Attendance sessions no longer expire automatically.

    # This function remains so existing menu calls still work.

    return



def start_attendance_session():

    print("\n================ START ATTENDANCE SESSION ================")

    subject = ask_subject("Enter Subject Name: ")

    attendance_date = ask_date("Enter Date (YYYY-MM-DD): ")

    active_session.clear()

    active_session.append(subject)

    active_session.append(attendance_date)
    save_records(students, attendance_records, active_session)

    print("\nAttendance session created successfully.")

    print("Subject :", subject)

    print("Date    :", attendance_date)

    print("Students can enter their Student ID at any time while this session is active.")

    print("Students who do not check in will not be marked Absent automatically.")



def show_active_session():

    if len(active_session) == 0:

        print("No active attendance session.")

    else:

        print("\nActive Attendance Session")

        print("Subject :", active_session[0])

        print("Date    :", active_session[1])



def student_check_in(student_list, record_list):

    print("\n================ AUTOMATIC ATTENDANCE =================")

    if len(active_session) == 0:

        print("No attendance session is currently open.")

        return

    student_id = ask_identifier("Enter Student ID: ")

    student_position = find_student(student_id, student_list)

    while student_position == -1:

        print("INVALID STUDENT ID. Attendance was not recorded.")

        student_id = ask_identifier("Enter a registered Student ID: ")

        student_position = find_student(student_id, student_list)

    subject = active_session[0]

    attendance_date = active_session[1]

    if find_attendance(student_id, subject, attendance_date, record_list) != -1:

        print("Attendance already recorded for this student and session.")

        return

    record_list.append([student_id, subject, attendance_date, "Present", "Student ID check-in"])
    save_records(student_list, record_list, active_session)

    print("Attendance recorded successfully.")

    print("Student :", student_list[student_position][1])

    print("Status  : Present")



def choose_status():

    print("\nChoose Attendance Status:")

    print("1. Present")

    print("2. Absent")

    print("3. Late")

    choice = ask_menu_choice("Enter status number: ", 1, 3)

    if choice == "1":

        result = "Present"

    elif choice == "2":

        result = "Absent"

    elif choice == "3":

        result = "Late"

    else:

        result = ""

    return result



def record_attendance(student_list, record_list):

    print("\n================ MANUAL ATTENDANCE ===================")

    print("Teacher records attendance here. Existing records cannot be changed.")

    student_id = ask_identifier("Enter Student ID: ")

    position = find_student(student_id, student_list)

    if position == -1:

        print("Student not found. Register the student first.")

        return

    subject = ask_subject("Enter Subject Name: ")

    attendance_date = ask_date("Enter Date (YYYY-MM-DD): ")

    if find_attendance(student_id, subject, attendance_date, record_list) != -1:

        print("Attendance already exists for this student, subject, and date.")

        return

    status = choose_status()

    if status == "":

        print("Invalid status. Attendance was not recorded.")

        return

    remarks = input("Enter Remarks (press Enter if none): ").strip()

    record_list.append([student_id, subject, attendance_date, status, remarks])
    save_records(student_list, record_list, active_session)

    print("Attendance recorded successfully.")



def show_all_attendance(record_list):

    print("\n================ ALL ATTENDANCE RECORDS ================")

    if len(record_list) == 0:

        print("No attendance records available.")

    else:

        print("Total Attendance Records:", len(record_list))

        for num in range(len(record_list)):

            record = record_list[num]

            print("\nRecord Number:", num + 1)

            print("Student ID :", record[0])

            print("Subject    :", record[1])

            print("Date       :", record[2])

            print("Status     :", record[3])

            if record[4] == "":

                print("Remarks    : None")

            else:

                print("Remarks    :", record[4])

            show_line()



def student_attendance_history(student_list, record_list):

    print("\n============== STUDENT ATTENDANCE HISTORY ==============")

    student_id = ask_identifier("Enter Student ID: ")

    position = find_student(student_id, student_list)

    if position == -1:

        print("Student not found.")

    else:

        print("Attendance History for:", student_list[position][1])

        found = 0

        for record in record_list:

            if record[0] == student_id:

                print("Subject:", record[1], "| Date:", record[2],

                      "| Status:", record[3], "| Remarks:", record[4])

                found = found + 1

        if found == 0:

            print("No attendance records found for this student.")

        else:

            print("Total records found:", found)



def search_attendance_by_date(record_list):

    print("\n================ SEARCH ATTENDANCE BY DATE ================")

    attendance_date = ask_date("Enter Date (YYYY-MM-DD): ")

    found = 0

    for record in record_list:

        if record[2] == attendance_date:

            print("Student ID:", record[0], "| Subject:", record[1],

                  "| Status:", record[3], "| Remarks:", record[4])

            found = found + 1

    if found == 0:

        print("No attendance records found for that date.")

    else:

        print("Total records for", attendance_date, ":", found)



def attendance_summary(student_list, record_list):

    print("\n================ STUDENT ATTENDANCE SUMMARY ================")

    student_id = ask_identifier("Enter Student ID: ")

    position = find_student(student_id, student_list)

    if position == -1:

        print("Student not found.")

    else:

        present = 0

        absent = 0

        late = 0

        total = 0

        for record in record_list:

            if record[0] == student_id:

                total = total + 1

                if record[3] == "Present":

                    present = present + 1

                elif record[3] == "Absent":

                    absent = absent + 1

                elif record[3] == "Late":

                    late = late + 1

        print("Student Name       :", student_list[position][1])

        print("Student ID         :", student_id)

        print("Total Records      :", total)

        print("Present            :", present)

        print("Absent             :", absent)

        print("Late               :", late)

        if total > 0:

            result = (present + late) * 5

            print("Attendance Points  :", result, "%")

        else:

            print("No attendance records to calculate a percentage.")



def all_students_summary(student_list, record_list):

    print("\n================ SUMMARY OF ALL STUDENTS ================")

    if len(student_list) == 0:

        print("No students registered yet.")

    else:

        for student in student_list:

            present = 0

            absent = 0

            late = 0

            total = 0

            for record in record_list:

                if record[0] == student[0]:

                    total = total + 1

                    if record[3] == "Present":

                        present = present + 1

                    elif record[3] == "Absent":

                        absent = absent + 1

                    elif record[3] == "Late":

                        late = late + 1

            print("\nStudent:", student[1], "| ID:", student[0])

            print("Total:", total, "| Present:", present, "| Absent:", absent,

                  "| Late:", late)

            if total > 0:

                result = (present + late) * 5

                print("Attendance Points:", result, "%")

            else:

                print("Present Percentage: No records")



def report_menu(student_list, record_list):

    choice = ""

    while choice != "7":

        print("\n================ ATTENDANCE REPORTS ================")

        print("1. View All Attendance Records")

        print("2. View One Student's Attendance Summary")

        print("3. View Student Attendance History")

        print("4. Search Attendance by Date")

        print("5. View Summary of All Students")

        print("6. Find All Students by Section")

        print("7. Return to Teacher Menu")

        choice = input("Choose an option: ").strip().strip()

        if choice == "1":

            show_all_attendance(record_list)

        elif choice == "2":

            attendance_summary(student_list, record_list)

        elif choice == "3":

            student_attendance_history(student_list, record_list)

        elif choice == "4":

            search_attendance_by_date(record_list)

        elif choice == "5":

            all_students_summary(student_list, record_list)

        elif choice == "6":

            show_students_by_section(student_list)

        elif choice == "7":

            print("Returning to Teacher Menu.")

        else:

            print("Invalid option. Please choose from 1 to 7.")



def teacher_login(student_list, record_list):

    print("\n===================== TEACHER LOGIN =====================")

    teacher_id = ask_identifier("Enter Teacher ID (TCH-001 to TCH-010): ")

    valid_teacher = False

    while not valid_teacher:

        for num in range(1, 11):

            if teacher_id == "TCH-" + str(num).zfill(3):

                valid_teacher = True

        if not valid_teacher:

            print("INVALID TEACHER ID. Enter TCH-001 to TCH-010.")

            teacher_id = ask_identifier("Enter Teacher ID: ")

    print("Teacher login successful.")

    teacher_menu(student_list, record_list)



def teacher_menu(student_list, record_list):

    choice = ""

    while choice != "9":

        print("\n==================== TEACHER MENU ====================")

        print("1. Register Student")

        print("2. View All Students")

        print("3. Search Student")

        print("4. Edit Student Information")

        print("5. Start Attendance Session")

        print("6. Record Attendance Manually")

        print("7. Attendance Reports")

        print("8. View Active Session")

        print("9. Return to Main Menu")

        choice = input("Choose an option: ").strip().strip()

        if choice == "1":

            add_student(student_list)

        elif choice == "2":

            show_students(student_list)

        elif choice == "3":

            search_student(student_list)

        elif choice == "4":

            edit_student(student_list)

        elif choice == "5":

            start_attendance_session()

        elif choice == "6":

            record_attendance(student_list, record_list)

        elif choice == "7":

            report_menu(student_list, record_list)

        elif choice == "8":

            show_active_session()

        elif choice == "9":

            print("Returning to Main Menu.")

        else:

            print("Invalid option. Please choose from 1 to 9.")



def student_menu(student_list, record_list):

    student_check_in(student_list, record_list)



def main():

    choice = ""

    while choice != "3":

        print("\n============================================================")

        print("       FRESHMEN BSIT STUDENT ATTENDANCE MONITORING")

        print("              PHINMA Cagayan de Oro City")

        print("============================================================")

        print("1. Teacher Login")

        print("2. Student Menu")

        print("3. Exit System")

        choice = input("Choose an option: ").strip().strip()

        if choice == "1":

            teacher_login(students, attendance_records)

        elif choice == "2":

            student_menu(students, attendance_records)

        elif choice == "3":

            print("\nThank you for using the Attendance Monitoring System.")

            print("Program closed.")

        else:

            print("Invalid option. Please choose 1, 2, or 3.")



main()
