timenow=float(input("What time is it now 0-24"))
hourswait=float(input("How many hours are you waiting?"))
                      
alarmtime = hourswait % 24 + timenow

if alarmtime > 24:
    alarmtime = alarmtime % 24
    print("your alarm will go off at ", alarmtime)
else:
    print("your alarm will go off at ", alarmtime)
    #else print("your alarm will go off at ", alarmtime)
