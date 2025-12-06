import numpy as np

class RNNCell:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size

        # Weights for input and hidden state
        self.W_ih = np.random.randn(input_size, hidden_size) * 0.1
        self.W_hh = np.random.randn(hidden_size, hidden_size) * 0.1
        self.b_h = np.zeros((1, hidden_size))

    def forward(self, x, h_prev):
        # x: input for a single time step
        # h_prev: hidden state from the previous time step
        h_next = np.tanh(np.dot(x, self.W_ih) + np.dot(h_prev, self.W_hh) + self.b_h)
        return h_next

class RNN:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.rnn_cell = RNNCell(input_size, hidden_size)

    def forward(self, X):
        # X: input sequence of shape (batch_size, seq_length, input_size)
        batch_size, seq_length, _ = X.shape
        h = np.zeros((batch_size, self.hidden_size))
        self.hidden_states = []

        for t in range(seq_length):
            h = self.rnn_cell.forward(X[:, t, :], h)
            self.hidden_states.append(h)
        return h, self.hidden_states

if __name__ == '__main__':
    # Toy data
    input_size = 10
    hidden_size = 20
    seq_length = 5
    batch_size = 1

    # Create an RNN
    rnn = RNN(input_size, hidden_size)

    # Input sequence
    X = np.random.randn(batch_size, seq_length, input_size)

    # Forward pass for the sequence
    h_last, hidden_states = rnn.forward(X)

    print("Input sequence shape:", X.shape)
    print("Last hidden state shape:", h_last.shape)
    print("Number of hidden states:", len(hidden_states))
    print("Shape of a hidden state:", hidden_states[0].shape)
