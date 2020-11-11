# with open('text.txt','w') as fp:
#     for i in range(10):
#         i +=1 
#         data = "피카츄 %d" % i
#         fp.write(data)
#         fp.write("\n")

# with open('text.txt','r') as fp2:    
#     print(fp2.readline())
#     print(fp2.readlines())
#     print(fp2.read())
    
# with open('text.txt','a') as fp3:
#     fp3.write('\nEnd writting file')

import csv

with open('csv_test.csv','w',newline='') as c:
    wr = csv.writer(c)
    wr.writerow(['Name','skill 1','skill 2','skill 3'])

for j in range(3):
    name = input("Name : ")
    skills = ['','','']
    for i in range(3):
        print(f"skill {i+1} :", end='')
        skills[i] = input("")
    with open("csv_test.csv",'a',newline='') as c:
        wr = csv.writer(c)
        wr.writerow([name,skills[0],skills[1],skills[2]])

with open('csv_test.csv','r') as c:
    rd = csv.reader(c)
    for line in rd:
        print(line)