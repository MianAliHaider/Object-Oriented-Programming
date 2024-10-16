class Numbers:
    def __init__(self):
        self.numbers_list = []
        self.odd_number_list = []
        self.even_number_list = []

    def add_number(self, number):
        self.numbers_list.append(number)
        if number % 2 == 0:
            self.even_number_list.append(number)
        else:
            self.odd_number_list.append(number)

    def delete_number(self, number):
        if number in self.numbers_list:
            self.numbers_list.remove(number)
            if number % 2 == 0:
                self.even_number_list.remove(number)
            else:
                self.odd_number_list.remove(number)
        else:
            print(f"Number {number} is not found in the list.")

    def search_number(self, number):
        return number in self.numbers_list

    def alter_number(self,old_number,new_number):
        if old_number in self.numbers_list:
            self.delete_number(old_number)
            self.add_number(new_number)
        else:
            print(f"Number {old_number} not found in the list.")

    def __next__(self):
        if self.current_index < len(self.numbers):
            result = self.numbers[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return iter(self.numbers)

    def __getitem__(self, index):
        return self.numbers[index]

def main():
    number_list = Numbers()
    number_list.add_number(8)
    number_list.add_number(5)
    number_list.add_number(2.7)
    print("[",end="")
    for i,num in enumerate(number_list.numbers_list):
        print(num,end=" ")
        if i < len(number_list.numbers_list) - 1:
            print(", ", end="")
    print("]")

    print(f"All odd numbers in the list: {number_list.odd_number_list}")
    print(f"All even numbers in the list: {number_list.even_number_list}")

    number_list.alter_number(5, 10)
    print("All Numbers after altering 5 with 10:",(number_list.numbers_list))

    print(f"Number is present in the list? {number_list.search_number(8)}")
    number_list.delete_number(5)
    print(f"After delteing 5 from the list {number_list.numbers_list}")

    print("The total list element is ",end="")
    print("[",end="")
    for i, number in enumerate(number_list.numbers_list):
        print(number,end="")
        if i < len(number_list.numbers_list) - 1:
            print(", ", end="")
    print("]")

if __name__ == "__main__":
    main()
