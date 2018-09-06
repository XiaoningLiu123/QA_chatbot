import os
import heapq

top_n = 16
 
score_file = open("test_result/pred_develop.score", 'r')
test_qa = open('data/testing_38.txt', 'r')
test_qa = test_qa.readlines()
score_data = score_file.readlines()

targets = open('data/A_ID.txt', 'r').readlines()

temp_list =[]
answer_list = []
for idx,item in enumerate(score_data):

    temp_list.append(float(item.split('\n')[0]))

    if (idx+1)%38 == 0:
        answerId = map(temp_list.index, heapq.nlargest(top_n, temp_list))
        answerId = list(answerId)
        answer_list.append(answerId)
        temp_list = []

cnt_right = 0
for idx,label in enumerate(targets):
    label = int(label.split('\n')[0])
    print(answer_list[idx], label)
    for item in answer_list[idx]:
        if int(item)==label:
            cnt_right += 1
#print(answer_list, len(answer_list))

print('Accuracy: ', float(cnt_right)/float(len(targets)))
