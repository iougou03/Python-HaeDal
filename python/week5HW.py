import csv

data=[['컴퓨터 구조','컴퓨터 비전','클라우드 컴퓨팅','SW창업 프로젝트','컴퓨터망프로그래밍','데이터과학기초'],
     ['이시형','정순기','김은주','이호경','서지훈','박혜영'],
     [3,3,3,3,3,3]]

with open('Classes.csv','w',newline='') as c:
    cp = csv.writer(c)
    cp.writerow(['Name','Professor','Point'])
    i=0
    for course in data[0]: 
        in_data = [course,data[1][i],data[2][i]]
        cp.writerow(in_data)
        i+=1
#------------------------------------------------
with open('Classes.csv','r') as c:
    clines= csv.reader(c)
    for line in clines:
        print(line)

