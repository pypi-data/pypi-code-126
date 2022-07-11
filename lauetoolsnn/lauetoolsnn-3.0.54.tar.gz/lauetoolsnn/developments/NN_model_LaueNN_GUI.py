# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:46:07 2022

@author: PURUSHOT

Numpy neural network implementation of the DNN model used in LaueNN GUI
Note: This does not include any kernel or bias regularization terms 
For larger output models please install tensorflow


Activate: Relu
Dropout: 0.3
optimizer: Adam (with learning rate)
Loss: categorical_crossentropy

For other models such as CNN, install tensorflow and keras 

"""   
import numpy as np
# =============================================================================
# Activation functions for forward and backward pass
# define new if required
# =============================================================================
def relu(Z):
    return np.maximum(0,Z)

def relu_backward(dA, Z):
    dZ = np.array(dA, copy = True)
    dZ[Z <= 0] = 0
    return dZ

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
# =============================================================================
# A full forward pass
# =============================================================================
def single_layer_forward_propagation(A_prev, W_curr, b_curr, activation="relu"):
    # calculation of the input value for the activation function
    Z_curr = np.dot(W_curr, A_prev) + b_curr

    # selection of activation function
    if activation == "relu":
        activation_func = relu
    else:
        raise Exception('Non-supported activation function')
        
    # return of calculated activation A and the intermediate Z matrix
    return activation_func(Z_curr), Z_curr

def full_forward_propagation(X, params_values, nn_architecture):
    # creating a temporary memory to store the information needed for a backward step
    memory = {}
    # X vector is the activation for layer 0 
    A_curr = X
    
    # iteration over network layers
    for idx, layer in enumerate(nn_architecture):
        # we number network layers from 1
        layer_idx = idx + 1
        # transfer the activation from the previous iteration
        A_prev = A_curr
        
        # extraction of the activation function for the current layer
        activ_function_curr = layer["activation"]
        # extraction of W for the current layer
        W_curr = params_values["W" + str(layer_idx)]
        # extraction of b for the current layer
        b_curr = params_values["b" + str(layer_idx)]
        # calculation of activation for the current layer
        A_curr, Z_curr = single_layer_forward_propagation(A_prev, W_curr, b_curr, activ_function_curr)
        
        # saving calculated values in the memory
        memory["A" + str(idx)] = A_prev
        memory["Z" + str(layer_idx)] = Z_curr

    # return of prediction vector and a dictionary containing intermediate values
    return A_curr, memory
# =============================================================================
# A full Backward propagation pass
# =============================================================================
def single_layer_backward_propagation(dA_curr, W_curr, b_curr, Z_curr, A_prev, activation="relu"):
    # number of examples
    m = A_prev.shape[1]
    
    # selection of activation function
    if activation == "relu":
        backward_activation_func = relu_backward
    else:
        raise Exception('Non-supported activation function')
    
    # calculation of the activation function derivative
    dZ_curr = backward_activation_func(dA_curr, Z_curr)
    
    # derivative of the matrix W
    dW_curr = np.dot(dZ_curr, A_prev.T) / m
    # derivative of the vector b
    db_curr = np.sum(dZ_curr, axis=1, keepdims=True) / m
    # derivative of the matrix A_prev
    dA_prev = np.dot(W_curr.T, dZ_curr)

    return dA_prev, dW_curr, db_curr

def full_backward_propagation(Y_hat, Y, memory, params_values, nn_architecture):
    grads_values = {}
    # number of examples
    m = Y.shape[1]
    # a hack ensuring the same shape of the prediction vector and labels vector
    Y = Y.reshape(Y_hat.shape)
    
    # initiation of gradient descent algorithm
    dA_prev = - (np.divide(Y, Y_hat) - np.divide(1 - Y, 1 - Y_hat));
    
    for layer_idx_prev, layer in reversed(list(enumerate(nn_architecture))):
        # we number network layers from 1
        layer_idx_curr = layer_idx_prev + 1
        # extraction of the activation function for the current layer
        activ_function_curr = layer["activation"]
        
        dA_curr = dA_prev
        
        A_prev = memory["A" + str(layer_idx_prev)]
        Z_curr = memory["Z" + str(layer_idx_curr)]
        
        W_curr = params_values["W" + str(layer_idx_curr)]
        b_curr = params_values["b" + str(layer_idx_curr)]
        
        dA_prev, dW_curr, db_curr = single_layer_backward_propagation(
            dA_curr, W_curr, b_curr, Z_curr, A_prev, activ_function_curr)
        
        grads_values["dW" + str(layer_idx_curr)] = dW_curr
        grads_values["db" + str(layer_idx_curr)] = db_curr
    
    return grads_values

def init_layers(nn_architecture, seed = 99):
    # random seed initiation
    np.random.seed(seed)
    # parameters storage initiation
    params_values = {}
    # iteration over network layers
    for idx, layer in enumerate(nn_architecture):
        # we number network layers from 1
        layer_idx = idx + 1

        # extracting the number of units in layers
        layer_input_size = layer["input_dim"]
        layer_output_size = layer["output_dim"]
        
        # initiating the values of the W matrix
        # and vector b for subsequent layers
        params_values['W' + str(layer_idx)] = np.random.randn(layer_output_size, layer_input_size) * 0.0005
        params_values['b' + str(layer_idx)] = np.random.randn(layer_output_size, 1) * 0.0005
        
    return params_values

# =============================================================================
# Update parameters
# =============================================================================
def update(params_values, grads_values, nn_architecture, learning_rate):
    # iteration over network layers
    for layer_idx, layer in enumerate(nn_architecture, 1):
        params_values["W" + str(layer_idx)] -= learning_rate * grads_values["dW" + str(layer_idx)]        
        params_values["b" + str(layer_idx)] -= learning_rate * grads_values["db" + str(layer_idx)]
    return params_values

# =============================================================================
# Loss function / cost function
# =============================================================================
def get_cost_value(Y_hat, Y):
    # number of examples
    m = Y_hat.shape[1]
    # calculation of the cost according to the formula
    cost = -1 / m * (np.dot(Y, np.log(Y_hat).T) + np.dot(1 - Y, np.log(1 - Y_hat).T))
    return np.squeeze(cost)

# =============================================================================
# Calculating accuracy
# =============================================================================
# an auxiliary function that converts probability into class
def convert_prob_into_class(probs):
    probs_ = np.copy(probs)
    probs_[probs_ > 0.5] = 1
    probs_[probs_ <= 0.5] = 0
    return probs_

def get_accuracy_value(Y_hat, Y):
    Y_hat_ = convert_prob_into_class(Y_hat)
    return (Y_hat_ == Y).all(axis=0).mean()
#%%
# =============================================================================
# Load training dataset
# =============================================================================
import sys
sys.path.append(r"C:\Users\purushot\Desktop\github_version_simple\lauetoolsnn")
from utils_lauenn import array_generator_verify, array_generator
import _pickle as cPickle


classhkl = np.load(r"C:\Users\purushot\Desktop\github_version_simple\lauetoolsnn\models\GaN_Si\MOD_grain_classhkl_angbin.npz")["arr_0"]
angbins = np.load(r"C:\Users\purushot\Desktop\github_version_simple\lauetoolsnn\models\GaN_Si\MOD_grain_classhkl_angbin.npz")["arr_1"]
loc_new = np.load(r"C:\Users\purushot\Desktop\github_version_simple\lauetoolsnn\models\GaN_Si\MOD_grain_classhkl_angbin.npz")["arr_2"]
with open(r"C:\Users\purushot\Desktop\github_version_simple\lauetoolsnn\models\GaN_Si\class_weights.pickle", "rb") as input_file:
    class_weights = cPickle.load(input_file)
class_weights = class_weights[0]

batch_size = 50
## Load generator objects from filepaths
training_data_generator = array_generator(r"C:\Users\purushot\Desktop\github_version_simple\lauetoolsnn\models\GaN_Si\training_data", 
                                          batch_size, \
                                          len(classhkl), loc_new, print)

    
    
#%%

n_bins = 1201
n_outputs = 120
param = n_outputs
    
nn_architecture = [
                    {"input_dim": n_bins, "output_dim": n_bins, "activation": "relu"},
                    {"input_dim": n_bins, "output_dim": ((param)*15 + n_bins)//2, "activation": "relu"},
                    {"input_dim": ((param)*15 + n_bins)//2, "output_dim": (param)*15, "activation": "relu"},
                    {"input_dim": (param)*15, "output_dim": n_outputs, "activation": "softmax"},
                    ]


params_values = init_layers(nn_architecture, np.random.randint(1e6))

learning_rate = 0.001
verbose = True
callback = None
# initiation of lists storing the history 
# of metrics calculated during the learning process 
cost_history = []
accuracy_history = []


# performing calculations for subsequent iterations
for ii in range(5):
    X1, Y1 = next(training_data_generator)
    for i in range(len(X1)): 
        X, Y = X1[i,:], Y1[i,:]
        # step forward
        Y_hat, cashe = full_forward_propagation(X, params_values, nn_architecture)
        
        # calculating metrics and saving them in history
        cost = get_cost_value(Y_hat, Y)
        cost_history.append(cost)
        accuracy = get_accuracy_value(Y_hat, Y)
        accuracy_history.append(accuracy)
        
        # step backward - calculating gradient
        grads_values = full_backward_propagation(Y_hat, Y, cashe, params_values, nn_architecture)
        # updating model state
        params_values = update(params_values, grads_values, nn_architecture, learning_rate)
        
        if(i % 50 == 0):
            if(verbose):
                print("Iteration: {:05} - cost: {:.5f} - accuracy: {:.5f}".format(ii, cost, accuracy))
            if(callback is not None):
                callback(i, params_values)






















