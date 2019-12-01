from sklearn.linear_model import LogisticRegression
import pandas


def log_reg(filename):
  data = pandas.read_csv(filename, 
    usecols=['max_pos', 'max_neg', 'has_images', 'has_code_snippets'])
  merged = pandas.read_csv(filename, usecols=['merged'], squeeze=True)
  clf = LogisticRegression().fit(data, merged)
  print(clf.score(data,merged))


if __name__ == '__main__':
  log_reg('sentiment-issue.csv')
  log_reg('sentiment-review.csv')
  log_reg('sentiment-both.csv')
