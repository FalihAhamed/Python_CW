# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1953587
# Date: 12/12/2022

Menu = int(input("For student type '1'and For staff type '2':"))

#user defined function
def Credits(Pass,Defer,Fail):
    if Pass + Defer + Fail == 120:
        
        
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

if Menu == 1: 
 while True: 
    #continuing value error until it gets the correct value
        while True:
            try:
                #getting inputs from students
                Pass = int(input("Please enter your credits at Pass: "))  
                if  Pass in(0,20,40,60,80,100,120):
                     break
                else:
                    print("Out of range")
            except ValueError:
                 print("Integer required")
        while True:
            try:
                Defer = int(input("Please enter your credits at Defer: "))
                if Defer in (0,20,40,60,80,100,120):
                     break
                else:
                    print("Out of range")
            except ValueError:
                 print("Integer required")
        while True:
            try:
                Fail = int(input("Please enter your credits at Fail: "))
                if  Fail in (0,20,40,60,80,100,120):
                     break
                else:
                    print("Out of range")
            except ValueError:
                 print("Integer required")    
        
        if Pass + Defer + Fail == 120:
        
        #progress conditon
             if Pass == 120 and Defer == 0 and Fail == 0:
                print("Progress")
                break

             elif Pass == 100 and (Defer in(20,0)) and (Fail in(0, 20)):
                print("Progress(Module Trailer)")
                break

             elif (Pass in (0, 20, 40, 60, 80)) and (Fail in(0, 20, 40, 60)):
                print("Do not progress-module retriever")
                break

             elif (Pass in(40, 20, 0)) and (Defer in (0, 20, 40)) and (Fail in(80, 100, 120)):
                print("Exclude")
                break

        else :
           print("Total Incorrect")

    
        

#looping the program to allow a staff member to predict progression outcomes for
#multiple students

elif Menu == 2:
     print()
     print("__________Staff Portal___________")
     while True:
            print()
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
                print()
                print("--" * 40)
                print("Histogram")
                print()
                print()

                #creating histogram
                if len(Progress) > 0:
                    print("Progress", len(Progress), "\t:", len(Progress) * "*")
                if len(Trailer) > 0:
                    print("Trailer", len(Trailer), "\t:", len(Trailer) * "*")
                if len(Retriever) > 0:
                    print("Retriever", len(Retriever), "\t:", len(Retriever) * "*")
                if len(Exclude) > 0:
                    print("Exclude", len(Exclude), "\t:", len(Exclude) * "*")
                total_outcome = len(Progress) + len(Trailer) + len(Retriever) + len(Exclude)
                print()
                print(total_outcome, "outcomes in total")
                break
            
            else:
            #poping error message for invalid value
                print("invalid condition applied")
                break
else:
    print('Invalid Input')
print()
print("--" * 40)
    

                    
