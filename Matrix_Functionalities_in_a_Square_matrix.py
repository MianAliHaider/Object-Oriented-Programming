class square_matrix_of_2_by_2:
    def __init__(self,a=0,b=0,c=0,d=0):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d

    def __str__(self):
        vstr = "("
        vstr += str(self.__a)
        vstr += " , "
        vstr += str(self.__b)
        vstr += " , "
        vstr += str(self.__c)
        vstr += " , "
        vstr += str(self.__d)
        vstr += ")"
        return vstr
    def add_two_matrices(m1,m2):
        ad=square_matrix_of_2_by_2()
        ad.__a=m1.__a+m2.__a
        ad.__b=m1.__b+m2.__b
        ad.__c=m1.__c+m2.__c
        ad.__d=m1.__d+m2.__d
        return ad
    staticmethod(add_two_matrices)

    def subtract_two_matrices(m1,m2):
        subt=square_matrix_of_2_by_2()
        subt.__a=m1.__a-m2.__a
        subt.__b=m1.__b-m2.__b
        subt.__c=m1.__c-m2.__c
        subt.__d=m1.__d-m2.__d
        return subt
    staticmethod(subtract_two_matrices)

    def multiply_two_matrices(m1,m2):
        multiply=square_matrix_of_2_by_2()
        multiply.__a=(m1.__a*m2.__a+m1.__b*m2.__c)
        multiply.__b=(m1.__a*m2.__b+m1.__b*m2.__d)
        multiply.__c=(m1.__c*m2.__a+m1.__d*m2.__c)
        multiply.__d=(m1.__c*m2.__b+m1.__d*m2.__d)
        return multiply
    staticmethod(multiply_two_matrices)

    def determinant_of_two_matrices(m): 
        determinant=square_matrix_of_2_by_2()
        determinant=(m.__a*m.__d)-(m.__b*m.__c)
        return determinant
    staticmethod(determinant_of_two_matrices)

    def singular_of_matrices(m):
        singular=square_matrix_of_2_by_2()
        determinant=(m.__a*m.__d)-(m.__b*m.__c)
        if determinant==0:
            return "Matrix is Singular."
        else:
            return "Matrix is not Singular."
    staticmethod(singular_of_matrices)

    def identity_of_a_matrices(m):
        identity=square_matrix_of_2_by_2()
        if m.__a==1 and m.__d==1 and m.__b==0 and m.__c==0:
            return "Matrix is Identity"
        else:
            return "Matrix is non Identity"
    staticmethod(identity_of_a_matrices)

    def transpose_of_two_matrices(m):
        transpose=square_matrix_of_2_by_2()
        transpose.__a,transpose.__b,transpose.__c,transpose.__d=m.__a,m.__c,m.__b,m.__d
        return transpose
    staticmethod(transpose_of_two_matrices)

    def null_matrix(m):
        null=square_matrix_of_2_by_2()
        if m.__a==0 and m.__b==0 and m.__c==0 and m.__d==0:
            return "Matrix is null"
        else:
            return "Matrix is not null"
    staticmethod(null_matrix)

    def inverse_of_matrices(m):
        inverse=square_matrix_of_2_by_2()
        determinant=(m.__a*m.__d)-(m.__b*m.__c)
        inverse.__a=(m.__d)/determinant
        inverse.__b=-(m.__b)/determinant
        inverse.__c=-(m.__c)/determinant
        inverse.__d=(m.__a)/determinant
        return inverse
    staticmethod(inverse_of_matrices)

    def division_Of_a_matrix(m1,m2):
        determinant=(m1.__a*m1.__d)-(m1.__b*m1.__c)
        inverse=square_matrix_of_2_by_2()
        inverse.__a=(m1.__d)/determinant
        inverse.__b=-(m1.__b)/determinant
        inverse.__c=-(m1.__c)/determinant
        inverse.__d=(m1.__a)/determinant
        division=square_matrix_of_2_by_2()
        division.__a=(m1.__a*m2.__a)+(m1.__b*m1.__c)
        division.__b=(m1.__a*m2.__b)+(m1.__b*m2.__d)
        division.__c=(m1.__c*m2.__a)+(m1.__d*m2.__c)
        division.__d=(m1.__c*m2.__b)+(m1.__d*m2.__d)
        return division
    staticmethod(division_Of_a_matrix)

    def scalar_matrix_of_two_matrices(constant,m):
        scalar=square_matrix_of_2_by_2()
        scalar.__a=constant*m.__a
        scalar.__b=constant*m.__b
        scalar.__c=constant*m.__c
        scalar.__d=constant*m.__d
        return scalar
    staticmethod(scalar_matrix_of_two_matrices)

    def cofactor_of_a_matrix(m):
        cofactor=square_matrix_of_2_by_2()
        cofactor.__a=(-1)**(1+1) * m.__d
        cofactor.__b=(-1)**(1+2) * m.__c
        cofactor.__c=(-1)**(2+1) * m.__b
        cofactor.__d=(-1)**(2+2) * m.__a
        return cofactor
    staticmethod(cofactor_of_a_matrix)
        
    
def main():
    x=square_matrix_of_2_by_2(1,5,5,1)
    y=square_matrix_of_2_by_2(2,5,1,5)

    
    ad=square_matrix_of_2_by_2.add_two_matrices(x,y)
    print(f"Addition of Two Matrices x+y  :  {ad}")

    subt=square_matrix_of_2_by_2.subtract_two_matrices(x,y)
    print(f"Subtraction of Two Matrices  :  {subt}")

    multiply=square_matrix_of_2_by_2.multiply_two_matrices(x,y)
    print(f"Multiplicationof Two Matrices  :   {multiply}")

    determinant_m1=square_matrix_of_2_by_2.determinant_of_two_matrices(x)
    determinant_m2=square_matrix_of_2_by_2.determinant_of_two_matrices(y)
    print(f"Deteminant of matrix m1  :  {determinant_m1}")
    print(f"Deteminant of matrix m2  :  {determinant_m2}")


    singualar_m1=square_matrix_of_2_by_2.singular_of_matrices(x)
    singualar_m2=square_matrix_of_2_by_2.singular_of_matrices(y)
    print(f"Matrix m1  :  {singualar_m1}")
    print(f"Matrix m2  :  {singualar_m2}")

    identity_m1=square_matrix_of_2_by_2.identity_of_a_matrices(x)
    identity_m2=square_matrix_of_2_by_2.identity_of_a_matrices(y)
    print(f"Matrix m1  :  {identity_m1}")
    print(f"Matrix m2  :  {identity_m2}")

    
    transpose_m1=square_matrix_of_2_by_2.transpose_of_two_matrices(x)
    transpose_m2=square_matrix_of_2_by_2.transpose_of_two_matrices(y)
    print(f"Transpose of Matrix m1  :  {transpose_m1}")
    print(f"Transpose of Matrix m2  :  {transpose_m2}")

    null_m1=square_matrix_of_2_by_2.null_matrix(x)
    null_m2=square_matrix_of_2_by_2.null_matrix(y)
    print(f"Matrix m1  :  {null_m1}")
    print(f"Matrix m2  :  {null_m2}")    
    
    inverse_m1=square_matrix_of_2_by_2.inverse_of_matrices(x)
    inverse_m2=square_matrix_of_2_by_2.inverse_of_matrices(y)
    print(f"Inverse of m1  :  {inverse_m1}")
    print(f"Inverse of m2  :  {inverse_m2}")

    division=square_matrix_of_2_by_2.division_Of_a_matrix(x,y)
    print(f"Division of a matirx  :   {division}")

    scalar_m1=square_matrix_of_2_by_2.scalar_matrix_of_two_matrices(3,x)
    scalar_m2=square_matrix_of_2_by_2.scalar_matrix_of_two_matrices(5,y)
    print(f"Scalar Multiple of m1 :   {scalar_m1}")
    print(f"Scalar Multiple of m2 :   {scalar_m2}")

    cofactor_m1=square_matrix_of_2_by_2.cofactor_of_a_matrix(x)
    cofactor_m2=square_matrix_of_2_by_2.cofactor_of_a_matrix(y)
    print(f"Cofacotor of a matrix m1 :   {cofactor_m1}")
    print(f"Cofacotor of a matrix m2 :   {cofactor_m2}")
    
main()
