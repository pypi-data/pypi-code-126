# TODO: import necessary libraries
from .Generaldistribution import Distribution
import math
import matplotlib.pyplot as plt


class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """

    def __init__(self, p, n, mu=0, sigma=1):
        Distribution.__init__(self, mu, sigma)
        self.p = p
        self.n = n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        return self.p * self.n

    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        return math.sqrt(self.n * self.p * (1 - self.p))

    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """

        self.read_data_file('numbers_binomial.txt')
        self.n = len(self.data)
        self.p = sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.hist(self.data)
        plt.show()

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        return (self.p**k)*((1-self.p)**(self.n-k)) * math.factorial(self.n)/(math.factorial(k)*math.factorial(self.n-k))

    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        x = [k for k in range(self.n)]
        y = [self.pdf(k) for k in range(self.n)]
        plt.bar(x=x, y=y)
        plt.show()

        return x, y

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        n = self.n + other.n
        p = self.p
        return Binomial(p, n)

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
    
        return f'mean: {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}'
