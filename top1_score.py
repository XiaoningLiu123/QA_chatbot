import os

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
        answerId = temp_list.index(max(temp_list))

        print(test_qa[38*((idx+1)/38-1)+answerId])

        answer_list.append(answerId)
        temp_list = []

cnt_right = 0
for idx,label in enumerate(targets):
    label = int(label.split('\n')[0])
    print(int(answer_list[idx]), label)
    if int(answer_list[idx])==label:
        cnt_right +=1
    
#print(answer_list, len(answer_list))

print('Accuracy: ', float(cnt_right)/float(len(targets)))
