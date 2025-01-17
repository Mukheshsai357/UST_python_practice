#Program 1

class Demo:
    value=0
    def __init__(self,*val1):
        self.value=val1
    def Fun(self):
        print(f"The first value is {self.value[0]}")
    def Gun(self):
        print(f"The Second value is {self.value[1]}")
obj=Demo(1,2)
obj2=Demo(3,4)
obj.Fun()
obj.Gun()
obj2.Fun()
obj2.Gun()

#Program 2

class Bookstore():
    No_of_books=0
    def __init__(self,Name,Author):
        self.name=Name
        self.author=Author
        Bookstore.No_of_books+=1
    def display(self):
        print(f"The Name of the book is {self.name}, author is {self.author} and there are {self.__class__.No_of_books} are in our Bookstore")
obj1=Bookstore("Linux System Programming","Robert Love")
obj1.display()
obj2=Bookstore("C programming","Robert Love")
obj2.display()
    
#Program 3

class Circle():
    PI=3.14
    def __init__(self):
        self.radius=0.0
        self.area=0
        self.circumference=0.0
    def Accept(self,radius):
        self.radius=radius
    def CalcaulataArea(self):
        self.area=self.__class__.PI*self.radius*self.radius
    def CalculateCircumference(self):
        self.circumference=2*self.__class__.PI*self.radius
    def Display(self):
        print(f"The radius of the circle is {self.radius},area of the {self.area} and cicremference of the circle is {self.circumference}")
    
obj=Circle()
obj.Accept(5)
obj.CalcaulataArea()
obj.CalculateCircumference()
obj.Display()

#Program 4

class BankAccount():
    ROI=10.5
    def __init__(self,Name,Amount):
        self.name=Name
        self.amount=Amount
    def Deposit(self,amount):
        self.amount+=amount
    def Withdrawl(self,amount):
        if amount<=self.amount:
            self.amount-=amount

        else:
            raise "No Sufficient amount in your BankAccount"
        
    def CalculateInterest(self):
        intrest=(self.amount/self.__class__.ROI)*100-self.amount
        print(f"The intrest would be {intrest}")
    def Display(self):
        print(f"The AccountHolder name is {self.name} and the amount in his bankaccount is {self.amount}")

obj=BankAccount("mukhesh",5000)
obj.Deposit(2000)
obj.Withdrawl(1500)
obj.CalculateInterest()
obj.Display()

#Program 5

class Numbers():
    value=0
    def __init__(self,value):
        Numbers.value=value
    def ChkPrime(self):
        for i in range(2,int(self.value**0.5)+1):
            if self.value%i==0:
                return False
        return True
    def ChkPerfect(self):
        sum_val=1+self.value
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                sum_val+=i
        if(sum_val==self.value):
            return True
        return False
    def Factors(self):
        factors=[1]
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                factors.append(i)
        factors.append(self.value)
        return factors
    def SumOfFactors(self):
        sum_val=1+self.value
        for i in range(2,self.value//2+1):
            if(self.value%i)==0:
                sum_val+=i
        return sum_val
obj=Numbers(6)
print(obj.ChkPerfect())
print(obj.ChkPrime())
print(obj.SumOfFactors())
print(obj.Factors())

#program 6

class Number2():
    def __init__(self):
        self.val1=0
        self.val2=0
    def Accept(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def Addition(self):
        return self.val1+self.val2
    def Subraction(self):
        return self.val1-self.val2
    def Multiplication(self):
        return self.val1*self.val2
    def Division(self):
        return self.val1/self.val2
obj=Number2()
obj.Accept(8,3)
print(obj.Addition())
print(obj.Subraction())
print(obj.Multiplication())
print(obj.Division())
