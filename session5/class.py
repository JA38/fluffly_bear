class FourCal:
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
        self.add_num = 0
        self.minus_num = 0
        self.div_num = 0
        self.multi_num = 0

    def add(self, n1, n2):
        self.add_num += 1
        result = n1 + n2
        return result
    def minus(self, n1,n2):
        self.minus_num += 1
        result = n1 - n2
        return result
    def div(self,n1,n2):
        self.div_num += 1
        result = n1/n2
        return result
    def multi(self,n1,n2):
        result = n1*n2
        self.multi_num += 1
        return result
    def ShowCount(self):
        print(f'덧셈:{self.add_num}\n뺄셈:{self.minus_num}\n곱셈:{self.multi_num}\n나눗셈:{self.div_num}')


calculator1 = FourCal("유재안",23,'engineering')
print(calculator1.name, calculator1.age, calculator1.school)
print(calculator1.add(100,23))
print(calculator1.add(100,3))
print(calculator1.div(20,3))
print(calculator1.multi(30,2))
calculator1.ShowCount()