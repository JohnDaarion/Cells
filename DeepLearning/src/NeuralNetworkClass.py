import random
from math import exp

import numpy as np


class NeuralNetwork:
    def __init__(self, n_input=None, n_output=None, n_hidden_nodes=None):
        self.n_input = n_input
        self.n_output = n_output
        self.n_hidden_nodes = n_hidden_nodes
        self.network = self._build_network()

    def train(self, X_train, y_train, l_rate=0.5, n_epochs=1000):

        for epoch in range(n_epochs):
            for (x, y) in zip(X_train, y_train):
                self._forward_pass(x)
                y_target = np.zeros(self.n_output, dtype=np.int)
                y_target[y] = 1
                self._backward_pass(y_target)
                self._update_weights(x, l_rate=l_rate)

    def predict(self, X):

        y_predict = np.zeros(len(X), dtype=np.int)
        for i, x in enumerate(X):
            output = self._forward_pass(x)
            y_predict[i] = np.argmax(output)

        return y_predict

    def _build_network(self):
        def _build_layer(n_input, n_output):
            layer = list()
            for idx_out in range(n_output):
                weights = list()
                for idx_in in range(n_input):
                    weights.append(random.random())
                layer.append({"weights": weights,
                              "output": None,
                              "delta": None})
            return layer

        n_hidden_layers = len(self.n_hidden_nodes)
        network = list()
        if n_hidden_layers == 0:
            network.append(_build_layer(self.n_input, self.n_output))
        else:
            network.append(_build_layer(self.n_input, self.n_hidden_nodes[0]))
            for i in range(1, n_hidden_layers):
                network.append(_build_layer(self.n_hidden_nodes[i - 1],
                                            self.n_hidden_nodes[i]))
            network.append(_build_layer(self.n_hidden_nodes[n_hidden_layers - 1],
                                        self.n_output))

        return network

    def _forward_pass(self, x):
        def activate(weights, inputs):
            activation = 0.0
            for i in range(len(weights)):
                activation += weights[i] * inputs[i]
            return activation

        input = x
        for layer in self.network:
            output = list()
            for node in layer:
                activation = activate(node['weights'], input)
                node['output'] = self._transfer(activation)
                output.append(node['output'])
            input = output

        return input

    def _backward_pass(self, target):
        n_layers = len(self.network)
        for i in reversed(range(n_layers)):
            layer = self.network[i]
            errors = list()
            if i == n_layers - 1:
                for j, node in enumerate(layer):
                    error = target[j] - node['output']
                    errors.append(error)
            else:
                for j, node in enumerate(layer):
                    error = 0.0
                    for node in self.network[i + 1]:
                        error += node['weights'][j] * node['delta']
                    errors.append(error)

            for j, node in enumerate(layer):
                node['delta'] = errors[j] * self._transfer_derivative(node['output'])

    def _update_weights(self, x, l_rate=0.3):
        for i_layer, layer in enumerate(self.network):
            if i_layer == 0:
                inputs = x
            else:
                inputs = np.zeros(len(self.network[i_layer - 1]))
                for i_node, node in enumerate(self.network[i_layer - 1]):
                    inputs[i_node] = node['output']
            for node in layer:
                for j, input in enumerate(inputs):
                    dW = l_rate * node['delta'] * input
                    node['weights'][j] += dW

    def _transfer(self, x):
        return 1.0 / (1.0 + exp(-x))

    def _transfer_derivative(self, transfer):
        return transfer * (1.0 - transfer)
