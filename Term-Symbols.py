x=int(input('select microstates for equivalent or non equivalent electrons = '))

if x==0:
        
    import math 
    import numpy as np
    import itertools
    
    "no. of electron"
    term=['S','P','D','F','G','H','I','K','L','M','N','O','Q','T','U','V']
    print("Enter orbital number")
    l=int(input())
    print("Enter no. of electrons")
    no=int(input())
    ml=np.arange(-l,l+1)
    ms=(-1/2,1/2)
    set1=list(itertools.product(ml,ms))
    print("Possible sub orbitals")
    print("=========================")
    print(set1)
    set2=[]
    
    set2=list(itertools.combinations(set1,no))
    print("Total number of microstate")
    print("=========================")
    print(len(set2))
    set3=[]
    for i in range(0, len(set2)):
        x=0
        y=0
        for j in range(0,no):
            x=x+(set2[i][j][0])
            y=y+(set2[i][j][1])
        set3.append((x,y))
    
    print("Possible microstates")
    print("=========================")
    print(set3)
    print(len(set3))
    set4=[]
    set5=[]
    while len(set3)!=0:
        maxl=max(set3)[0]
        print("maxl")
        print(maxl)
        maxs=max(set3)[1]
        print("maxs")
        print(maxs)
        for i in range(0,int(2*maxs+1)):
            for k in range(0,2*maxl+1):
                set3.remove((maxl-k,maxs-i))
        set4.append((maxl,maxs))
        set5.append((str(int(2*maxs+1))+term[maxl]))
    print("Final no. of microstates")
    print("=========================")
    print(set4)
    print("Final microstates")
    print("=========================")
    print(set5)

else:        
    import math 
    import numpy as np
    import itertools
    
    term=['S','P','D','F','G','H','I','K','L','M','N','O','Q','T','U','V']
    print("Enter orbital number1")
    l1=int(input())
    print("Enter orbital number2")
    l2=int(input())
    
    print("Total Orbital Quantum Number")
    print("======================")
    L=np.arange(abs(l1-l2),l1+l2+1)
    print(L)
    print("Total Spin Quantum Number")
    print("=========================")
    s1=1/2
    s2=-1/2
    S=np.arange(s1+s2,s1-s2+1)
    print(S)
    
    print("multiplicity")
    print("============")
    r=[]
    for k in range(0,len(S)):
        r.append(int(2*S[k]+1))
    print(r)
    
    set=[]
    for i in range(0,len(r)):
        for j in range(0,len(L)):
            set.append((str(r[i])+term[L[j]]))    
    print("Final microstates")
    print("=========================")
    print(set)      
