age  = int (input ("Enter your Age :\n"))
if (age < 19 or age > 65):
    print("No \n You Can't Drive a Car.")
elif(age >19 and age < 65):
    print("Yes \n You Can Drive a Car. Thanks")
else :
    print("Invalid Age Entered")