from sklearn.linear_model import LogisticRegression
import pandas


def log_reg(filename, cols):
  data = pandas.read_csv(filename, usecols=cols)
  merged = pandas.read_csv(filename, usecols=['merged'], squeeze=True)
  clf = LogisticRegression().fit(data, merged)
  return clf.score(data,merged)


if __name__ == '__main__':
  print("Issues only:")
  print("All  -", log_reg('sentiment-issue.csv', ['max_pos', 'max_neg', 'has_images', 'has_code_snippets']))
  print("Max  -", log_reg('sentiment-issue.csv', ['max_pos', 'max_neg']))
  print("Pos  -", log_reg('sentiment-issue.csv', ['max_pos']))
  print("Neg  -", log_reg('sentiment-issue.csv', ['max_neg']))
  print("Imgs -", log_reg('sentiment-issue.csv', ['has_images']))
  print("Code -", log_reg('sentiment-issue.csv', ['has_code_snippets']))
  print("\nReviews only:")
  print("All  -", log_reg('sentiment-review.csv', ['max_pos', 'max_neg', 'has_images', 'has_code_snippets']))
  print("Max  -", log_reg('sentiment-review.csv', ['max_pos', 'max_neg']))
  print("Pos  -", log_reg('sentiment-review.csv', ['max_pos']))
  print("Neg  -", log_reg('sentiment-review.csv', ['max_neg']))
  print("Imgs -", log_reg('sentiment-review.csv', ['has_images']))
  print("Code -", log_reg('sentiment-review.csv', ['has_code_snippets']))
  print("\nBoth:")
  print("All  -", log_reg('sentiment-both.csv', ['max_pos', 'max_neg', 'has_images', 'has_code_snippets']))
  print("Max  -", log_reg('sentiment-both.csv', ['max_pos', 'max_neg']))
  print("Pos  -", log_reg('sentiment-both.csv', ['max_pos']))
  print("Neg  -", log_reg('sentiment-both.csv', ['max_neg']))
  print("Imgs -", log_reg('sentiment-both.csv', ['has_images']))
  print("Code -", log_reg('sentiment-both.csv', ['has_code_snippets']))
