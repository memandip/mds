import numpy as np
import pandas as pd

class LinearRegression:
    def __init__(self, X: pd.DataFrame, y: np.ndarray):
        self.params = {}
        self.m, self.n = X.shape
        self.params["w"] = np.random.randn(self.n, 1) * 0.001
        self.params["b"] = np.zeros(1)
        
        self.X = X
        self.y = y
        self.result = pd.DataFrame()

    def train(self, alpha = 0.001, epochs = 10):
        for epoch in range(epochs):
            print("Epoch:", epoch, end="")
            z = np.dot(self.X, self.params["w"]) + self.params["b"]
            
            self.y_pred = self.sigmoid(z)
            
            self.result[0] = self.y
            
            # Update the parameters
            self.params["W"] = self.params["W"] - alpha * 1/self.m * np.dot(self.X.transpose(), (self.y_pred - np.reshape(self.y, (self.m, 1))))
            self.params["b"] = self.params["b"] - alpha * 1/self.m * np.sum(self.y_pred - np.reshape(self.y, (self.m, 1)))
            
            self.y_pred = self.sigmoid(np.dot(self.X, self.params["W"]) + self.params["b"])
            loss = self.loss(self.y, self.y_pred)
            
            self.result[1] = self.y_pred
            self.result[2] = loss
        
        print(",Final Loss:", loss)
        print(f"Final Weights: {self.params['W']}, Final Bias: {self.params['b']}")
    
    def loss(self, y: np.ndarray, y_pred: np.ndarray):
        # print(np.log(1-y_pred))
        y_zero_loss = y.T.dot(np.log(y_pred))
        y_one_loss = (1 - y).T.dot(np.log(1 - y_pred))
        
        return -np.sum(y_zero_loss + y_one_loss) / len(y)
    
    def sigmoid(self, z: np.ndarray):
        return 1 / (1 + np.exp(-z))
    
    def predict(self, X: pd.DataFrame):
        return self.sigmoid(np.dot(X, self.params["w"]) + self.params["b"])
    