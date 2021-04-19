def add_time(start, duration):
    hour_1=[]
    minute_1=[]
    a=start.split(':')
    hour_1.append(int(a[0]))
    a=a[1].split(' ')
    minute_1.append(int(a[0]))
    time_domain=[]
    time_domain.append(a[1])
    hour_1.append(duration.split(':')[0])
    minute_1.append(duration.split(':')[1])
    days=int(hour_1[1])//24
    hours_left=int(hour_1[1])-24*days
    actual_hours=int(hour_1[0])+hours_left
    actual_minutes=int(minute_1[0])+int(minute_1[1])
    if(actual_minutes>=60):
        actual_hours+=1
        actual_minutes-=60
    if(actual_hours<=12):
        if(actual_hours<12 and actual_hours!=0):
            new_time=str(actual_hours)+":"
            if(actual_minutes<10):
                new_time+="0"+str(actual_minutes)+" "+time_domain[0]
            else:
                new_time+=str(actual_minutes)+" "+time_domain[0]
        elif(actual_hours==0):
            actual_hour+=12
            new_time=str(actual_hours)+":"
            if(actual_minutes<10):
                new_time+="0"+str(actual_minutes)+" "+time_domain[0]
            else:
                new_time+=str(actual_minutes)+" "+time_domain[0]
        else:
            new_time=str(actual_hours)+":"
            if(actual_minutes<10):
                new_time+="0"+str(actual_minutes)
            else:
                new_time+=str(actual_minutes)
            if(time_domain[0]=="PM"):
                new_time+=" "+"AM"
            else:
                new_time+=" "+"PM"
    elif(actual_hours>12 and actual_hours<24):
        actual_hours-=12
        if(actual_minutes>=10):
            new_time=str(actual_hours)+":"+str(actual_minutes)+" "
        else:
            new_time=str(actual_hours)+":"+"0"+str(actual_minutes)+" "
        if(time_domain[0]=="PM"):
            new_time+="AM"
        else:
            new_time+="PM"
    else:
        actual_hours-=24
        if(actual_minutes>=10):
            new_time=str(actual_hours)+":"+str(actual_minutes)+" "+time_domain[0]
        else:
            new_time=str(actual_hours)+":"+"0"+str(actual_minutes)+" "+time_domain[0]
    if(default!="1"):
        days_list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        day_no=0
        for string in days_list:
            count=0
            if(default.capitalize()==string):
                break
            else:
                day_no+=1
    if(time_domain[0]=="PM"):
        hours_added=int(hour_1[0])+int(hour_1[1])+12
    else:
        if(hour_1[0]=="12"):
            hour_1[0]="0"
        hours_added=int(hour_1[0])+int(hour_1[1])
    minutes_added=int(minute_1[0])+int(minute_1[1])
    if(minutes_added>=60):
        hours_added+=1
    days=hours_added//24
    if(default=="1"):
        if(days>=1):
            if(days==1):
                new_time+=" "+"(next day)"
            else:
                new_time+=" "+"("+str(days)+" "+"days"+" later)"
    else:
        if(days<1):
            new_time+=","+" "+string
        elif(days==1):
            new_time+=", "+days_list[(day_no+1)%7].capitalize()+" "+"(next day)"
        else:
            new_time+=", "+days_list[(day_no+days)%7].capitalize()+" "+"("+str(days)+" days later)"
            
    



    return new_time
