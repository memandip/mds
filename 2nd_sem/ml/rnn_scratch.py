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

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)

            # Calculate loss (mean squared error)
            loss = np.mean((output - y)**2)

            # Backward pass
            d_output = 2 * (output - y) / y.shape[0]
            self.backward(d_output, learning_rate)

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")

if __name__ == '__main__':
    # Toy data: Predict the sum of a sequence
    input_size = 1
    hidden_size = 16
    output_size = 1
    seq_length = 5
    
    # Create an RNN
    rnn = RNN(input_size, hidden_size, output_size)

    # Generate a simple dataset
    X = np.random.rand(100, seq_length, input_size)
    y = np.sum(X, axis=1)

    # Train the RNN
    rnn.train(X, y, epochs=1001, learning_rate=0.01)

    # Test the trained network
    test_X = np.array([[[0.1], [0.2], [0.3], [0.4], [0.5]]])
    test_y = np.sum(test_X)
    prediction = rnn.forward(test_X)
    print(f"\nTest Input Sum: {test_y}, Prediction: {prediction[0][0]}")
