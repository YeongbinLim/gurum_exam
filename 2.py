m=int(input())
Ni=[]
Ni=input()
Ni=Ni.split()
Ni = [int (i) for i in Ni]
init=[]
init=input()
init=init.split()
init = [int (i) for i in init]
press=int(input())
def sum(Ni,init,m,cnt):

    if cnt == 0:
        result=[]
        s = ''.join(str(v) for v in init)
        print(s)
        return 5
    else:
        init[len(Ni)-1]+=1

        cnt-=1

        check(Ni,init,m,cnt)

def check(Ni,init,m,cnt):


    if Ni[m-1] < init[m-1]:
        if m<2:
            init[m - 1] = 0
            sum(Ni, init, len(Ni), cnt)
        else:
            init[m-1]=0
            init[m-2]+=1
            check(Ni,init,m-1,cnt)
    else:
        sum(Ni,init,len(Ni),cnt)

sum(Ni,init,m,press)

