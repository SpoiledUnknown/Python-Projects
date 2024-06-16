print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()  

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
   
answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    
answer = input("What does NPU stand for? ")
if answer.lower() == "neural processing unit":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    
answer = input("What does Ram stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    
answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    
answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
    
print(f"You got {str(score)} questions correct! that is {str(round((score / 7) * 100))}%")