file=open("file.txt", "r")
data=file.read()
print(data)
file.close()                        #file ko last me close krna ek ache coder ki pehchan hoti hai


# READING FILE
# USING WITH

with open("file.txt","r") as f:       #ispe f ko close ni krna padega kyuki ff ke lea hum with lga rhe hai ye apne aap hi close kr dega
    data=f.read()
    print(data)


# READ LINE BY LINE
with open("file.txt","r") as f:
    line1=f.readline()
    line2=f.readline()
    print(line1)
    print(line2)                       #ispe jitni line padni  hai utne code likhna, har line ke lea ek new code
    data=f.read()
    print(data)                        #ispe empty dikhayega kyuki pointer to already un dono line ko show krne ke bad niche empty wale line pe jaa chuka hai


# READ ALL LINES
with open("file.txt","r") as f:
    lines=f.readlines()
    print(lines)                           #ispe sari lines ek sath print ho jayegi list of string ke formate mein
 
# TO FIND KI KITNE LINE KA CODE THA 
with open("file.txt","r") as f:
    lines=f.readlines()
    print(len(lines))


# WRITING ON FILE
with open("file.text","w") as f:
    f.write("ispe apna code likh do, lekin yad rakhna purana lihe hue ko ye override kr dega")


# APPEND METHOD
with open("file.txt","a") as f:                #iske output direct file.txt pe dekhna
    f.write("purane wale ko override ni karega\n niche likhega ye code")




f=open("badri.txt","r")
line = f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()

'''high score calcualate krna hai using function and hiscore.txt file'''
'''ye mera logic hai'''
def game():
    score = int(input("enter the number:"))

    with open("hicore.txt","a") as f:
        hiscore=f.read()
        hiscore=int(hiscore)
        if(hiscore==0):
            return f"your high score is:{score}"

        if(hiscore==""):
            return f"your high score is:{score}"
         
        if(score>hiscore):
             return f"your high score is:{score}"
        hiscore=f.append(score)


    return f"your high score is:{score}"

# game()"'''ye harry ka logic hai '''
import random
def game():
    print('you are playing the game')
    score = random.randint(1,69)
    #fetch the hiscore file
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore!=""):
            hiscore=int(hiscore)
        else:

            hiscore=0
    print(f"your high score,{score}")
        

'''ek folder m aalag alag file m table bnani hai'''

def generate_table(n):
    table=""
    for i in range(1,11):
        table+=f"{n}x{i}={n*i}\n"

    with open(f"table/table_{n}","w") as f:   #ispe table nam ka folder khud se bna 
        f.write(table)

for i in range(2,21):
    generate_table(i)

'''replace krna hai apne file ke words ko new words se:
and file handaling ke concept smjhne ke lea kafi acha hai'''

word="priyanshu"

with open("file.txt") as f:
    content = f.read()
  
newcontent = content.replace(word, "badri")

with open("file.txt","w") as f:
    f.write(newcontent)


'''humko pta krna hai ki python us file pe hai ki ni or agr hai too konsi line pe hai'''
with open("file.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"python is present in the the line:{lineno}")
        break
    lineno+=1

else:
    print("python is not present")

