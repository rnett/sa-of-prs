import re
import data

input = open('senti_strength_se_output', 'r')
output = open('sentiment.csv', 'w')
output.write("id,max_pos,max_neg,merged\n")
prs = {}

for list_of_prs in data.PR.load_all():
    # print(len(list_of_prs))

    for pr in list_of_prs:
        prs[pr.id] = pr.merged

for line in input:
    temp = re.sub(r' \t| ', ',', line)
    temp_list = temp.split(',')
    if prs[temp_list[0]]:
        merged = "true"
    else:
        merged = "false"
    output.write(merged + ',' + re.sub(r' \t| ', ',', line))

input.close()
output.close()