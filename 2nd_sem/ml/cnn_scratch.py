import numpy as np

class ConvLayer:
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

        # Initialize kernels (filters)
        self.kernels = np.random.randn(out_channels, in_channels, kernel_size, kernel_size)
        self.biases = np.zeros((out_channels, 1))

    def forward(self, X):
        # Input dimensions
        (batch_size, in_channels, in_height, in_width) = X.shape

        # Output dimensions
        out_height = (in_height - self.kernel_size + 2 * self.padding) // self.stride + 1
        out_width = (in_width - self.kernel_size + 2 * self.padding) // self.stride + 1

        # Padded input
        X_padded = np.pad(X, ((0, 0), (0, 0), (self.padding, self.padding), (self.padding, self.padding)), 'constant')

        # Initialize output
        output = np.zeros((batch_size, self.out_channels, out_height, out_width))

        # Perform convolution
        for i in range(out_height):
            for j in range(out_width):
                h_start = i * self.stride
                h_end = h_start + self.kernel_size
                w_start = j * self.stride
                w_end = w_start + self.kernel_size

                # Slice the input
                X_slice = X_padded[:, :, h_start:h_end, w_start:w_end]

                # Convolve
                for k in range(self.out_channels):
                    output[:, k, i, j] = np.sum(X_slice * self.kernels[k, :, :, :], axis=(1, 2, 3))

        return output

class PoolLayer:
    def __init__(self, kernel_size, stride=2):
        self.kernel_size = kernel_size
        self.stride = stride

    def forward(self, X):
        # Input dimensions
        (batch_size, in_channels, in_height, in_width) = X.shape

        # Output dimensions
        out_height = (in_height - self.kernel_size) // self.stride + 1
        out_width = (in_width - self.kernel_size) // self.stride + 1

        # Initialize output
        output = np.zeros((batch_size, in_channels, out_height, out_width))

        # Perform pooling
        for i in range(out_height):
            for j in range(out_width):
                h_start = i * self.stride
                h_end = h_start + self.kernel_size
                w_start = j * self.stride
                w_end = w_start + self.kernel_size

                # Slice the input
                X_slice = X[:, :, h_start:h_end, w_start:w_end]

                # Pool
                output[:, :, i, j] = np.max(X_slice, axis=(2, 3))

        return output

class FCLayer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size)
        self.biases = np.zeros((1, output_size))

    def forward(self, X):
        self.input = X
        return np.dot(X, self.weights) + self.biases

class CNN:
    def __init__(self):
        self.conv1 = ConvLayer(in_channels=1, out_channels=3, kernel_size=3)
        self.pool1 = PoolLayer(kernel_size=2)
        self.fc1 = FCLayer(input_size=3 * 4 * 4, output_size=10) # Adjusted input size

    def forward(self, X):
        # Convolution and pooling
        x = self.conv1.forward(X)
        x = self.pool1.forward(x)

        # Flatten
        x = x.reshape(x.shape[0], -1)

        # Fully connected layer
        x = self.fc1.forward(x)
        return x

if __name__ == '__main__':
    # Toy data
    X = np.random.randn(1, 1, 10, 10)  # 1 image, 1 channel, 10x10
    
    cnn = CNN()
    output = cnn.forward(X)

    print("Input shape:", X.shape)
    print("Final output shape:", output.shape)
