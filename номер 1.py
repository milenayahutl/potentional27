f=open('astronaut_time.csv', encoding='utf8').readlines()
shp=f.pop(0)
a=[]

for x in f:
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

s=open('new_time.txt', 'w', encoding='utf8')

for i in range(len(f)):
    f[i] = f[i].strip().split(',')
    s.write(f'На станции {f[i][1]} в каюте {f[i][2]} восстановлено время. Актуальное время: {a[i]} \n')


s=open('new_time.txt', 'r', encoding='utf8')
f=s.readlines()
for i in range(3):
    print(f[i])