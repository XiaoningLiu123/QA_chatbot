# encoding:utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

raw_data = open('cmj_training.txt', 'r')
raw_data = raw_data.readlines()

raw_data_list = raw_data[0].split('\t')
print(len(raw_data_list))

question_list = []
answers_list = []

for idx, item in enumerate(raw_data_list):
#    item = item.split('0')
#    if len(item)>1:
#        print('Before', item)
#        item_out = item[0]
#        for sub_item in item[1:]:
#            print(type(item_out), type(sub_item))
#            item_out = item_out +'0'+ sub_item
#        print('After', item_out)
#    else:
    #item_out = item.split('\t')
    item_out = item.decode("utf-8")   
    print(item_out)
    if idx % 2 ==0:
        question_list.append(item_out)
    else:
        answers_list.append(item_out)

out_q = open('question_list.txt', 'w')
for item in question_list:
    out_q.write(item)
    out_q.write('\n')
out_q.close()

out_a = open('answer_list.txt', 'w')
for item in answers_list:
    out_a.write(item)
    out_a.write('\n')
out_a.close()

