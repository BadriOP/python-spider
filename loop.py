# write a program to print 1 to 10  using while loop
# while loop:
i=1
while i<=10:
    print(i)
    i=i+1

# opposite direction m krna hai ab
i=10
while i>=0:
    print(i)
    i=i-1

# all even number between 1 to 50
i=1
while i<=50:
    if i%2==0:
        print(i)
    i=i+1


# write a program to print too print first sum natural number.
# for ex n=3 output=1+2+3=6
n=int(input("enter the number:"))
sum=0
while n>=1:
    sum=sum+n
    
    n=n-1
print(sum)



# pattern printing wahi star wala
n=int(input("enter the number:"))
i=1
while i<=n:
    print("*" * i)
    i=i+1


# want to print name five times but each name should associate with number , so now write a code for it
name=input("enter your name:")
i=1
while i<=5:
    print(i,name)
    i=i+1



# write a program too print the table of any number
n=int(input("enter any number you want to print table of:"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i=i+1





# for loop pe aa jao ab
item=["mango", "pizza","orange"]
for i in item:
    print("badri want to eat:",i)


# for loop with range
for i in range(1,6,1):                                       #agr range(6) bhi likh dega too bhi same result print hoga bss start 0 se hoga
    print(i)


#nested loop
for i in range(4):
    for j in range(1,4):
        print(i,j)


# pattern printing using for loop
for i in range(1,4):
    print("*"*i)

l = ["harry","badri","priyanshu","prakriti"]

for name in l:
    if name.startswith("p"):
        print(f"hellow {name}")



'''multiplication table using for loop''' 
n=int(input("enter the number:"))
for i in range (11):
    print(f"{n}x{i}={n*i}")
    i+=1


'''multiplication table using while loop'''
n=int(input("enter the number:"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1


"""to find wheather a number is prime or not """
n=int(input("enter the number:"))
for i in range (2,n):
    if (n%i)==0:
        print("The number is not prime:")
        break
else:
    print("This number is prime")


'''sum of natural number using while loop'''
n=int(input("enter the number:"))   
i=1
m=0
while i<=n:
    m+=i
    i+=1

print("sum of n natural number is:",m)


'''factorial using for loop'''

n=int(input("enter the number:")) 

m=1
for i in range(1,n+1):

    m*=i
print("factorial of the number is:",m)


'''star pattern'''
n=int(input("enter the number:")) 

for i in range(1,n+1,2):
    print('x'*i)


'''
  *
 ***
*****
ye pattern banana hai
'''

n=int(input("enter the number:")) 
for i in range(1,n+1):
    print(" "*(n-i), end="")  #ye end ek tarike hota h isse next line pe print ni hota hai
    print("*"*(2*i-1), end="") #print automatically new line pe chala jata hai lein ye dono line ek sath print hongi
    print("")


