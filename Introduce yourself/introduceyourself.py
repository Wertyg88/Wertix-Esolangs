import sys

def parseinst(inst: str) -> list:
    #preinsts = ["How old are you, ","How old are you in character, ","The age of ","Are you ","Pardon me, please say line "]
    inp = inst.split(", ")
    x = ""
    y = ""
    fini = ""
    match inp[0]:
        case "How old are you":
            x = inp[1].removesuffix("?")
            fini = "out"
        case "How old are you in character":
                x = inp[1].removesuffix("?")
                fini = "outchr"
        case "Pardon me":
                fini = inp[1].removeprefix("please say line ")
                x = fini.removesuffix(" again.")
                fini = "jump"
        case "Hi":
                x = inp[1].removeprefix("I am ")
                y = inp[2].removeprefix("I am ").removesuffix(" years old.")
                fini = "def"
        case _:
                if inp[0].endswith(" is now a secret."):
                    x = inp[0].removeprefix("The age of ").removesuffix(" is now a secret.")
                    fini = "in"
                elif inp[0].endswith(" is now a secret in character."):
                    x = inp[0].removeprefix("The age of ").removesuffix(" is now a secret in character.")
                    fini = "inchr"
                elif inp[0].endswith(" years later..."):
                    x = inp[0].removesuffix(" years later...").partition(": ")[0]
                    y = inp[0].removesuffix(" years later...").partition(": ")[2]
                    fini = "add"
                elif inp[0].endswith(" years ago..."):
                    x = inp[0].removesuffix(" years ago...").partition(": ")[0]
                    y = inp[0].removesuffix(" years ago...").partition(": ")[2]
                    fini = "sub"
                elif inp[1].endswith("?"):
                    y = inp[0].removeprefix("Are you ").partition(" years old")[0]
                    x = inp[1].removesuffix("?")
                    fini = "if"
    return [fini,x,y]

vardict = {}
ip = 0

def resolve(inp: str):
     global vardict
     if inp in vardict:
          return vardict[inp]
     elif inp.isdigit():
          return int(inp)

def runinst(inst,x,y):
    global vardict
    global ip
    match inst:
        case "def":
              if x not in vardict:
                   vardict[x] = resolve(y)
        case "out":
            print(resolve(x),end="")
        case "outchr":
            print(chr(resolve(x)%256), end="")
        case "jump":
            ip = resolve(x) -2
        case "in":
            vardict[x] = int(input())
        case "inchr":
            vardict[x] = ord(sys.stdin.read(1))
        case "add":
            vardict[x] += resolve(y)
        case "sub":
            if vardict[x] - resolve(y) >= 0:
                vardict[x] -= resolve(y)
        case "if":
            if resolve(x) != resolve(y):
                ip += 1

rwcode = open(sys.argv[1]).readlines()
code = []
for ln in rwcode:
    code.append(ln.strip())

while ip < len(code):
    curi = parseinst(code[ip])
    #print(f"debug ip: {ip}, {curi}")
    runinst(*curi)
    ip += 1