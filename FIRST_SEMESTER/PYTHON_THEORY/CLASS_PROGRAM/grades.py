#write a python script to process 3 students detail roll-no, 3 subject marks,
#to calculate avg ,percentage and display grades based on percentage = 
#[60-75 % first class] above 75% display distinction below 60% 2nd class and below 35% will be treated as fail

#global variable [accessed by every method]
#local variable [declare inside the method]

roll_no= 0
name = ''
sub_one , sub_two, sub_three= 0,0,0


#function to read data
def read_data():
    global sub_one,sub_two,sub_three,name,roll_no
    name= input("enter your name: ")
    # reads thee 'str' type data from keyboard
    sub_one=input("enter marks: ")
    #converts to int
    sub_one= int(sub_one)

    sub_two=input("enter marks: ")
    #converts to int
    sub_two= int(sub_two)

    sub_three=input("enter marks: ")
    #converts to int
    sub_three= int(sub_three)

    #returns multiple values
    return roll_no,name,sub_one,sub_two,sub_three



    pass

    
def get_total():
    pass

def get_average():
    pass

def find_grade():
    pass

def display_result():
    pass




