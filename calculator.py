import math

def sqrt_check(s):
    cnt=0
    length=len(s)
    new_s=""
    temp=0
    starting_point_a=-1
    ending_point_a=-1
    
    while cnt<length:
        if s[cnt-2]=='t' and s[cnt-1]=='(':
            temp=1
            starting_point_a=cnt-5
            
        if s[cnt]==')' and temp==1:
            temp=0
            ending_point_a=cnt
            
            #print(new_s)
            
            new_int_sqrt=str(int(math.sqrt(int(new_s)))) 
            
            #print(new_int_sqrt)
            
            cnt2=0
            new_s2=""
            while cnt2<starting_point_a:
                new_s2+=s[cnt2]
                cnt2+=1
            
            new_s2+=str(new_int_sqrt)
            
            cnt2=ending_point_a+1
            while cnt2<length:
                new_s2+=s[cnt2]
                cnt2+=1 
                
            s=new_s2
            cnt=-1 
            length=len(s)
            new_s=""
            #print(s)
        
        if temp==1:
            new_s+=s[cnt]
        cnt+=1
    #print("This is sqrt check function : ",s)
    return s    
    
    
    
####################################

def solve_for_degree(s,pos):
    num=""
    deg=""
    new_s=s
    cnt=pos-1
    #print(s,pos)
    
    starting_point_c=-1
    ending_point_c=-1 
    
    temp=0 
    
    while cnt>=0:
        if new_s[cnt] in ['0','1','2','3','4','5','6','7','8','9']:
            num=new_s[cnt]+num
            cnt-=1
        else:
            starting_point_c=cnt +1 
            temp=1 
            break 
    if temp==0:
        starting_point_c=cnt+1 
    if temp==1:
        temp=0 
        
    cnt=pos+1
    length=len(new_s)
    
    while cnt<length:
        if new_s[cnt] in ['0','1','2','3','4','5','6','7','8','9']:
            deg=deg+new_s[cnt] 
            cnt+=1
        else :
            ending_point_c=cnt -1 
            temp=1 
            break
    if temp == 0:
        ending_point_c=cnt
    
    
    
    deg=str(int(math.pow(int(num),int(deg))))
    
    #print(num,deg)
    
    
    new_string_cc=""
    cnt=0 
    while cnt<starting_point_c:
        new_string_cc+=s[cnt]
        cnt+=1 
        
    #print("deg : ",deg)    
    
    for i in deg:
        new_string_cc+=i 
    
    #print("Before second part added",new_string_cc)
    cnt=ending_point_c+1 
    while cnt<len(s) :
        new_string_cc+=s[cnt]
        cnt+=1 
    
    
    
    
    
    
    
    
    
    
    #print("New string : ",new_string_cc)
    # print("New string : ",deg ) 
    #print("This is solve for degree function : ",s)
    return new_string_cc
    #print(  new_int0 )    
####################################################################
def four_function(a,b,c):
    if c=='/' and b=='0':
        print("In this task detected a division number by 0 which is undefined.\nProgram stopped")
        exit()
    
    if c=='+':
        return int(a)+int(b)
    if c=='-':
        if int(a)<int(b):
            print("Sorry, we have not developed negative calculation yet, try other input\n \n ")
            exit() 
        return int(a)-int(b)
    if c=='*':
        return int(a)*int(b)
    if c=='/':
        return int(int(a)/int(b))
        
####################################################################
def solve_it(s):
    #print(" we are in solve_it function\n\n\n")
    task=s 
    new_str=""
    cnt=0 
    length=len(task)
    while cnt<length:
        #print("Solve it function in while loop 1")
        
        if task[cnt]=='*' or task[cnt]=='/':
            left_part=""
            right_part=""
            temp_pos_left=0
            temp_pos_right=0
            
            temp_cnt=cnt-1
            #print("167 line : temp_cnt:",temp_cnt)
            
            #print("19 line : ", task)
            while temp_cnt>=0:
                if task[temp_cnt] in ['0','1','2','3','4','5','6','7','8','9']:
                    left_part+=task[temp_cnt] 
                else :
                    temp_pos_left=temp_cnt+1
                    #print("in line 173 tempposleft:",temp_pos_left)
                    break 
                temp_cnt-=1 
                
            left_part=left_part[::-1]
            
            #for right part 
            temp_cnt=cnt+1 
            temp_to_stop=0
            while temp_cnt<length:
                #print("Here is while:\n", task[temp_cnt])
                if task[temp_cnt] in ['0','1','2','3','4','5','6','7','8','9']:
                    right_part+=task[temp_cnt]
                else :
                    temp_pos_right=temp_cnt-1 
                    temp_to_stop=1 
                    break 
                temp_cnt+=1 
            
            if temp_to_stop==0:
                temp_pos_right=length
            #print("This is temp pos right ", temp_pos_right)
            
            result01=str(four_function(left_part,right_part,task[cnt])) 
            
            #print("THis is result01 : ",result01)
            
            new_str_01=""
            temp_cnt=0 
            
            #print(temp_cnt,temp_pos_left)
            while temp_cnt<temp_pos_left:
                new_str_01+=task[temp_cnt]
                temp_cnt+=1 
                
            #print("THis is abc : ",new_str_01)
            new_str_01+=str(result01) 
            
            temp_cnt=temp_pos_right+1 
            
            while temp_cnt<length:
                new_str_01+=task[temp_cnt]
                temp_cnt+=1 
            
            #print("New_str_01: ",new_str_01)
            cnt=-1  
            task=new_str_01 
            length=len(task)
        cnt+=1    
    ################
    
    # THis 
    new_str=""
    cnt=0 
    length=len(task)
    while cnt<length:
        #print("Solve it function in while loop 1")
        
        if task[cnt]=='+' or task[cnt]=='-':
            left_part=""
            right_part=""
            temp_pos_left=0
            temp_pos_right=0
            
            temp_cnt=cnt-1
            #print("167 line : temp_cnt:",temp_cnt)
            
            #print("19 line : ", task)
            while temp_cnt>=0:
                if task[temp_cnt] in ['0','1','2','3','4','5','6','7','8','9']:
                    left_part+=task[temp_cnt] 
                else :
                    temp_pos_left=temp_cnt+1
                    #print("in line 173 tempposleft:",temp_pos_left)
                    break 
                temp_cnt-=1 
                
            left_part=left_part[::-1]
            
            #for right part 
            temp_cnt=cnt+1 
            temp_to_stop=0
            while temp_cnt<length:
                #print("Here is while:\n", task[temp_cnt])
                if task[temp_cnt] in ['0','1','2','3','4','5','6','7','8','9']:
                    right_part+=task[temp_cnt]
                else :
                    temp_pos_right=temp_cnt-1 
                    temp_to_stop=1 
                    break 
                temp_cnt+=1 
            
            if temp_to_stop==0:
                temp_pos_right=length
            #print("This is temp pos right ", temp_pos_right)
            
            result01=str(four_function(left_part,right_part,task[cnt])) 
            
            #print("THis is result01 : ",result01)
            
            new_str_01=""
            temp_cnt=0 
            
            #print(temp_cnt,temp_pos_left)
            while temp_cnt<temp_pos_left:
                new_str_01+=task[temp_cnt]
                temp_cnt+=1 
                
            #print("THis is abc : ",new_str_01)
            new_str_01+=str(result01) 
            
            temp_cnt=temp_pos_right+1 
            
            while temp_cnt<length:
                new_str_01+=task[temp_cnt]
                temp_cnt+=1 
            
            #print("New_str_01: ",new_str_01)
            cnt=-1  
            task=new_str_01 
            length=len(task)
        cnt+=1    
    
    
    
    #print("!!!!!!!! This is task var : ",task)
    return task 
    
    
    

####################################################################

def solve_for_bracket(s,pos):
    
 
    
    to_solve_str=""
    cnt=pos-2
    length=len(s)
    
    a_point_bracket=0 
    b_point_bracket=pos 
    
    
    
    while cnt>=0:
        if s[cnt]!='(':
            to_solve_str+=s[cnt]
        else:
            a_point_bracket=cnt
            break 
        cnt-=1 
    to_solve_str=to_solve_str[::-1]
    #print("to_solve_str : ",to_solve_str)
    
    cnt=pos+1
    deg=""
    #print("THis is cnt before",cnt,'\n')
    #print("THis is s before",s,'\n')
    
    temp=-1 
    while cnt<length:
        if s[cnt] in  ['0','1','2','3','4','5','6','7','8','9']:
            deg+=s[cnt] 
        else :
            b_point_bracket=cnt-1 
            temp=1
            break
        cnt+=1 
        
    if temp==-1:
        b_point_bracket=length-1 
        
    #print("This is degree",deg,"\n", "This is to_solve_str : ",to_solve_str)
    print(s,a_point_bracket,b_point_bracket)
    res1=solve_it(to_solve_str)
    result007=str(int(res1)**int(deg ))
    
    
    new_str_bracket=""
    cnt=0 
    while cnt<a_point_bracket:
        new_str_bracket+=s[cnt] 
        cnt+=1 
    new_str_bracket+=result007
    
    cnt=b_point_bracket+1 
    while cnt<length:
        new_str_bracket+=s[cnt] 
        cnt+=1 
        
    #print(s,a_point_bracket,b_point_bracket)
    #print(result007)
    #print(new_str_bracket)
    
    return new_str_bracket
    
    
############################################################

def solve_for_bracket_only(s,pos):
    
 
     
    to_solve_str=""
    cnt=pos-1
    length=len(s)
    
    a_point_bracket=0 
    b_point_bracket=pos 
    
    
    
    while cnt>=0:
        if s[cnt]!='(':
            to_solve_str+=s[cnt]
        else:
            a_point_bracket=cnt
            break 
        cnt-=1 
    to_solve_str=to_solve_str[::-1]
    #print("to_solve_str : ",to_solve_str)
    
    cnt=pos

    #print("THis is cnt before",cnt,'\n')
    #print("THis is s before",s,'\n')
    
    
        
    #print("This is degree",deg,"\n", "This is to_solve_str : ",to_solve_str)
    #print(s,a_point_bracket,b_point_bracket, to_solve_str)
    res1=solve_it(to_solve_str)
    result007=res1 
    
    
    new_str_bracket=""
    cnt=0 
    while cnt<a_point_bracket:
        new_str_bracket+=s[cnt] 
        cnt+=1 
    new_str_bracket+=result007
    
    cnt=b_point_bracket+1 
    while cnt<length:
        new_str_bracket+=s[cnt] 
        cnt+=1 
        
    #print(s,a_point_bracket,b_point_bracket)
    #print(result007)
    #print(new_str_bracket)
    
    return str(new_str_bracket)
    
    

##########################################################
while 2>1:
    www="Please enter a task to solve\n\nNegative calculation have not developed yet !\n\n"
    www+="Examples of input: '10+12' 'sqrt(100)*10' '(99/3)' 'sqrt(100)+(10/2)^2' \n\n"
    www+="addition, substraction small numbers from big numbers, square root calculation, degree - acceptable\n\n"

    s=str(input(www))
    s=sqrt_check(s) 
    cnt=0 
    length=len(s)
    temp0009=0
    s=str(s)
    
    while cnt<length:
        
        if s[cnt]=='^': 
            if s[cnt-1]==')':
                s=solve_for_bracket(s,cnt)
                
                length=len(str(s)) 
                cnt=0
            else :
                s=solve_for_degree(s,cnt)
                length=len(s) 
                cnt=0 
                #print(degree)
                  
        cnt+=1
    
# for simple checking 
#print(s)
    cnt=0 
    length=len(s)
    while cnt<length:
    
        if s[cnt]==')': 
            s=solve_for_bracket_only(s,cnt)
            length=len(s)
            cnt=-1 
        cnt+=1 
#print(s)
    s=solve_it(s) 

    print("The result is :",s,"\nDo you want to continue ? \nType 'y' for yes and 'n' for no\n ")
    cmdd=str(input())
    if cmdd=='n':
        exit()
    print("\n\n")