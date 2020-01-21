import re
import data
import pickle
import convert_funcs

class Sentiment:
    def __init__(self):
        self.sum_pos = 0
        self.sum_neg = 0
        self.min_neg = 0
        self.max_pos = 0
        self.num_comments = 0

    def add_comment(self, pos, neg):
        pos -= 1
        neg += 1

        self.sum_pos += pos
        self.sum_neg += neg
        if pos > self.max_pos:
            self.max_pos = pos

        if neg < self.min_neg:
            self.min_neg = neg

        self.num_comments += 1


if __name__ == '__main__':
    file = open("data/parsed_data", 'rb')
    parsed_data = pickle.load(file)
    file.close()
    types = ["both", "issue"]

    for type in types:
        sentiment_file = "data/se-" + type
        csv_file = "sentiment-" + type + ".csv"
        input = open(sentiment_file, 'r')
        output = open(csv_file, 'w')
        output.write("id,sum_pos,sum_neg,min_neg,max_pos,num_comments,has_images,has_code_snippets,merged\n")
        prs = {}

        for data in parsed_data[type]:
            prs[str(data.id)] = (data, Sentiment())

        for line in input:
            temp = re.sub(r' \t| ', ',', line)
            temp_list = temp.split(',')
            temp_data, sentiment = prs[temp_list[0]]

            sentiment.add_comment(int(temp_list[1]), int(temp_list[2][:-1]))

        for (data, sentiment) in prs.values():
            has_images = "True" if data.images else "False"
            has_code_snippets = "True" if data.code_snippets else "False"
            merged = "True" if data.merged else "False"

            if (sentiment.sum_pos == 0 and
                sentiment.sum_neg == 0 and
                sentiment.min_neg == 0 and
                sentiment.max_pos == 0):
                continue
            output.write(str(data.id) + ',' +
                         str(sentiment.sum_pos) + ',' +
                         str(sentiment.sum_neg) + ',' +
                         str(sentiment.min_neg) + ',' +
                         str(sentiment.max_pos) + ',' +
                         str(sentiment.num_comments) + ',' +
                         has_images + ',' +
                         has_code_snippets + ',' +
                         merged + '\n')

        input.close()
        output.close()