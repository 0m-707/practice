a = (int(input("enter the amount ")))
if a <= 100000 :
    p = int(input("enter the password"))
    if p == 5333 :
        print (a, "is withdrawn")
    else :
        print ("wrong password")
else:
 print ("amount exceeds balance  ")