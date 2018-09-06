import os

score_list = []
score_data = open('test_result/pred_develop.score', 'r')
score_data = score_data.readlines()

id_list = []
for i, item in enumerate(score_data):
    if i == 99:
        break
    item = item.split('\n')
    score = round(float(item[0]), 4)
    print(score)
    if score in score_list:
        a_id = score_list.index(score)
    else:
        score_list.append(score)
        if len(id_list)==0:
            a_id=0
        else:
            a_id = max(id_list)+1
    id_list.append(a_id)

out_id = open('A_ID.txt', 'w')
for item in id_list:
    out_id.write(str(item))
    out_id.write('\n')

out_id.close()

