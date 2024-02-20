# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1953587
# Date: 12/12/2022

#user defined function
def Credits(Pass,Defer,Fail):
    if Pass + Defer + Fail == 120:
        PASS.append(Pass)
        DEFER.append(Defer)
        FAIL.append(Fail)
        
        if Pass == 120 and Defer == 0 and Fail == 0:
            print("Progress")
            Progress.append("*")

        elif Pass == 100 and (Defer in(20,0)) and (Fail in(0, 20)):
            print("Progress(Module Trailer)")
            Trailer.append("*")

        elif (Pass in (0, 20, 40, 60, 80)) and (Fail in(0, 20, 40, 60)):
            print("Do not progress-module retriever")
            Retriever.append("*")

        elif (Pass in(40, 20, 0)) and (Defer in (0, 20, 40)) and (Fail in(80, 100, 120)):
            print("Exclude")
            Exclude.append("*")

    else :
        print("Total Incorrect")

#creating descriptive names for variables
Progress = []
Trailer = []
Retriever = []
Exclude = []
Pass = int()
Defer = int()
Fail = int()

PASS=[]
DEFER=[]
FAIL=[]

print()
print("__________Staff Portal___________")
while True:
    
    try:
        print()
        #getting inputs
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
        Credits(Pass,Defer,Fail) 

    
        #asking to quit or continue and creating histogram
        print()
        print("Would you like to enter another set of data?")
        change = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        if change == "y":
            continue 

        elif change == "q":
            print()
            print("--" * 30)
            print("_________LIST_________")
            print()

            
            for i in range(len(PASS)):# creating list
                 if PASS[i] == 120:
                    print("Progress","-", PASS[i], ",", DEFER[i], ",", FAIL[i])
                 elif PASS[i] == 100 and (DEFER[i] in (20, 0)) and (FAIL[i] in (0, 20)):
                    print("Progress (moduletrailer)","-", PASS[i], ",", DEFER[i], ",", FAIL[i])
                 elif (PASS[i] in (80, 60, 40, 0, 20)) and (DEFER[i] in (40, 20, 0, 60, 80, 100, 120)) and (
                        FAIL[i] in (0, 20, 40, 60)):
                    print("Module retriever","-", PASS[i], ",", DEFER[i], ",", FAIL[i])
                 elif (PASS[i] in (40, 20, 0)) and (DEFER[i] in (0, 20, 40)) and (FAIL[i] in (80, 100, 120)):
                    print("Exclude","-", PASS[i], ",", DEFER[i], ",", FAIL[i])
        else:  #Error popup for INVALID CONDITION
            print("Invalid, check your condition")
            break
        break
    except ValueError:
        print("Integer required")
        
