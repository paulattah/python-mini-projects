print("welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! Lets play :)") 
score =0

answer  = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print ("correct")
    score += 1
else:
    print ("incorrec!")


answer  = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print ("correct")
    score += 1
else:
    print ("incorrec!")

answer  = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print ("correct")
    score += 1
else:
    print ("incorrec!")


answer  = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print ("correct")
    score += 1
else:
    print ("incorrec!")


print("You got " + str(score) + " questions corret!")

print("You got " + str((score / 4 ) * 100) + " %")