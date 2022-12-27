def reqargs(a,b,c,d):
    return a+b+c+d

def keywordargs(a,b,c,d):
    return a+b+c+d

def defaultargs(a,b,c=6,d=2):
    return a+b+c+d

def variablelengthargs(a,*b):
    s = 0
    for i in b:
        s = s+i
    s+a
    return s


print("required arguments",reqargs(1,3,6,2))
print("keyword arguments",keywordargs(d=2,b=3,c=6,a=1))
print("default arguments",defaultargs(1,3))
print("variablelength arguments",variablelengthargs(1,3,6,2,15))
