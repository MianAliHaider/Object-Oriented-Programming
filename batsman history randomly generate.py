from random import*
class Batsman:
    __name = None
    __country = None
    __score = []
    
    @property
    def name (self):
        return self.__name
    name.setter
    def name (self,n):
        self.__name = n

    @property
    def country (self):
        return self.__country
    country.setter
    def country (self,n):
        self.__country = n

    @property
    def score (self):
        return self.__score
    score.setter
    def score (self,n):
        self.__score = n
        
    def __init__(self,no_of_matches = None):
        self.__no_of_matches = no_of_matches
        if self.__no_of_matches  is None:
            self.__no_of_matches = randint(1,95)
            self.__randomScores(no_of_matches)
        else:
            self.__randomScores(no_of_matches)

    def __randomScores (self,no_of_matches):
        
        number = randint(0,10)
        for i in range (no_of_matches):
            if number <= 7:
                self.__score.append(randint(0,180))
            elif number >=7 and number <=9:
                self.__score.append(randint(181,350))
            else:
                self.__score.append(randint(351,500))

    def calcTotal(self):
        sum = 0
        for i in range(len(self.__score)):
            sum = sum + self.__score[i]
        return sum

    def calcAverage(self):
        x = self.calcTotal()
        y = len(self.__score)
        average = x/y
        return average

    def findMaxScore(self):
        max = 0
        for i in range(len(self.__score)):
            if self.__score[i] > max:
                max = self.__score[i]

        return max
    def count_50(self):
        count = 0
        for i in range(len(self.__score)):
            if self.__score[i] > 50 and self.__score[i] < 100:
                count = count + 1
        return count
    def count_100(self):
        count = 0
        for i in range(len(self.__score)):
            if self.__score[i] >= 100:
                count = count + 1
        return count

    def show (self):
        x= ""
        print("No of Matches",self.__no_of_matches)
        for i in range(len(self.__score)):
            x = x + str (self.__score[i])
            x += " "
        print("Score ", x)    
    

b = Batsman(5)
b.show()
print("Total: ",b.calcTotal())
print("Average: ",b.calcAverage())
print("Maximum Score: ",b.findMaxScore())
print("Total 50: ",b.count_50())
print("Total 100: ",b.count_100())
  

    
