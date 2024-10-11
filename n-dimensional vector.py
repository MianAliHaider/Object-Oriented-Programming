import math

class N_Dimensional_Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return (f"N-Dimensional Vector{self.components}")

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        components = list(self.components)
        components[index] = value
        self.components = tuple(components)


    def __eq__(self, other):
        return self.components == other.components

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return N_Dimensional_Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return N_Dimensional_Vector(*(x - y for x, y in zip(self.components, other.components)))

    def __mul__(self, scalar):
        return N_Dimensional_Vector(*(x * scalar for x in self.components))

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def dot_product(*vectors):
        if not all(len(v) == len(vectors[0]) for v in vectors):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        if len(vectors) < 2:
            raise ValueError("At least two vectors are required for dot product.")
        result = vectors[0]
        for vector in vectors[1:]:
            result = [x * y for x, y in zip(result, vector)]
        return sum(result)
    
    def __neg__(self):
        return N_Dimensional_Vector(*(-x for x in self.components))

    def __iter__(self):
        return iter(self.components)
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        return self.magnitude() <= other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def __ne__(self, other):
        return not self == other

def main():
    v1 = N_Dimensional_Vector(89, 28, 32, 92, 81, 94)
    v2 = N_Dimensional_Vector(4, 5, 19, 10, 11, 12)
    v3 = N_Dimensional_Vector(13, 85, 65, 25, 22, 50)
    v4 = N_Dimensional_Vector(22, 1, 63, 10, 10, 92)
    v5 = N_Dimensional_Vector(96, 22, 2, 8, 29, 44)
    v6 = N_Dimensional_Vector(74, 15, 19, 10, 11, 12)

    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector 3:", v3)
    print("Vector 4:", v4)
    print("Vector 5:", v5)
    print("Vector 6:", v6)
    print("Magnitude of Vector 1:", round(v1.magnitude()))
    print("Magnitude of Vector 2:", round(v2.magnitude()))
    print("Magnitude of Vector 3:", round(v3.magnitude()))
    print("Magnitude of Vector 4:", round(v4.magnitude()))
    print("Magnitude of Vector 5:", round(v5.magnitude()))
    print("Magnitude of Vector 6:", round(v6.magnitude()))
    print("Dot Product of Vector (1,2,3,4,5,6):",N_Dimensional_Vector.dot_product(v1,v2,v3,v4,v5,v6))
    print("Sum of Vector (1,2,3,4,5,6):", v1 + v2 + v3 + v4 + v5 + v6)
    print("Difference of Vector (1,2,3,4,5,6):", v1 - v2 - v3 - v4 - v5 - v6)
    print("Vector 1 multiplied by 5:", v1 * 5)
    print("Negation of Vector 2:", -v2)
    print("Is Vector 3 less than Vector 4? {v3 < v4}")
    print("Is Vector 5 greater than or equal to Vector 6? {v5 >= v6}")

if __name__=="__main__":
    main()
