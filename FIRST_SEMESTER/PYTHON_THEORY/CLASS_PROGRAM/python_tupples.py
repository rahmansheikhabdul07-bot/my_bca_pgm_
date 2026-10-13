#write a python program , process single student data
#1.name  2.roll_no  3.phone_no  4.email_id    5.five_sub_mark   6.sub_total
#implement using nested list
#later update to process 'n' number of student
#input shoud recieve using kea_board


name =int(input("enter student name:") )
roll_no =int(input("enter roll_no: "))
phone_no =int(input("enter phone.no: "))
email =int(("enter email_id:"))
sub_1 = float(input("enter your engish mark: "))
sub_2 = float(input("enter your hindi mark: "))
sub_3 = float(input("enter your social mark: "))
sub_4 = float(input("enter your science mark: "))
sub_5 = float(input("enter maths marks: "))
sum ,sub_total= [sub_1 + sub_2 + sub_3 + sub_4 + sub_5]
student_data=["name",roll_no,phone_no,"email",sub_total]

print(name)
print(roll_no)
print(phone_no)
print(email)
print(sub_total)

