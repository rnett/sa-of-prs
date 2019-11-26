import re
import data
import pickle
import convert_funcs

type = "both"
sentiment_file = "both_sentiment"
csv_file = "sentiment-" + type + ".csv"
if __name__ == '__main__':
    file = open("parsed_data", 'rb')
    parsed_data = pickle.load(file)
    print(parsed_data)

    input = open(sentiment_file, 'r')
    output = open(csv_file, 'w')
    output.write("id,max_pos,max_neg,has_images,has_code_snippets,merged\n")
    prs = {}

    for data in parsed_data[type]:
        prs[data.id] = data

    for line in input:
        temp = re.sub(r' \t| ', ',', line)
        temp_list = temp.split(',')
        if prs[temp_list[0]].merged:
            merged = "True"
        else:
            merged = "False"

        if prs[temp_list[0]].images:
            has_images = "True"
        else:
            has_images = "False"

        if prs[temp_list[0]].code_snippets:
            has_code_snippets = "True"
        else:
            has_code_snippets = "False"

        output.write(temp_list[0] + ',' +
                     temp_list[1] + ',' +
                     temp_list[2][:2] + ',' +
                     has_images + ',' +
                     has_code_snippets + ',' +
                     merged + '\n')

    input.close()
    output.close()