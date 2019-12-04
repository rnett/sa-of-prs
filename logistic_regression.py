import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def log_reg(filename, use_test=True):
    data = pandas.read_csv(filename,
                           usecols=['max_pos', 'max_neg', 'has_images', 'has_code_snippets'])
    merged = pandas.read_csv(filename, usecols=['merged'], squeeze=True)

    X_train, X_test, y_train, y_test = train_test_split(data, merged, test_size=0.20,
                                                        shuffle=True, random_state=321)

    clf = LogisticRegression().fit(X_train, y_train)

    if use_test:
        print(clf.score(X_test, y_test))
    else:
        print(clf.score(X_train, y_train))


if __name__ == '__main__':
    log_reg('sentiment-issue.csv')
    log_reg('sentiment-review.csv')
    log_reg('sentiment-both.csv')
