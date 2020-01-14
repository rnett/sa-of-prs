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

    clf = LogisticRegression(solver='lbfgs')  # SVC()
    clf.fit(X_train, y_train)

    # print("Avg:", np.mean(clf.predict(X_test)))

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
