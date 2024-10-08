class Student:
    def __init__(self,name = None, rollnumber = None , semester = None, cgpa = None , department_id = None):
        self.Name = name
        self.Roll_Number = rollnumber
        self.Semester = semester
        self.Cgpa = cgpa
        self.Department_id = department_id
        
    @property
    def Name (self):
        return self.__name
    @Name.setter
    def Name (self,n):
        self.__name = n
    
    @property
    def Roll_Number (self):
        return self.__rollnumber
    @Roll_Number.setter
    def Roll_Number (self,n):
        self.__rollnumber = n
    
    @property
    def Semester (self):
        return self.__semester
    @Semester.setter
    def Semester (self,n):
        self.__semester = n
        
        
    @property
    def Cgpa (self):
        return self.__cgpa
    @Cgpa.setter
    def Cgpa (self,n):
        self.__cgpa = n
        
    @property
    def Department_id (self):
        return self.__department_id
    @Department_id.setter
    def Department_id (self,n):
        self.__department_id = n    
        
    def __str__(self):
        a = str(self.Roll_Number)
        a += "\t"
        a += str(self.Name)        
        a += "\t\t\t"
        a += str(self.Semester)
        a += "\t\t "
        a += str(self.Cgpa)
        return a

class Department:
    def __init__(self ,department_name = None , chairman = None , department_id = None):
        self.Department_Name = department_name
        self.Chairman = chairman
        self.Department_id = department_id
    
    @property
    def Department_Name(self):
        return self.__department_name
    @Department_Name.setter
    def Department_Name(self,n):
        self.__department_name = n
        
    @property
    def Chairman(self):
        return self.__chairman
    @Chairman.setter
    def Chairman(self,n):
        self.__chairman = n
    
    @property
    def Department_id(self):
        return self.__department_id
    @Department_id.setter
    def Department_id(self,n):
        self.__department_id = n
      
      
    def __str__(self):
        a = "Department"
        a += ":"
        a += str(self.Department_id)
        a += ","
        a += str(self.Department_Name)
        a += ","
        a += str(self.Chairman)
        
        return a

from Student_class import Student
from Department_class import Department


def main():
    CS = []
    SE = []
    DS = []
    IT = []

    student_data = []
    student_data.append(Student("Ali","001",1,3.4,"IT"))
    student_data.append(Student("Azam","002",1,3.5,"DS"))
    student_data.append(Student("Shabbir","003",1,3.8,"SE"))
    student_data.append(Student("Raza","004",1,2.7,"IT"))
    student_data.append(Student("Bashir","005",1,3.9,"DS"))
    student_data.append(Student("Durrab","006",1,2.9,"CS"))
    student_data.append(Student("Talha","007",1,3.2,"CS"))
    student_data.append(Student("Rehan","008",1,3.7,"SE"))
    student_data.append(Student("Haider","009",1,3.2,"IT"))
    student_data.append(Student("Saad","010",1,2.90,"CS"))
    student_data.append(Student("Haris","011",1,3.6,"DS"))
    student_data.append(Student("Amina","012",2,3.7,"IT"))
    student_data.append(Student("Aqsa","013",2,1.6,"DS"))
    student_data.append(Student("Minahil","014",2,1.6,"SE"))
    student_data.append(Student("Mahmona","015",2,2.7,"IT"))
    student_data.append(Student("Kaif","016",2,1.7,"DS"))
    student_data.append(Student("Shahbaz","017",1,1.2,"CS"))
    student_data.append(Student("Shameer","018",2,1,"CS"))
    student_data.append(Student("Zameer ","019",1,3.7,"SE"))
    student_data.append(Student("Danish","020",1,1.4,"IT"))
    student_data.append(Student("Usman","021",1,2.90,"CS"))
    student_data.append(Student("Rukaya","022",1,3.6,"DS"))



    computer_science = Department("Computer Science"  ,  "Dr. Shahzad Sarwar", "CS") 
    software_engineering = Department("Software Engineering" , "Dr. Murtaza Yousaf", "SE")
    information_technology = Department("Information Technology" , "Dr. Waqar ul Qounain", "IT" )
    data_science = Department("Data Science" , "Dr. Shahid Manzoor", "DS")
    

    for i in range (len(student_data)):
        if student_data[i].Department_id == computer_science.Department_id:
            CS.append(student_data[i])
        elif student_data[i].Department_id == software_engineering.Department_id:
            SE.append(student_data[i])
        elif student_data[i].Department_id == data_science.Department_id:
            DS.append(student_data[i])
        else:
            IT.append(student_data[i])


    print(computer_science)
    print(f"Roll#\tName \t\t Semester \t\t CGPA")
    for i in range(len(CS)):
        print(CS[i])
    print()
    
    print(data_science)
    print(f"Roll#\tName \t\t Semester \t\t CGPA")
    for i in range(len(DS)):
        print(DS[i])

    print()
    print(information_technology)
    print(f"Roll#\t Name \t\t Semester \t\t CGPA")
    for i in range(len(IT)):
        print(IT[i])
        
    print()
    print(software_engineering)
    print(f"Roll#\t Name \t\t Semester \t\t CGPA")
    for i in range(len(SE)):
        print(SE[i])

    print()
    
#below lines for students whose CGPA less than 1.70.
    print("Below lines for students whose CGPA less than 1.70")
    print()
    print()
    print(computer_science)
    print(f"Roll#\tName \t\t Semester \t\t CGPA")
    for i in range(len(CS)):
        if CS[i].Cgpa<=1.70:
            print(CS[i])

    print()
    print(data_science)
    print(f"Roll#\tName \t\t Semester \t\t CGPA")
    for i in range(len(DS)):
        if DS[i].Cgpa<=1.70:
            print(DS[i])
            
    print()
    print(information_technology)
    print(f"Roll#\t Name \t\t Semester \t\t CGPA")
    for i in range(len(IT)):
        if IT[i].Cgpa<=1.70:
            print(IT[i])

    
    print()
    print(software_engineering)
    print(f"Roll#\t Name \t\t Semester \t\t CGPA")
    for i in range(len(SE)):
        if SE[i].Cgpa<=1.70:
            print(SE[i])

 
        
if __name__ == "__main__":
    main()
    

    
            


    

        
        
    
