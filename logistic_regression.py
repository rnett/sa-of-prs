import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def log_reg(filename, cols, use_test=True):
    data = pandas.read_csv(filename, usecols=cols)

    # if 'sum_pos' in cols:
    #     data['sum_pos'] /= data['num_comments']
    #
    # if 'sum_neg' in cols:
    #     data['sum_neg'] /= data['num_comments']

    merged = pandas.read_csv(filename, usecols=['merged'], squeeze=True)

    X_train, X_test, y_train, y_test = train_test_split(data, merged, test_size=0.20,
                                                        shuffle=True, random_state=321)

    clf = LogisticRegression(solver='lbfgs').fit(X_train, y_train)

    if use_test:
        return clf.score(X_test, y_test)
    else:
        return clf.score(X_train, y_train)

def print_table(files, columns):
  print("\n        ", end=' ')
  for filepair in files:
    print(filepair[0], end='   \t')
  print()
    
  for colpair in columns:
    print(colpair[0], '-', end=' ')
    for filepair in files:
      print(round(log_reg(filepair[1], colpair[1]), 4), end='   \t')
    print()
  

if __name__ == '__main__':
    files = [("Issues ", 'sentiment-issue.csv'),
             ("Reviews", 'sentiment-review.csv'),
             ("Both   ", 'sentiment-both.csv')]

  columns = [("All   ", ['sum_pos', 'sum_neg', 'min_neg', 'max_pos', 'num_comments', 'has_images', 'has_code_snippets']),
             ("PosNeg", ['sum_pos', 'sum_neg', 'min_neg', 'max_pos']),
             ("Sums  ", ['sum_pos', 'sum_neg']),
             ("MaxMin", ['min_neg', 'max_pos']),
             ("SumPos", ['sum_pos']),
             ("SumNeg", ['sum_neg']),
             ("MinNeg", ['min_neg']),
             ("MaxPos", ['max_pos']),
             ("NumCom", ['num_comments']),
             ("Images", ['has_images']),
             ("Code  ", ['has_code_snippets']),
             ("SumCom", ['sum_pos', 'sum_neg', 'num_comments']),
             ("MM Com", ['min_neg', 'max_pos', 'num_comments'])]

  print_table(files, columns)
  '''
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
