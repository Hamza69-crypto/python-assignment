
def add (a,b):
    return a+b
name=input("Enter Your Name: ")
roll=int(input("Enter your Roll NO: "))

low=3
mid=4
high=5
total_marks=0
subject={}
subject=int(input("HOW MANY SUBJECTV YOU WANT TO BE CALCULATED: "))

if subject in [low,mid,high]:
     for i in range(subject):
         subject_name=input(f"ENTER YOUR SUBJECT NAME {i+1}: ")
         marks=int(input(f"ENTER YOUr MARKS IN {subject_name}: "))
         subject[subject_name]=marks
         total_marks=add(total_marks,marks)
         
         
         
         
         average=total_marks/subject
         Percentage=(total_marks/(subject*100))*100
         
         
         print(f"\n HERE IS THE TOTAL MARKS {total_marks}")
         print(f"AVERAGE: {average}")
         print(f"PERCENTAGE: {Percentage}")