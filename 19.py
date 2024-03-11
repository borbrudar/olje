from datetime import date,timedelta

cd = date(1901,1,1)
for i in range(0,7):
    if (cd+ timedelta(i)).weekday() == 6:
        cd += timedelta(i)
        break
    
cnt=0
while cd.year < 2001:
    if cd.day == 1: cnt +=1
    cd += timedelta(7)

print(cnt)