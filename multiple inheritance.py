class Person:
    def __init__(self,name , contact_number):
        self.__Name = name
        self.__Contact_Number = contact_number

    @property 
    def Name (self):
        return self.__name
    @Name.setter
    def Name (self,n):
        self.__name = n
    
    @property 
    def Contact_Number (self):
        return self.__Contact_number
    @Contact_Number.setter
    def Name (self,n):
        self.__contact_number = n
    
    def __str__ (self):
        
        vstr = str(self.__Name)
        vstr += " , "
        vstr += str(self.__Contact_Number)
        return vstr


class Students(Person):
    def __init__(self,name,contact_number,department,semester):
        super().__init__(name,contact_number)
        self.__Department = department
        self.__Semester = semester
    
    @property
    def Department(self):
        return self.__department
    @Department.setter
    def Department(self,n):
        self.__department = n
    
    def __str__ (self):
        vstr = super().__str__()
        vstr += " , "
        vstr += str(self.__Department)
        vstr += " , "
        vstr += str(self.__Semester)
        return vstr



class Teacher(Person):
    def __init__(self,name,contact_number,course,office_number):
        super().__init__(name,contact_number)
        self.__Course = course
        self.__Office_Number = office_number

    @property
    def Course(self):
        return self.__course
    @Course.setter
    def Course(self,n):
        self.__course = n
    
    @property
    def Office_Number (self):
        return self.__office_Number
    @Office_Number.setter
    def Office_Number(self,n):
        self.__office_Number = n
    
    def __str__ (self):
        vstr = super().__str__()
        vstr += " , "
        vstr += str(self.__Course)
        vstr += " , "
        vstr += str(self.__Office_Number)
        return vstr
    
class TeacherAssisstant(Students,Teacher):
    def __init__(self,name,contact_number,department,semester,course,office_number):
        self.__Name = name
        self.__Contact_Number = contact_number
        self.__Department = department
        self.__Semester = semester
        self.__Course = course
        self.__Office_Number = office_number

    def __str__(self):
        vstr = str(self.__Name)
        vstr += " , "
        vstr += str(self.__Contact_Number)
        vstr += " , "
        vstr += str(self.__Department)
        vstr += " , "
        vstr += str(self.__Semester)
        vstr += " , "
        vstr += str(self.__Course)
        vstr += " , "
        vstr += str(self.__Office_Number)
        return vstr

def main():
    std_name = "Ali"
    std_contact = "0300-12345678"
    std_course = "Bachelor"
    std_dept = "Data Science"
    std_semester = "2"
    teach_name = "Muhammad Idress"
    teach_office_number = "0420000000"
    teach_contact = "03000000000"
    teach_course = "OOP"
    ta_name = "Ali"
    ta_contact = "0300000000"
    ta_dept = "Data Science"
    ta_semester = "4"
    ta_course = "OOP Lab"
    ta_office_number = "0420000000"
    p = Person(std_name,std_contact)
    s = Students(std_name,std_contact,std_dept,std_semester)
    t = Teacher(teach_name,teach_contact,teach_course,teach_office_number)
    ta = TeacherAssisstant(ta_name,ta_contact,ta_dept,ta_semester,ta_course,ta_office_number)
    print("Person Data: " , end =" ")
    print(p)
    print("Student Data: " , end = " ")
    print(s)
    print("Teacher Data: " , end = " ")
    print(t)
    print("Teacher Assistant Data: " , end = " ")
    print(ta)
if __name__ == "__main__":
    main()