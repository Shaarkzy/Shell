#------------------------------------------------------------------------------------------------------------------------------


from colorama import Fore as F



#------------------------------------------------------------------------------------------------------------------------------


res_val = {
    "black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "gray":8, "white":9
}

#------------------------------------------------------------------------------------------------------------------------------


mul_val = {
    "black":1, "brown":10, "red":100, "orange":1000, "yellow":10000, "green":100000, "blue":1000000, "gold":0.1, "silver":0.01
}

tol_val = {
    "brown":1, "red":2, "green":0.5, "blue":0.25, "violet":0.1, "gold":5, "silver":10
}

temp_val = {
    "black":250, "brown":100, "red":50, "orange":15, "yellow":25, "green":20, "blue":10, "violet":5, "grey":1, "gray":1
}


#------------------------------------------------------------------------------------------------------------------------------

def get_value(key, method):
    if method == "temp_val":
        return temp_val[key]
    elif method == "tol_val":
        return tol_val[key]
    elif method == "mul_val":
        return mul_val[key]
    elif method == "res_val":
        return res_val[key]

def solve_resist(*args):
    total = len(args)
    if total == 2:
        value = (args[0] * 10) + (args[1] * 1)
        return value
        
    else:
        value = (args[0] * 100) + (args[1] * 10 ) + (args[2] * 1)
        return value



#------------------------------------------------------------------------------------------------------------------------------



        
def solve(*args):

    band = len(args)
    temperature = ""

    if band == 4:
        resist = solve_resist(get_value(args[0], "res_val"), get_value(args[1], "res_val"))
        multiplier = get_value(args[2], "mul_val")
        tolerance = get_value(args[3], "tol_val")
        
    elif band == 5:
        resist = solve_resist(get_value(args[0], "res_val"), get_value(args[1], "res_val"), get_value(args[2], "res_val"))
        multiplier = get_value(args[3], "mul_val")
        tolerance = get_value(args[4], "tol_val")

    elif band == 6:
        resist = solve_resist(get_value(args[0], "res_val"), get_value(args[1], "res_val"), get_value(args[2], "res_val"))
        multiplier = get_value(args[3], "mul_val")
        tolerance = get_value(args[4], "tol_val")
        temperature = ", "+str(get_value(args[5], "temp_val"))+"ppm/K"
        
    else:
        print(f"\n{F.RED}[x]Error: Invalid Band Type")
        return True
        
    solve = (resist * multiplier) 
    print(f"\n{F.BLUE}[*]Output: {F.CYAN}{solve}Ω ±{tolerance}% {temperature}\n")
    upper_r = (solve) + (int(tolerance)/100) * solve
    lower_r = (solve) - (int(tolerance)/100) * solve
    print(f"{F.BLUE}[*]Range: {F.CYAN}{upper_r} ~ {lower_r}")




#------------------------------------------------------------------------------------------------------------------------------



 
try:
    def run_resist():
        print(f"\n{F.YELLOW}[!]Example For A 4 Band Resistor: {F.WHITE}red white yellow gold")   

        inp = input(F.GREEN+"[:]Enter Code: "+F.WHITE).lower().split()

        try:
            solve(*inp)
        except KeyError:
            print(f"\n{F.RED}[x]Invalid Color Code\n")

except:
    quit(0)


#------------------------------------------------------------------------------------------------------------------------------
#end line 114
