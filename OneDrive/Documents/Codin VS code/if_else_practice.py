marks1 = int (input ("Enter the Marks1 :"))
marks2 = int (input ("Enter the Marks2 :"))
marks3 = int (input ("Enter the Marks3 :"))
marks4 = int (input ("Enter the Marks4 :"))
marks5 = int (input ("Enter the Marks5 :"))
total = marks1+marks2+marks3+marks4+marks5
percent = (total/500)*100
print ("The percentage of Five Marks is ", percent)
if (marks1>33 and marks2>33  and marks3>33  and marks4>33  and marks5>33  and percent >40):
 print('''Yes You are Passed. Congratulation
you are passed with percentage of ''', percent)

else :
 print("OOPS You are FAILED Sorry")