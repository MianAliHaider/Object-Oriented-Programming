from random import*
class Polynomial:

    def __init__(self,variable="x",degree=0,coefficient=[]):
        self.Degree=degree
        self.Variable = variable
        self.Coefficient = coefficient
        
    @property
    def Degree(self):
        return self.__degree
    @Degree.setter
    def Degree(self,d):
        self.__degree = d

    @property
    def Variable(self):
        return self.__variable
    @Variable.setter
    def Variable(self,d):
        self.__variable = d

    @property
    def Coefficient(self):
        return self.__coefficient
    @Coefficient.setter
    def Coefficient (self , d):
        self.__coefficient = d

    def __str__(self):
        c = (self.Coefficient).copy()
        c.reverse()
        size = len(c)
        self.terms=[]
        for i in range(size):
            polynomial = ""
            if c[i] == 0:
                continue
            else:
                if (size-i-1) != 0:
                    if c[i] == 1:
                        if size-i-1 != 0:
                            polynomial = polynomial + str (self.Variable)
                        else:
                            polynomial = polynomial + str (self.Variable) + "^" + str(size-i-1)
                    elif c[i]==-1:                  
                        if size-i-1==1:                
                            polynomial = polynomial + '-' + str(self.Variable)
                        else:
                            polynomial = polynomial + '-' + str(self.Variable) + '^' + str(size-i-1)
                    else:                           
                        if size-i-1==1:                
                            polynomial = polynomial + str(c[i]) + str(self.Variable)
                        else:
                            polynomial = polynomial + str(c[i]) + str(self.Variable) + '^' + str(size-i-1)
                else: 
                    polynomial = polynomial + str(c[i])
                (self.terms).append(polynomial)       
        term = ' + '.join (self.terms) 
        return term.replace('+ -', '- ')
    def __add__(self, other):
        d = max(self.Degree, other.Degree)
        s = []
        x = (self.Coefficient).copy()
        y = (other.Coefficient).copy()
        if len(x)>len(y):
            t = len(x)-len(y)
            for i in range (t):
                (y).append(0)
            
        elif len(x)<len(y):
            t = len(y)-len(x)
            for i in range (t):
                (x).append(0)
                

        for i in range (len(x)):
            s.append(x[i]+y[i])
        return Polynomial(self.Variable, d, s)
    
    def __mul__ (self, other):       
        coefficient = [0]*(len(self.Coefficient)+len(other.Coefficient)-1)   
        for i in range (len(self.Coefficient)):           
            for j in range (len(other.Coefficient)):      
                coefficient[i+j]+=(self.Coefficient[i]*other.Coefficient[j]) 
        return Polynomial(self.Variable, self.Degree+other.Degree, coefficient)
    
def main():
    variable_1 = str(input ("Enter the first polynomial variable: "))
    degree_1 = int(input("Enter the first polynomial degree: "))
    coefficient_1=[]
    for i in range (degree_1+1):
        coefficient_1.append(randint(0,9))
    while coefficient_1[len(coefficient_1)-1] == 0:
        coefficient_1[len(coefficient_1)-1] = randint(0,9)
    polynomail_1=Polynomial(variable_1,degree_1,coefficient_1)
    print(polynomail_1)
    
    variable_2 = str(input ("Enter the second polynomial variable: "))
    degree_2 = int(input("Enter the second polynomial degree: "))
    coefficient_2=[]
    for i in range (degree_2+1):
        coefficient_2.append(randint(0,9))
    while coefficient_2[len(coefficient_2)-1] == 0:
        coefficient_2[len(coefficient_2)-1] = randint(0,9)
    polynomail_2 = Polynomial(variable_2,degree_2,coefficient_2)
    print(polynomail_2)

    
    print(f"Polynomail_1 + Polynomail_2 : {polynomail_1 + polynomail_2}")
    print()
    print(f"Polynomail 1 * Polynomail 2 : {polynomail_1*polynomail_2}")
    print()
   
if __name__ == "__main__":
    main()
   


          
        
