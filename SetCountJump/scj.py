import sys

vardict = {}
ip = 0

def runinst(left,op,right):
    global vardict
    global ip
    left = findval(left)
    #resright = findval(right)
    #print(f"{left} {op} {right}")
    match op:
        case ">":
            vardict[right] = left
            vardict[f"-{right}"] = -left
            if right == "$":
                print(chr(left),end="")
        case "+":
            if right in vardict:
                vardict[right] += left
                vardict[f"-{right}"] = -vardict[right]
        case ":":
            if left > 0:
                ip = findval(right) -2
                #print(f"ip: {ip}")

def findval(x: str):
    global ip
    res = 0
    if x.isdigit():
        x = int(x)
        res = x
    global vardict
    #print(type(x))
    if x in vardict and type(x)==str:
        res = vardict[x]
    elif type(x)==str:
        raise Exception(f"No such variable as '{x}' at line {ip+1}")
    return res

if len(sys.argv) > 1:
    fl = open(sys.argv[1])
else:
    raise Exception("Please give filename. Please. Next time. Okay? Good.")
code = fl.readlines()
fl.close()

while ip < len(code):
    inst = code[ip].rstrip("\r\n").split(" ",3)
    if len(inst) == 3:
        runinst(*inst)
    ip+=1