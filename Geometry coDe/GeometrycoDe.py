import sys

if len(sys.argv) > 1:
    fl = open(sys.argv[1])
else:
    raise Exception("Please give filename. Please. Next time. Okay? Good.")
rwcode = fl.read()
fl.close()
code = rwcode.split()

accs = [0,0,0]
curfunc = ""
secacc = 0
sp = 1
wavestc = []
run = True

def runfunc(a):
    global accs
    global curfunc
    global secacc
    global sp
    global wavestc
    global ip
    global run
    curacc = accs[a]
    if run:
        for i in range(sp):
            match curfunc:
                case "cube":
                    accs[a] += 1
                case "ship":
                    accs[a] -= 1
                case "ball":
                    accs[a] = 0
                case "spider":
                    accs[a] = -accs[a]
                case "robot":
                    print(chr(accs[a]), end="")
                case "ufo":
                    accs[a] += accs[secacc]
                case "trigger":
                    accs[a] = ord(sys.stdin.read(1))
                case "wave":
                    if accs[a] > 0:
                        wavestc.append(ip-2)
                        #print(wavestc)
                    else:
                        run = False
                case "swing":
                    if accs[a] > 0:
                        #print(wavestc)
                        ip = wavestc.pop()
                    else:
                        wavestc.pop()
    elif curfunc == "swing":
        run = True

def runinst(inst):
    global accs
    global curfunc
    global secacc
    global ip
    global sp
    match inst:
        case "spike":
            runfunc(0)
        case "saw":
            runfunc(1)
        case "block":
            runfunc(2)
        case "mini":
            secacc = 0
        case "dual":
            secacc = 1
        case "mirror":
            secacc = 2
        case "1x":
            sp = 1
        case "2x":
            sp = 2
        case "3x":
            sp = 3
        case "4x":
            sp = 4
        case "end":
            ip = 9999999999999999999
        case _:
            curfunc = inst

ip = 0
while ip < len(code):
    runinst(code[ip])
    ip += 1