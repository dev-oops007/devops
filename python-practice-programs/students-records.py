#Students Results record : Total , Percentage, Grade
#when
#total Marks are defined (it should be dynamic according to subject) 

def percentage(a,b,c):
    
    subT = a + b + c 
    perc = subT/300 *100
    perc = round(perc, 2) #rounded the percentage upto 2 digit after decimel 
    
    # grade system according to percentage
    if perc>=30 and perc<35: 
        grade = 'Pass with Grace'
    elif perc>=35 and perc<45:
        grade = 'Grade E'
    elif perc>=45 and perc<60:
        grade = 'Grade D'
    elif perc>=60 and perc<75:
        grade = 'Grade C'
    elif perc>=75 and perc<90:
        grade = 'Grade B'
    elif perc>=90 and perc<=100:
        grade = 'Grade A'
    else:
        grade = 'Fail'
    
    return subT, perc, grade 

num = int(input('How many students in class : '))
studentsRecord = {'fields':['English', 'Math', 'Science', 'Subtotal', 'Percentage', 'Grade']}


for i in range(1,num+1):
    
    student= input(f'enter student {i} name : ').capitalize()
    studentsRecord[student]=[]
    
    #input student subject marks 
    count=0 
    
    #English marks 
    while count<=10:
        if count==10:
                print('Reached Maximum Tries')
                break
        try:
            #exception handling for marks datatype
            eng = input(f'Enter {student} English Marks from 100 : ')
            eng = int(eng)
            break         
        except:
            print('Not Valid datatype\n Please enter integer value')
            count+=1
    
    #Math marks
    while count<=10:
        
        if count==10:
                print('Reached Maximum Tries')
                break
        try: 
            math =  input(f'Enter {student} Math Marks from 100 : ')
            math = int(math)
            break         
        except:
            print('Not Valid datatype\n Please enter integer value')
            count+=1
    
    #Science marks
    while count<=10:
        if count==10:
                print('Reached Maximum Tries')
                break
        try: 
            sci =  input(f'Enter {student} Science Marks from 100 : ')
            sci = int(sci)
            break         
        except:
            print('Not Valid datatype\n Please enter integer value')
            count+=1
    
    if student in studentsRecord:
        
        studentsRecord[student].append(eng)
        studentsRecord[student].append(math)        
        studentsRecord[student].append(sci)
        
        subT, perc, grade = percentage(eng,math,sci)
        studentsRecord[student].append(subT) #append students subtotatal of marks
        studentsRecord[student].append(perc) # append the overall percentage 
        studentsRecord[student].append(grade) #append overall grade on basis of percentage


