time_all = {}
ded_all = {}
def mul(a,b):
    global ded_all
    ded_all = {}
    ded_all["s"] = a["s"] * b["s"]
    ded_all["m"] = a["m"] * b["m"]

def sum_ded(a , b):
    global ded_all
    ded_all = {}
    ded_all["s"] = (a["s"]) * b["m"] + (b["s"] * a["m"])
    ded_all["m"] = a["m"] * b["m"]

def minu_ded(a ,b):
    global ded_all
    ded_all = {}
    ded_all["s"] = (a["s"]) * b["m"] - (b["s"] * a["m"])
    ded_all["m"] = a["m"] * b["m"]

def div(a , b):
    global ded_all
    ded_all = {}
    ded_all["s"] = a["s"] * b["m"]
    ded_all["m"] = b["s"] * a["m"]


def sum_time(a = None , b = None):
    global time_all
    time_all = {}
    time_all["h"] = a["h"] + b["h"]
    time_all["m"] = a["m"] + b["m"]
    time_all["s"] = a["s"] + b["s"]
    while True :
        if time_all["s"] >= 60 :
            time_all["s"] -= 60
            time_all["m"] += 1
        else : break
    while True :
        if time_all["m"] >= 60 :
            time_all["m"] -= 60
            time_all["h"] += 1
        else : break

def minu_time(a = None , b = None):
    global time_all
    time_all = {}
    time_all["h"] = a["h"] - b["h"]
    time_all["m"] = a["m"] - b["m"]
    time_all["s"] = a["s"] - b["s"]
    while True :
        if time_all["s"] < 0:
            time_all["s"] += 60
            time_all["m"] -= 1
        else :break
    while True :
        if time_all["m"] < 0 :
            time_all["m"] += 60
            time_all["h"] -= 1
        else : break

while True:
    print("\n1_ Deduction")
    print("2_ Time")
    print("0_ Exit")
    op = int(input("- "))
    if op == 0 :
        break
    elif op == 1 :
        while True :
            ded1 = int(input("\nEnter Deduction 1 : "))
            ded2 = int(input("Enter Deduction 1 : "))
            ded3 = int(input("\nEnter Deduction 2 : "))
            ded4 = int(input("Enter Deduction 2 : "))
            a = {"s":ded1, "m":ded2}
            b = {"s":ded3, "m":ded4}

            sum_ded(a , b)
            print("\nsum : ")
            print(str(ded_all["s"])+" / "+str(ded_all["m"]))
            mul(a , b)
            print("\nmul : ")
            print(str(ded_all["s"])+" / "+str(ded_all["m"]))
            minu_ded(a , b)
            print("\nminu: ")
            print(str(ded_all["s"])+" / "+str(ded_all["m"]))
            div(a ,b)
            print("\ndiv: ")
            print(str(ded_all["s"])+" / "+str(ded_all["m"]))

            if input("\ncontinue ? y|n _ ").strip().lower() == "n" :
                break

            
    elif op == 2 :
        while True :
            t1_h = int(input("\nEnter hour time 1   : ").strip())
            t1_m = int(input("Enter minute time 1 : ").strip())
            t1_s = int(input("Enter Second time 1 : ").strip())
            t2_h = int(input("\nEnter hour time 2 : ").strip())
            t2_m = int(input("Enter minute time 2 : ").strip())
            t2_s = int(input("Enter Second time 2 : ").strip())
            
            print("\n"+str(t1_h)+" : "+str(t1_m)+" : "+str(t1_s))
            print(str(t2_h)+" : "+str(t2_m)+" : "+str(t2_s))

            ta1 = {"h":t1_h, "m":t1_m, "s":t1_s}
            ta2 = {"h":t2_h, "m":t2_m, "s":t2_s}
            print("\nsum : ")
            sum_time(ta1, ta2)
            print(str(time_all["h"])+" : "+str(time_all["m"])+" : "+str(time_all["s"]))
            print("\nminu: ")
            minu_time(ta1, ta2)
            print(str(time_all["h"])+" : "+str(time_all["m"])+" : "+str(time_all["s"]))
            
                
            
            if input("\ncontinue ? y|n _ ").strip().lower() == "n" :
                break