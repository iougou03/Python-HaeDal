import csv

data=[['컴퓨터 구조','컴퓨터 비전','클라우드 컴퓨팅','SW창업 프로젝트','컴퓨터망프로그래밍','데이터과학기초'],
     ['이시형','정순기','김은주','이호경','서지훈','박혜영'],
     [3,3,3,3,3,3],
     ['COMP411008','ITEC424001','GLSO227001','GLSO217002','GLSO229001','ITEC419001']]

with open('Classes.csv','w',newline='') as c:
    cp = csv.writer(c)
    cp.writerow(['Name','Professor','Point','Code'])
    i=0
    for course in data[0]: 
        in_data = [course,data[1][i],data[2][i],data[3][i]]
        cp.writerow(in_data)
        i+=1
#------------------------------------------------
with open('Classes.csv','r') as c:
    clines= csv.reader(c)
    for line in clines:
        print(line)

