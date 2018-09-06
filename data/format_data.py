import os
import sys
#import os
reload(sys)
sys.setdefaultencoding('utf-8')

q_data = open('20180905/Q_list.txt', 'r')
a_data = open('20180905/A_list.txt', 'r')
#labels = open('A_ID.txt', 'r').readlines()
q_data = q_data.readlines()
a_data = a_data.readlines()

out_list = []
for idx, item in enumerate(q_data):
    #item = item.decode("utf-8")
    item = item.split('\n')
    item = item[0].split('\t')
    flag = int(item[1])
    
    for i in range(42):
        if i == flag:
            label = 1
        else:
            label = 0
        print(a_data[i].split('\n')[0].split('\t')[1])
       # out_list.append([item[0], a_data[i].split('\n')[0], str(label)])
        out_list.append([item[0], a_data[i].split('\n')[0].split('\t')[1]])

f_out = open('testing_v2.txt', 'w')
for x in out_list:
    for y in x:
        f_out.write(y)
        f_out.write('\t')
    f_out.write('\n')
f_out.close()
