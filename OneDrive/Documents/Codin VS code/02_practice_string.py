letter = '''Dear **<NAME>** 
According to your roll number and you are the luckiest
person in today's Interview
and Hope you feel good as
You are Selected as a Winner
We hope you for your bright future ahead.
Congratulation The KING **********
     *** Date: <DATE> ***   ''' 
name =input("Enter your name\n")
date = input ("Enter Date: \n")
letter=letter.replace("<NAME>", name)
letter= letter.replace("<DATE>", date)
# print(type(letter))
print(letter)