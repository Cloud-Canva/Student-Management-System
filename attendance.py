
class Student:
    def __init__(self, name, student_id, number, email):
        self.name = name
        self.student_id = student_id
        self.number = number
        self.email = emaip
        self.attendance = []

    def mark_attendance(self, status):
        self.attendance.append(status)


class AttendanceSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        number = input("Enter student number: ")
        email = input("Enter student email: ")
        student = Student(name, student_id, number, email)
        self.students.append(student)

    def mark_student_attendance(self, student_id, status):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance(status)
                return True
        return False

    def calculate_attendance(self):
        attendance_data = {'<80%': [], '>=80%': []}
        for student in self.students:
            total_classes = len(student.attendance)
            if total_classes > 0:
                attendance_percentage = (student.attendance.count('P') / total_classes) * 100
                if attendance_percentage < 80:
                    attendance_data['<80%'].append((student.name, student.student_id, attendance_percentage))
                else:
                    attendance_data['>=80%'].append((student.name, student.student_id, attendance_percentage))
            else:
                attendance_data['<80%'].append((student.name, student.student_id, 0))
        return attendance_data


def main():
    attendance_system = AttendanceSystem()
    
    # Adding some sample students
    sample_student_data = [
        ("John Doe", "1234", "1234567890", "john.doe@example.com"),
        ("Jane Smith", "5678", "0987654321", "jane.smith@example.com"),
        # Add more sample students if needed
    ]
    
    for data in sample_student_data:
        student = Student(*data)
        attendance_system.students.append(student)

    while True:
        print("\n1. Add Student\n2. Mark Attendance\n3. Calculate Attendance\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            attendance_system.add_student()
        elif choice == "2":
            student_id = input("Enter student ID: ")
            status = input("Enter attendance status (P for Present, A for Absent): ").upper()
            if attendance_system.mark_student_attendance(student_id, status):
                print("Attendance marked successfully!")
            else:
                print("Student not found!")
        elif choice == "3":
            attendance_data = attendance_system.calculate_attendance()
            print("\nAttendance <80%:")
            for student in attendance_data['<80%']:
                print(f"Name: {student[0]}, ID: {student[1]}, Attendance: {student[2]:.2f}%")
            print("\nAttendance >=80%:")
            for student in attendance_data['>=80%']:
                print(f"Name: {student[0]}, ID: {student[1]}, Attendance: {student[2]:.2f}%")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main
