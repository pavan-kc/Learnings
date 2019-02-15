a,b,c,d=input("enter a"),input("enter b"),input("enter c"),input("enter d")
if a>b and a>c and a>d:
    print("a "+str(a)+ " is greatest")
elif b>c and b>d:
    print("b "+str(b)+" is greater")
elif c>d:
    print("c "+str(c)+" is greater")
else:
    print("d "+str(d)+" is greater")
