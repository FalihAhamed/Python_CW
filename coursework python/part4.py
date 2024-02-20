# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1953587
# Date: 12/12/2022

#user defined function
def Credits(Pass,Defer,Fail,dict1):
    if Pass + Defer + Fail == 120:
        
        
        if Pass == 120 and Defer == 0 and Fail == 0:
            pro = 'progress'
            print(pro)
            Progress.append("*")

        elif Pass == 100 and (Defer in(20,0)) and (Fail in(0, 20)):
            pro = 'Progress(Module Trailer)'
            print(pro)
            Trailer.append("*")

        elif (Pass in (0, 20, 40, 60, 80)) and (Fail in(0, 20, 40, 60)):
            pro = 'Do not progress-module retriever'
            print(pro)
            Retriever.append("*")

        elif (Pass in(40, 20, 0)) and (Defer in (0, 20, 40)) and (Fail in(80, 100, 120)):
            pro = 'Exclude'
            print(pro)
            Exclude.append("*")

    else :
        print("Total Incorrect")
    
    dict1[user_id]=[pro,Pass,Defer,Fail]
    
#creating descriptive names for variables
Progress = []
Trailer = []
Retriever = []
Exclude = []
Pass = int()
Defer = int()
Fail = int()
pro = str()
dict1={}


#looping the program to allow a staff member to predict progression outcomes for
#multiple students

print()
print("__________Staff Portal___________")

while True:
    digit_count=0
    try:
        while True:
            print()
            user_id=input("Enter your student ID:")
            if user_id[0] == 'w':
                if len(user_id)== 8:
                    break
                else:
                    print("Invalid UserID")
                    continue
            else:
                print("Invalid UserID")
                continue
                
               
                            
        
        
        while True:
            try:
                #getting inputs
                Pass = int(input("Please enter your credits at pass: "))  
                if Pass in (0,20,40,60,80,100,120):
                    break
                else:
                    print("Out of range")
                        
            except ValueError:
                print("Integer required")
                    
        while True:
            try:
                Defer = int(input("Please enter your credits at defer: "))
                if Defer in (0,20,40,60,80,100,120):
                    break
                else:
                    print("Out of range")
                        
            except ValueError:
                print("Integer required")
                    
        while True:
            try:
                Fail = int(input("Please enter your credits at fail: "))
                if Fail in (0,20,40,60,80,100,120):
                    break
                else:
                    print("Out of range")
                        
            except ValueError:
                print("Integer required")
                    
        #call for def fuction
        Credits(Pass,Defer,Fail,dict1)
            

            

    #asking to quit or continue and creating histogram
        print()
        print("Would you like to enter another set of data?")
        change = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        if change == "y":
            continue 

        elif change == "q":
            break
    except ValueError:
        print('Eneter Integer')
print("--" * 30)        
print()
print("Dictionary")
print()
for key in dict1:
    print(key,'\t:',dict1[key][0],"-",dict1[key][1],",",dict1[key][2],",",dict1[key][3])
print()
print("--" * 30)
