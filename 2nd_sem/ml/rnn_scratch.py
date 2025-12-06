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

if __name__ == '__main__':
    # Toy data
    input_size = 10
    hidden_size = 20
    
    # Create an RNN cell
    rnn_cell = RNNCell(input_size, hidden_size)

    # Input for a single time step (batch size = 1)
    x = np.random.randn(1, input_size)
    
    # Initial hidden state
    h_prev = np.zeros((1, hidden_size))

    # Forward pass for a single time step
    h_next = rnn_cell.forward(x, h_prev)

    print("Input shape:", x.shape)
    print("Previous hidden state shape:", h_prev.shape)
    print("Next hidden state shape:", h_next.shape)
