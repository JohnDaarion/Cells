import numpy as np
from csv import reader


def read_csv(filename):
    X_str = list()
    y_str = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            else:
                X_str.append(row[:-1])
                y_str.append(row[-1])

    def convert_str2idx(y_str):
        unique = set(y_str)
        lookup = dict()
        for idx_label, label in enumerate(unique):
            lookup[label] = idx_label
        y_idx = list()
        for label in y_str:
            y_idx.append(lookup[label])
        return y_idx

    y_idx = convert_str2idx(y_str)

    X = np.array(X_str, dtype=np.float32)
    y = np.array(y_idx, dtype=np.int)

    return X, y


def normalize(X):
    x_min = X.min(axis=0)
    x_max = X.max(axis=0)
    for x in X:
        for j in range(X.shape[1]):
            x[j] = (x[j] - x_min[j]) / (x_max[j] - x_min[j])


def crossval_folds(N, n_folds, seed=1):
    np.random.seed(seed)
    idx_all_permute = np.random.permutation(N)
    N_fold = int(N / n_folds)
    idx_folds = []
    for i in range(n_folds):
        start = i * N_fold
        end = min([(i + 1) * N_fold, N])
        idx_folds.append(idx_all_permute[start:end])
    return idx_folds
