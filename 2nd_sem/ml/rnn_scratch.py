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

class FCLayer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.1
        self.biases = np.zeros((1, output_size))

    def forward(self, X):
        self.input = X
        return np.dot(X, self.weights) + self.biases

class RNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.rnn_cell = RNNCell(input_size, hidden_size)
        self.fc = FCLayer(hidden_size, output_size)

    def forward(self, X):
        self.X = X
        batch_size, seq_length, _ = X.shape
        h = np.zeros((batch_size, self.hidden_size))
        self.hidden_states = [h]

        for t in range(seq_length):
            h = self.rnn_cell.forward(X[:, t, :], h)
            self.hidden_states.append(h)
        
        self.output = self.fc.forward(h)
        return self.output

    def backward(self, d_output, learning_rate):
        # Backprop through FC layer
        d_h = np.dot(d_output, self.fc.weights.T)
        d_W_out = np.dot(self.hidden_states[-1].T, d_output)
        d_b_out = np.sum(d_output, axis=0, keepdims=True)

        # BPTT
        d_W_ih = np.zeros_like(self.rnn_cell.W_ih)
        d_W_hh = np.zeros_like(self.rnn_cell.W_hh)
        d_b_h = np.zeros_like(self.rnn_cell.b_h)

        for t in reversed(range(len(self.hidden_states) - 1)):
            # Gradient of tanh
            d_tanh = (1 - self.hidden_states[t+1]**2) * d_h
            
            # Gradients for weights and biases
            d_W_ih += np.dot(self.X[:, t, :].T, d_tanh)
            d_W_hh += np.dot(self.hidden_states[t].T, d_tanh)
            d_b_h += np.sum(d_tanh, axis=0, keepdims=True)

            # Gradient for next hidden state
            d_h = np.dot(d_tanh, self.rnn_cell.W_hh.T)

        # Update weights
        self.fc.weights -= learning_rate * d_W_out
        self.fc.biases -= learning_rate * d_b_out
        self.rnn_cell.W_ih -= learning_rate * d_W_ih
        self.rnn_cell.W_hh -= learning_rate * d_W_hh
        self.rnn_cell.b_h -= learning_rate * d_b_h

if __name__ == '__main__':
    # Toy data
    input_size = 10
    hidden_size = 20
    output_size = 5
    seq_length = 5
    batch_size = 1

    # Create an RNN
    rnn = RNN(input_size, hidden_size, output_size)

    # Input sequence and target
    X = np.random.randn(batch_size, seq_length, input_size)
    y = np.random.randn(batch_size, output_size)

    # Forward pass
    output = rnn.forward(X)

    # Backward pass (dummy gradient)
    d_output = output - y
    rnn.backward(d_output, learning_rate=0.01)

    print("Input sequence shape:", X.shape)
    print("Output shape:", output.shape)
    print("Backward pass completed.")
