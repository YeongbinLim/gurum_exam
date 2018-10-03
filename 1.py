import sys





def numParser(i,a,y): #년월일 숫자 얻는 파서


    result=[]
    real=[]
    j=i-1
    count=0
    while a[j].isdigit() == True:
        j=j-1
        count+=1
    j+=1
    for k in range(j,j+count):
        result+=a[k]

    if y==0 and len(result)!=4:
        result.insert(0,0)
        result.insert(0,2)

    #[2,0,1,8] -> 2018 로 합치기
    real=''.join(str(v) for v in result)
    real=int(real)
    return real

sentence=[]
#END를 입력해야 입력끝   한줄 검사후  집어 널기
while True:
    try:
        a=input()
        if a[-1]=="D" and a[-2]=="N" and a[-3]=="E":
            a = a.replace("END", "")
            sentence.append(a)
            break
        else:
            sentence.append(a)
    except EOFError:
        break


year_counter=0
month_counter=1
date_counter=2
money=20000
year=[None]*len(sentence)
month=[None]*len(sentence)
date=[None]*len(sentence)
arr5=[]
a=[]
y=0
m=0
d=0
j=0
# a에 원소 하나하나 분리해서 집어 넣기
for j in range(0,len(sentence)):
    a.extend(sentence[j])
#년월일 checker
for i in range(0,len(a)):
    if a[i]=="년" or (a[i]=="/" and year_counter==0) or (a[i]=="-" and year_counter==0) :

        year_counter+=1
        month_counter=0

        year[y]=numParser(i,a,0)
        y+=1
    elif a[i]=="월" or (a[i]=="/" and month_counter==0) or (a[i]=="-" and month_counter==0) :
        month_counter+=1
        date_counter=0
        month[m]=numParser(i,a,1)
        m+=1
    elif a[i].isdigit()== False and date_counter==0 :
        year_counter=0
        date_counter+=1
        date[d] = numParser(i,a,1)
        d+=1


class Time: #날짜정보 + 문장 + 순서
    def setdata(self,y,m,d,sentence,order):
        self.y=int(y)
        self.m=int(m)
        self.d=int(d)
        self.sentence=sentence
        self.order=order
    def get_y(self):
        return self.y
    def get_m(self):
        return self.m
    def get_d(self):
        return self.d
    def get_s(self):
        return self.sentence
    def get_order(self):
        return self.order

for i in range(0,len(sentence)):
        arr5.append(Time())
        arr5[i].setdata(year[i],month[i],date[i],sentence[i],i)

order=[]
low_year=3000
y_order=0
low_month=0
m_year=0
low_date=0
counter_1=0
#크기순 구하기
while len(order) == len(sentence):
    i=0

    if low_year > year[i]:

        low_year=year[i]
        order.insert(0, arr5[i].order)
    i += 1
    counter_1+=1
    if counter_1 == len(sentence):
        i=0
        while len(order) == len(sentence):




print(order)
for i in order:
    print("k")
    sys.stdout.write(arr5[i].sentence)








