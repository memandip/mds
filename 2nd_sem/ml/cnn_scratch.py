import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / np.sum(e_x, axis=-1, keepdims=True)

def cross_entropy_loss(y_pred, y_true):
    m = y_true.shape[0]
    p = softmax(y_pred)
    log_likelihood = -np.log(p[range(m), y_true])
    loss = np.sum(log_likelihood) / m
    return loss, p

class ConvLayer:
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

        self.kernels = np.random.randn(out_channels, in_channels, kernel_size, kernel_size) * 0.1
        self.biases = np.zeros((out_channels, 1))

    def forward(self, X):
        self.X = X
        (batch_size, _, in_height, in_width) = X.shape
        out_height = (in_height - self.kernel_size + 2 * self.padding) // self.stride + 1
        out_width = (in_width - self.kernel_size + 2 * self.padding) // self.stride + 1

        self.X_padded = np.pad(X, ((0, 0), (0, 0), (self.padding, self.padding), (self.padding, self.padding)), 'constant')
        self.output = np.zeros((batch_size, self.out_channels, out_height, out_width))

        for i in range(out_height):
            for j in range(out_width):
                h_start, w_start = i * self.stride, j * self.stride
                h_end, w_end = h_start + self.kernel_size, w_start + self.kernel_size
                X_slice = self.X_padded[:, :, h_start:h_end, w_start:w_end]
                for k in range(self.out_channels):
                    self.output[:, k, i, j] = np.sum(X_slice * self.kernels[k, :, :, :], axis=(1, 2, 3)) + self.biases[k]
        return self.output

    def backward(self, d_output, learning_rate):
        (batch_size, _, out_height, out_width) = d_output.shape
        d_kernels = np.zeros_like(self.kernels)
        d_biases = np.zeros_like(self.biases)
        d_X_padded = np.zeros_like(self.X_padded)

        for i in range(out_height):
            for j in range(out_width):
                h_start, w_start = i * self.stride, j * self.stride
                h_end, w_end = h_start + self.kernel_size, w_start + self.kernel_size
                X_slice = self.X_padded[:, :, h_start:h_end, w_start:w_end]
                for k in range(self.out_channels):
                    d_kernels[k] += np.sum(X_slice * d_output[:, k, i, j][:, np.newaxis, np.newaxis, np.newaxis], axis=0)
                    d_X_padded[:, :, h_start:h_end, w_start:w_end] += self.kernels[k] * d_output[:, k, i, j][:, np.newaxis, np.newaxis, np.newaxis]
        
        d_biases = np.sum(d_output, axis=(0, 2, 3)).reshape(-1, 1)

        self.kernels -= learning_rate * d_kernels / batch_size
        self.biases -= learning_rate * d_biases / batch_size

        if self.padding > 0:
            return d_X_padded[:, :, self.padding:-self.padding, self.padding:-self.padding]
        return d_X_padded

class PoolLayer:
    def __init__(self, kernel_size, stride=2):
        self.kernel_size = kernel_size
        self.stride = stride

    def forward(self, X):
        self.X = X
        (batch_size, in_channels, in_height, in_width) = X.shape
        out_height = (in_height - self.kernel_size) // self.stride + 1
        out_width = (in_width - self.kernel_size) // self.stride + 1
        output = np.zeros((batch_size, in_channels, out_height, out_width))

        for i in range(out_height):
            for j in range(out_width):
                h_start, w_start = i * self.stride, j * self.stride
                h_end, w_end = h_start + self.kernel_size, w_start + self.kernel_size
                X_slice = X[:, :, h_start:h_end, w_start:w_end]
                output[:, :, i, j] = np.max(X_slice, axis=(2, 3))
        return output

    def backward(self, d_output):
        (batch_size, in_channels, out_height, out_width) = d_output.shape
        d_X = np.zeros_like(self.X)

        for i in range(out_height):
            for j in range(out_width):
                h_start, w_start = i * self.stride, j * self.stride
                h_end, w_end = h_start + self.kernel_size, w_start + self.kernel_size
                X_slice = self.X[:, :, h_start:h_end, w_start:w_end]
                mask = (X_slice == np.max(X_slice, axis=(2, 3))[:, :, np.newaxis, np.newaxis])
                d_X[:, :, h_start:h_end, w_start:w_end] += mask * d_output[:, :, i, j][:, :, np.newaxis, np.newaxis]
        return d_X

class FCLayer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.1
        self.biases = np.zeros((1, output_size))

    def forward(self, X):
        self.input = X
        return np.dot(X, self.weights) + self.biases

    def backward(self, d_output, learning_rate):
        d_weights = np.dot(self.input.T, d_output)
        d_biases = np.sum(d_output, axis=0, keepdims=True)
        d_input = np.dot(d_output, self.weights.T)

        self.weights -= learning_rate * d_weights
        self.biases -= learning_rate * d_biases
        return d_input

class CNN:
    def __init__(self):
        self.conv1 = ConvLayer(in_channels=1, out_channels=2, kernel_size=3, padding=1)
        self.pool1 = PoolLayer(kernel_size=2)
        self.fc1 = FCLayer(input_size=2 * 2 * 2, output_size=2)

    def forward(self, X):
        self.conv1_out = self.conv1.forward(X)
        self.pool1_out = self.pool1.forward(self.conv1_out)
        self.pool1_out_flat = self.pool1_out.reshape(self.pool1_out.shape[0], -1)
        return self.fc1.forward(self.pool1_out_flat)

    def backward(self, d_output, learning_rate):
        d_fc1 = self.fc1.backward(d_output, learning_rate)
        d_pool1_out_flat = d_fc1.reshape(self.pool1_out.shape)
        d_conv1_out = self.pool1.backward(d_pool1_out_flat)
        self.conv1.backward(d_conv1_out, learning_rate)

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            loss, p = cross_entropy_loss(output, y)
            
            # Backward pass
            d_output = p
            d_output[range(y.shape[0]), y] -= 1
            d_output /= y.shape[0]
            
            self.backward(d_output, learning_rate)

            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")

if __name__ == '__main__':
    # Toy dataset: 4x4 images, class 0 (vertical line), class 1 (horizontal line)
    X = np.array([
        [[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]],
        [[[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]],
        [[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]],
        [[[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]]
    ])
    y = np.array([0, 1, 0, 1])

    cnn = CNN()
    cnn.train(X, y, epochs=101, learning_rate=0.1)

    # Test
    test_img = np.array([[[[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]]])
    prediction = cnn.forward(test_img)
    print("\nTest prediction:", np.argmax(softmax(prediction)))
