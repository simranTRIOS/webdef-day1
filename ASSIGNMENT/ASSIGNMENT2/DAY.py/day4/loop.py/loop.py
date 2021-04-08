count = 0

while  True :
    if count < 4:
        print("simran")
        count+= 1
        
    else :
        user_ip=input("would youlike to print your name again?")
       
        if user_ip == 'yes':
            count = 0
        else:
         count + = 1
