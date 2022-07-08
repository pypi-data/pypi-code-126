#skweness  Enherafffn  https://www.analyticsvidhya.com/blog/2021/05/shape-of-data-skewness-and-kurtosis/
#kurtosis taffartoh   https://www.analyticsvidhya.com/blog/2021/05/shape-of-data-skewness-and-kurtosis/s

StatisticsDictionary = {
    #الالتواء
    "Skewness": {
        "Definition": "Skewness is a degree of asymmetry observed in a probability distribution that deviates from the symmetrical normal distribution (bell curve) in a given set of data.",
        "Example": "When data is symmetrically distributed, the left-hand side, and right-hand side, contain the same number of observations.mean=median=mode"
                   " (If the dataset has 100 values, then the left-hand side has 50 observations, and the right-hand side has 50 observations.)"
                   "But, what if not symmetrical distributed? That data is called asymmetrical data",
        "Types":["Negative skewed or left-skewed","Positive skewed or right-skewed"],
        "Hints":"If the skewness is between -0.5 & 0.5, the data are nearly symmetrical."
                "If the skewness is between -1 & -0.5 (negative skewed) or between 0.5 & 1(positive skewed), the data are slightly skewed"
                ".the skewness is lower than -1 (negative skewed) or greater than 1 (positive skewed), the data are extremely skewed."
        },

    "Kurtosis":{
        "Definition":"Kurtosis refers to the degree of presence of outliers in the distribution.",
        "Example":"",
        "Types":["Leptokurtic or heavy-tailed distribution (kurtosis more than normal distribution) >3","Mesokurtic (kurtosis same as the normal distribution).","Platykurtic or short-tailed distribution (kurtosis less than normal distribution)."],

        "Hints":"Leptokurtic (kurtosis > 3) Leptokurtic is having very long and skinny tails, which means there are more chances of 'outliers'. Positive values of kurtosis indicate that distribution is peaked and possesses thick tails. An extreme positive kurtosis indicates a distribution where more of the numbers are located in the tails of the distribution instead of around the mean."
                "Mesokurtic is the same as the normal distribution, which means kurtosis is near to 0. In Mesokurtic, distributions are moderate in breadth, and curves are a medium peaked height."
                "Platykurtic having a lower tail and stretched around center tails means most of the data points are present in high proximity with mean. A platykurtic distribution is flatter (less peaked) when compared with the normal distribution"
    },
    "Stability":{
        "Definition":"Measures how stable or constant this column is. The number of rows with the most frequent non-missing value divided by the total number of data rows with non-missing values."
    },
    "Missing":{
        "Definition":"The number of missing values in this column as a fraction of the total number of data rows"
    },
    "Outlier":{
        "Definition":"Extreme values that fall a long way outside of the other observations,its have negative effect on the model"
    },
    "Correlation (C)":{
        "Definition":"Measures the linear correlation between the data column and the target column. This quality bar is only available when the task is 'Predict'.",
                        "Example":"Low Correlation: a correlation of less than 0.01% indicates that this column is not likely to contribute to the predictions. While keeping such a column is not problematic, removing it may speed up the model building."
                                "High Correlation: a correlation of more than 40% may be an indicator for information you don't have at prediction time. In that case, you should remove this column. Sometimes, however, the prediction problem is simple, and you will get a better model when the column is included. Only you can decide."
    },
    "Idness (I)":{"Definition":" measures the degree to which this Attribute resembles an ID. The number of different values for the Attribute divided by the number of data rows."},
    'Mean Absolute Error(MAE)':{'Definition':'MAE is a very simple metric which calculates the absolute difference between actual and predicted values then sum all the errors and divide them by a total number of observations,and we aim to get the minimum MAE',
                                   'Examples' :['most Robust to outliers','Use MAE if you do not want to penalize large prediction errors.','common metrics used to measure accuracy for continuous variables']
                                },
    'Mean Squared Error (MSE)' :{'Definition':'It represents the squared distance between actual and predicted values. we perform squared to avoid the cancellation of negative terms and it is the benefit of MSE.',
                                'Examples': ['not Robust to outliers',
                                            'it is always a positive value',
                                            '0 means the model is perfect',
                                            'The smaller the mean squared error ,The closer you are to finding the line of best fit. Depending on your data',
                                            'When a model has no error, the MSE equals zero',
                                            'As model error increases, MSE value increases',
                                            'MSE gives larger penalization to big prediction error by square it while MAE treats all errors the same.',
                                            'For an ideal model, RMSE/MAE=0',
                                            ]    
                            },
    'Root Mean Squared Error(RMSE)':{'Definition':'It represents the root squared distance between actual and predicted values. we perform squared to avoid the cancellation of negative terms and it is the benefit of MSE.',
                                    'Examples': ['The RMSE will always be larger or equal to the MAE',
                                                'If the RMSE=MAE, then all the errors are of the same magnitude',
                                                'Both the MAE and RMSE can range from 0 to ∞.'
                                                'If RMSE>MAE, then there is variation in the errors.',
                                                'If the RMSE-MAE difference was isnt large enough so no need to indicate the presence of very large errors.',
                                                'one distinct advantage of RMSE over MAE is that RMSE avoids the use of taking the absolute value, which is undesirable in many mathematical calculations ',
]
                                },
}

##Generalized Linear Model: generalization of linear regression models
# Deep Learning: multi-level neural network for learning non-linear relationships
# Decision Tree: finds simple tree-like models which are easy to understand
# Random Forest: ensemble of multiple randomized trees
# Gradient Boosted Trees: powerful but complex model using ensembles of decision trees
# Support Vector Machine: powerful but relatively fast model, especially for non-linear relationships