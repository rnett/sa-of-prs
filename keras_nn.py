import matplotlib.pyplot as plt
import pandas
from keras import Input, Model, metrics
from keras.callbacks import History
from keras.layers import Dense


def log_reg(filename):
  data = pandas.read_csv(filename,
                         usecols=['max_pos', 'max_neg'])
  merged = pandas.read_csv(filename, usecols=['merged'], squeeze=True)

  input = Input((2,))
  l = input
  # l = Dense(2, activation='relu')(l)
  # l = Dense(8, activation='relu')(l)
  l = Dense(1, activation='sigmoid')(l)

  model = Model(inputs=input, outputs=l)
  # model.summary()

  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[metrics.binary_accuracy])

  hist: History = model.fit(data, merged, epochs=10, verbose=False)

  plt.plot(hist.history['loss'])
  plt.plot(hist.history['binary_accuracy'])
  plt.show()

  acc = model.evaluate(data, merged)[model.metrics_names.index("binary_accuracy")]
  print("Accuracy:", acc)


if __name__ == '__main__':
  log_reg('sentiment-issue.csv')
  log_reg('sentiment-review.csv')
  log_reg('sentiment-both.csv')
