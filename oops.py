#OOPS IN PYHTON 
class st:
    name="badri"                                #attributes
    branch="cse"                                #attributes
    roll=23                                     #attributes

#creating object
s1=st()
print(s1.roll)
s2=st()
s2.name="priyanshu"                             #ese krke attribute change kr sakta hai
print(s2.name)


# INIT CONSTRUCTOR      automatically call when the object is created
class st:
    def __init__(self,name ,cource):         #isoe self obj(s1 and s2)ko store krta hai
        self.n=name                         #ispe n pe badri and ramesh store kr rha hai
        self.c=cource                       #ispe c pe cource store kr rha hai

s1=st("badri","btech")
print("student name:",s1.n)

s2=st("ramesh","bsc")
print("student name:",s2.c)


#create a class that takes 3 marks and has a method average
class st:
    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1 
        self.mark2=mark2
        self.mark3=mark3
    def avg(self):
        avg=int((mark1+mark2+mark3)/3)
        print("average of the no:",avg)

mark1=int(input("enter the mark1:"))
mark2=int(input("enter the mark2:"))
mark3=int(input("enter the mark3:"))
s1=st("mark1","mark2","mark3")
s1.avg()
