import pyttsx3
import os
import datetime
import numpy as np

import datetime  

while True:
    
    
    pc_greetings=['how can i help you : ','what is your requirment : ','what can i do for you : ',"ask me anything : "
                  ,"what you want to start : ", "what can i open for you : "]
    v=np.random.randint(0,len(pc_greetings),size=1)
    a=list(v)
    b=a[0]

    print(pc_greetings[b] , end='')
    p = input()

    # print(p)
    # os.system(p)
    if (("donot"in p) or ("dont" in p)) or (("don't" in p) or ("not start" in p)):
        print("ok")
    elif ((("run" in p) or ("execute" in p)) or  (("start" in p) or ("open" in p))) and (("chrome" in p) or ("browser" in p)):
        os.system("start iexplore")
    
    elif ((("today" in p) or ("show" in p)) or  (("what" in p) or ("tell" in p))) or (("time" in p) or ("date" in p)):
        current_time = datetime.datetime.now() 
        print ("current time and date  is : " ,current_time)
        current_time = datetime.datetime.now()
        if current_time.hour < 12:print('Good morning.')
        elif 12 <= current_time.hour < 18:
            print('Good afternoon.')
        else:
            print('Good evening.')

        
    elif ((("run" in p) or ("execute" in p)) or  (("start" in p) or ("open" in p))) and  (("notepad" in p) or ("editor" in p)):
        os.system("notepad")

    elif ((("run" in p) or ("execute" in p)) or  (("start" in p) or ("open" in p))) and ("player" in p) and ("media" in p):
        os.system("wmplayer")
    elif ((("run" in p) or ("execute" in p)) or  (("start" in p) or ("open" in p))) and ((("calci" in p) or ("calculator" in p)) or ("scientific calculator"
                                                                                                           in p) or ("calc" in p)):
        
        os.system("calc")
    
    elif ((("run" in p) or ("execute" in p)) or  (("start" in p) or ("open" in p))) and (("paint" in p) or ("drawing" in p) or ("draw" in p)):
        os.system("mspaint")
        
    elif ((("run" in p) or ("execute" in p)) or  (("start" in p) or ("open" in p))) and ((("this pc" in p) or ("my computer" in p)) or ("explorer" in p)):
        os.system("explorer")
        
        
    elif  ((("exit" in p)  or ("quit" in p)) or (("close" in p) or ("break" in p)) or ("stop" in p)):
        break

    else:
        print("dont support")
