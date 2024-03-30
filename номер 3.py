"""
a - список восстановленного времени
stationnum - вводимый номер станции
"""


m=open('astronaut_time.csv', encoding='utf8').readlines()
shp=m.pop(0)
a=[]

for x in m:
    x=x.strip().split(',')
    x[0]=int(x[0])
    x[4]=int(x[4])
    x[3]=[int(j) for j in x[3].split(':')]
    if x[3][0]<23:
       x[3][0]+=x[4]
    else:
        x[3][0]=0+x[4]-1
    x[3]=f'{x[3][0]}:{x[3][1]}:{x[3][2]}'
    a.append(x[3])

while 1:
    stationnum=input()
    if stationnum=='stop':
        break
    else:
        f=0
        for i in range(len(m)):
            m[i]=m[i].strip().split(',')

            if m[i][1]==stationnum:
                f=1
                print(f'На станции {stationnum} восстановлено время {m[i][3]}. Актуальное время: {a[i]}')
        if f==0:
            print('На станции все хорошо')


