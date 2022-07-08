# LSTM Model
from torch import nn

class RegressionLSTM(nn.Module):
    # the model only requires the number of features and the number of hidden units
    # to define the shape of the LSTM
    def __init__(self, num_features, hidden_units):
        super().__init__()
        self.num_features = num_features 
        self.hidden_units = hidden_units
        self.num_layers = 1 # a single LSTM layer is used

        # with the previously assigned parameters of the model
        # the different components are initialized
        self.lstm = nn.LSTM(
            input_size = num_features,
            hidden_size = hidden_units,
            batch_first = True,
            num_layers = self.num_layers
        )

        self.linear = nn.Linear(in_features=self.hidden_units, out_features=1) # check the linear layer in the figure

    # the forward pass receives the input data and passes it through the network
    def forward(self, x):
        _, (hn, cn) = self.lstm(x) # i#nputs are passed to the LSTM.
                                   # As described in the documentation the "output" contains the the hidden
                                   # state for each element in the sequence of the last layer of the lstm
                                   # therefore it is not used

        out = hn[-1]    # hn contains the final hidden state of each example of the batch,
                        # hn[-1] is used to reshape the outputs
    
        out = self.linear(out) # y_hat is calculate through the linear layer using hn[-1]

        return out.reshape(-1), hn[-1], cn[-1] # returns y_hat (as a column), hn[-1] the last hidden state,
                                               # and cn[-1] the last cell state