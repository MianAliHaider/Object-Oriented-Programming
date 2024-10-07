import os
import pickle

class Course:
    def __init__(self, code, title, credit_hours, semester, course_type):
        self.code = code
        self.title = title
        self.credit_hours = credit_hours
        self.semester = semester
        self.course_type = course_type

def save_courses(courses):
    with open("courses_data.pkl", "wb") as file:
        pickle.dump(courses, file)

def load_courses():
    if os.path.exists("courses_data.pkl"):
        with open("courses_data.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return []

def display_menu():
    print("\nMenu:")
    print("a) Add")
    print("s) Search")
    print("d) Delete")
    print("l) List All")
    print("e) Edit")
    print("q) Quit")

def add_course(courses):
    code = input("Enter course code: ")
    title = input("Enter course title: ")
    credit_hours = int(input("Enter credit hours: "))
    semester = int(input("Enter semester: "))
    course_type = str(input("Enter course type (core/elective): "))

    new_course = Course(code, title, credit_hours, semester, course_type)
    courses.append(new_course)
    save_courses(courses)
    print("Course added successfully!")

def search_course(courses):
    code = input("Enter course code to search: ")
    for course in courses:
        if course.code == code:
            print("Course Found:")
            print(f"Code: {course.code}")
            print(f"Title: {course.title}")
            print(f"Credit Hours: {course.credit_hours}")
            print(f"Semester: {course.semester}")
            print(f"Type: {course.course_type}")
            return
    print("Course not found!")

def delete_course(courses):
    code = input("Enter course code to delete: ")
    for course in courses:
        if course.code == code:
            courses.remove(course)
            save_courses(courses)
            print("Course deleted successfully!")
            return
    print("Course not found!")

def list_all_courses(courses):
    if not courses:
        print("No courses found.")
    else:
        print("\nAll Courses:")
        for course in courses:
            print(f"Code: {course.code}, Title: {course.title}, Semester: {course.semester}")

def edit_course(courses):
    code = input("Enter course code to edit: ")
    for course in courses:
        if course.code == code:
            print("Editing Course:")
            print(f"Code: {course.code}, Title: {course.title}, Semester: {course.semester}")

            title = input("Enter new title (press enter to keep the same): ")
            course.title = title if title else course.title

            credit_hours = input("Enter new credit hours (press enter to keep the same): ")
            course.credit_hours = int(credit_hours) if credit_hours else course.credit_hours

            semester = input("Enter new semester (press enter to keep the same): ")
            course.semester = int(semester) if semester else course.semester

            course_type = input("Enter new course type (press enter to keep the same): ")
            course.course_type = course_type if course_type else course.course_type

            save_courses(courses)
            print("Course edited successfully!")
            return
    print("Course not found!")

def main():
    courses = load_courses()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == 'a':
            add_course(courses)
        elif choice == 's':
            search_course(courses)
        elif choice == 'd':
            delete_course(courses)
        elif choice == 'l':
            list_all_courses(courses)
        elif choice == 'e':
            edit_course(courses)
        elif choice == 'q':
            print("Quitting program. Goodbye!")
            break
        else:
            print("Invalid input. Choose from below mentioned options.")

if __name__ == "__main__":
    main()
