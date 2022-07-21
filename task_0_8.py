def convert(sec):
    hour = sec // 60
    sec %= 60 
    minutes = sec 
    if(hour==1 and minutes==1):
        print(f"{hour} hour,{minutes} minute")
    elif(hour==1 and minutes>1):
        print(f"{hour} hour, {minutes} minutes")
    elif(hour >2 and minutes ==1):
        print(f"{hour} hours, {minutes} minute")
    elif(hour<2 and minutes==1):
        print(f"{hour} hour,{minutes} minute")
    else:    
        print(f"{hour} hours, {minutes} minutes")
         
    
sec = 71
convert(sec)
