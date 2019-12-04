import matplotlib.pyplot as plt
import pandas
from keras import Input, Model, metrics
from keras.callbacks import History
from keras.layers import Dense
from sklearn.model_selection import train_test_split


def log_reg(filename):
    data = pandas.read_csv(filename,
                           usecols=['sum_pos', 'sum_neg', 'min_neg', 'max_pos', 'num_comments', 'has_images',
                                    'has_code_snippets'])

    data['sum_pos'] /= data['num_comments']
    data['sum_neg'] /= data['num_comments']

    merged = pandas.read_csv(filename, usecols=['merged'], squeeze=True)

    X_train, X_test, y_train, y_test = train_test_split(data, merged, test_size=0.20,
                                                        shuffle=True, random_state=321)

    input = Input((7,))
    l = input
    l = Dense(8, activation='relu')(l)
    l = Dense(4, activation='relu')(l)
    l = Dense(1, activation='sigmoid')(l)

    model = Model(inputs=input, outputs=l)
    # model.summary()

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[metrics.binary_accuracy])

    hist: History = model.fit(X_train, y_train, epochs=10, verbose=False)

    plt.plot(hist.history['loss'])
    plt.plot(hist.history['binary_accuracy'])
    plt.show()

    acc = model.evaluate(X_test, y_test)[model.metrics_names.index("binary_accuracy")]
    print("Accuracy:", acc)


if __name__ == '__main__':
    log_reg('sentiment-issue.csv')
    log_reg('sentiment-review.csv')
    log_reg('sentiment-both.csv')
