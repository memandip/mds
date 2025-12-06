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

if __name__ == '__main__':
    # Toy data
    X = np.random.randn(1, 1, 5, 5)  # 1 image, 1 channel, 5x5
    conv = ConvLayer(in_channels=1, out_channels=3, kernel_size=3)
    output = conv.forward(X)
    print("Input shape:", X.shape)
    print("Output shape:", output.shape)
