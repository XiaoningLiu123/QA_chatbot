import os

id_data = open('A_ID.txt', 'r').readlines()
answer_list = open('answer_list.txt', 'r').readlines()

id_data_38 = set(id_data)
id_temp = []
out_list = []
for idx, item in enumerate(id_data):
    item = int(item.split('\n')[0])
    if item not in id_temp:
        id_temp.append(item)
        print(answer_list[idx].split('\n')[0])
        out_list.append(answer_list[idx].split('\n')[0])
        
out_a = open('answers_38.txt', 'w')
for item in out_list:
    out_a.write(item)
    out_a.write('\n')
out_a.close()
