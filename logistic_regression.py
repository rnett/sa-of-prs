from sklearn.linear_model import LogisticRegression
import pandas


def log_reg(filename, cols):
  data = pandas.read_csv(filename, usecols=cols)
  merged = pandas.read_csv(filename, usecols=['merged'], squeeze=True)
  clf = LogisticRegression().fit(data, merged)
  return clf.score(data,merged)

def to_percent(num):
  return str(round(num * 100, 2)) + "%"

if __name__ == '__main__':
  
  print("Issues:")
  print("All    -", to_percent(log_reg('sentiment-issue2.csv', ['sum_pos', 'sum_neg', 'min_neg', 'max_pos', 'num_comments', 'has_images', 'has_code_snippets'])))
  print("PosNeg -", to_percent(log_reg('sentiment-issue2.csv', ['sum_pos', 'sum_neg', 'min_neg', 'max_pos'])))
  print("Sums   -", to_percent(log_reg('sentiment-issue2.csv', ['sum_pos', 'sum_neg'])))
  print("MaxMin -", to_percent(log_reg('sentiment-issue2.csv', ['min_neg', 'max_pos'])))
  print("SumPos -", to_percent(log_reg('sentiment-issue2.csv', ['sum_pos'])))
  print("SumNeg -", to_percent(log_reg('sentiment-issue2.csv', ['sum_neg'])))
  print("MinNeg -", to_percent(log_reg('sentiment-issue2.csv', ['min_neg'])))
  print("MaxPos -", to_percent(log_reg('sentiment-issue2.csv', ['max_pos'])))
  print("NumCom -", to_percent(log_reg('sentiment-issue2.csv', ['num_comments'])))
  print("Images -", to_percent(log_reg('sentiment-issue2.csv', ['has_images'])))
  print("Code   -", to_percent(log_reg('sentiment-issue2.csv', ['has_code_snippets'])))
  print("SumCom -", to_percent(log_reg('sentiment-issue2.csv', ['sum_pos', 'sum_neg', 'num_comments'])))
  print("MM Com -", to_percent(log_reg('sentiment-issue2.csv', ['min_neg', 'max_pos', 'num_comments'])))
  
  print("\nReviews:")
  print("All    -", to_percent(log_reg('sentiment-review.csv', ['sum_pos', 'sum_neg', 'min_neg', 'max_pos', 'num_comments', 'has_images', 'has_code_snippets'])))
  print("PosNeg -", to_percent(log_reg('sentiment-review.csv', ['sum_pos', 'sum_neg', 'min_neg', 'max_pos'])))
  print("Sums   -", to_percent(log_reg('sentiment-review.csv', ['sum_pos', 'sum_neg'])))
  print("MaxMin -", to_percent(log_reg('sentiment-review.csv', ['min_neg', 'max_pos'])))
  print("SumPos -", to_percent(log_reg('sentiment-review.csv', ['sum_pos'])))
  print("SumNeg -", to_percent(log_reg('sentiment-review.csv', ['sum_neg'])))
  print("MinNeg -", to_percent(log_reg('sentiment-review.csv', ['min_neg'])))
  print("MaxPos -", to_percent(log_reg('sentiment-review.csv', ['max_pos'])))
  print("NumCom -", to_percent(log_reg('sentiment-review.csv', ['num_comments'])))
  print("Images -", to_percent(log_reg('sentiment-review.csv', ['has_images'])))
  print("Code   -", to_percent(log_reg('sentiment-review.csv', ['has_code_snippets'])))
  print("SumCom -", to_percent(log_reg('sentiment-review.csv', ['sum_pos', 'sum_neg', 'num_comments'])))
  print("MM Com -", to_percent(log_reg('sentiment-review.csv', ['min_neg', 'max_pos', 'num_comments'])))
  
  print("\nBoth:")
  print("All    -", to_percent(log_reg('sentiment-both.csv', ['sum_pos', 'sum_neg', 'min_neg', 'max_pos', 'num_comments', 'has_images', 'has_code_snippets'])))
  print("PosNeg -", to_percent(log_reg('sentiment-both.csv', ['sum_pos', 'sum_neg', 'min_neg', 'max_pos'])))
  print("Sums   -", to_percent(log_reg('sentiment-both.csv', ['sum_pos', 'sum_neg'])))
  print("MaxMin -", to_percent(log_reg('sentiment-both.csv', ['min_neg', 'max_pos'])))
  print("SumPos -", to_percent(log_reg('sentiment-both.csv', ['sum_pos'])))
  print("SumNeg -", to_percent(log_reg('sentiment-both.csv', ['sum_neg'])))
  print("MinNeg -", to_percent(log_reg('sentiment-both.csv', ['min_neg'])))
  print("MaxPos -", to_percent(log_reg('sentiment-both.csv', ['max_pos'])))
  print("NumCom -", to_percent(log_reg('sentiment-both.csv', ['num_comments'])))
  print("Images -", to_percent(log_reg('sentiment-both.csv', ['has_images'])))
  print("Code   -", to_percent(log_reg('sentiment-both.csv', ['has_code_snippets'])))
  print("SumCom -", to_percent(log_reg('sentiment-both.csv', ['sum_pos', 'sum_neg', 'num_comments'])))
  print("MM Com -", to_percent(log_reg('sentiment-both.csv', ['min_neg', 'max_pos', 'num_comments'])))
  
  '''
  print("Issues only:")
  print("All  -", log_reg('sentiment-issue.csv', ['max_pos', 'max_neg', 'has_images', 'has_code_snippets']))
  print("SUM  -", log_reg('sentiment-issue1.csv', ['sum']))
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
  '''
