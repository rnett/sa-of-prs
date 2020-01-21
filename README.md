# Sentiment Analysis of Pull Requests

This repository contains the code used in the paper "Sentiment Analysis of Pull Requests".

## Structure

### Data Prep
The initial checking and storing of pull requests is done in `Preprocess.ipynb`.
This is where we generate our dataset of 10k pull requests and their comments.

### Sentiment Analysis

1. run `python3 convert.py`
2. run `java -jar SentiStrength-SE_V1.5.jar`
3. Detect sentiments for each data file <br />
    a. `data/input-se-both.txt` <br />
    b. `data/input-se-issues.txt` <br />
    c. `data/input-se-review.txt` <br />
4. Save the outputs the the following files: <br />
    a. `data/se-both.txt` <br />
    b. `data/se-issue` <br />
    c. `data/se-review` <br />
5. run `python3 convert_senti-strength-se.py`

### Analysis

Our model fitting is done in `logistic_regression.py`.
`keras_nn.py` is the Keras model we used as a sanity check.

## Data

`sentiment-both.csv`, `sentiment-issue.csv`, and `sentiment-review.csv` are data files for use in analysis.
They contain features for issues and code review comments, just issues, and just code review comments, respectively.


