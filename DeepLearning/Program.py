import numpy as np
from src.NeuralNetworkClass import NeuralNetwork
import src.utils as utils


def main():
    filename = "training_data.csv"
    n_hidden_nodes = [5]
    l_rate = 0.6
    n_epochs = 800
    n_folds = 4

    print("Neural network model:\n n_hidden_nodes = {}".format(n_hidden_nodes))
    print(" l_rate = {}".format(l_rate))
    print(" n_epochs = {}".format(n_epochs))
    print(" n_folds = {}".format(n_folds))

    print("\nReading '{}'...".format(filename))
    X, y = utils.read_csv(filename)
    utils.normalize(X)
    N, d = X.shape
    n_classes = len(np.unique(y))

    print(" X.shape = {}".format(X.shape))
    print(" y.shape = {}".format(y.shape))
    print(" n_classes = {}".format(n_classes))

    idx_all = np.arange(0, N)
    idx_folds = utils.crossval_folds(N, n_folds, seed=1)

    acc_train, acc_test = list(), list()
    print("\nTraining and cross-validating...")
    for i, idx_test in enumerate(idx_folds):
        idx_train = np.delete(idx_all, idx_test)
        X_train, y_train = X[idx_train], y[idx_train]
        X_test, y_test = X[idx_test], y[idx_test]

        model = NeuralNetwork(n_input=d, n_output=n_classes, n_hidden_nodes=n_hidden_nodes)
        model.train(X_train, y_train, l_rate=l_rate, n_epochs=n_epochs)

        y_train_predict = model.predict(X_train)
        y_test_predict = model.predict(X_test)

        acc_train.append(100 * np.sum(y_train == y_train_predict) / len(y_train))
        acc_test.append(100 * np.sum(y_test == y_test_predict) / len(y_test))

        print(" Fold {}/{}: train acc = {:.2f}%, test acc = {:.2f}% (n_train = {}, n_test = {})".format(i + 1, n_folds,
                                                                                                        acc_train[-1],
                                                                                                        acc_test[-1],
                                                                                                        len(X_train),
                                                                                                        len(X_test)))

    print("\nAvg train acc = {:.2f}%".format(sum(acc_train) / float(len(acc_train))))
    print("Avg test acc = {:.2f}%".format(sum(acc_test) / float(len(acc_test))))


if __name__ == "__main__":
    main()
