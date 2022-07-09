import warnings
import pandas as pd
from sklearn import preprocessing
warnings.simplefilter(action='ignore', category=FutureWarning)


class Preprocessing:
    def __init__(self, df):
        self.df = df

    def isnumber(self, x):
        try:
            float(x)
            return True
        except:
            return False

    def run(self):

        # Over the Columns:
        for i in self.df.columns:
            # remove the id column if exists:
            if i.lower() == 'id':
                self.df.drop(columns=self.df.columns[self.df.columns.get_loc(i)], axis=1, inplace=True)

            # Make sure the class column is the last column:
            if i.lower() == 'class':
                if self.df.columns.get_loc(i) == self.df.columns.size - 1:
                    pass
                else:
                    column = self.df[[i]]
                    self.df.drop(columns=self.df.columns[self.df.columns.get_loc(i)], axis=1, inplace=True)
                    self.df = self.df.join(column)

        # in case one column has one value for all samples:
        for i in self.df.columns:
            List = self.df[i].to_list()
            if all(element == List[0] for element in List):
                self.df.drop(columns=self.df.columns[self.df.columns.get_loc(i)], axis=1, inplace=True)
            else:
                pass

        # replace all non-numeric entries with NaN in a pandas dataframe:
        self.df.iloc[:, :-1] = self.df.iloc[:, :-1][self.df.iloc[:, :-1].applymap(self.isnumber)]

        # replace nan values with average of columns:
        self.df.fillna(self.df.mean())

        # as a confirmation, convert the dataset to the type float:
        self.df.iloc[:, :-1] = self.df.iloc[:, :-1].apply(pd.to_numeric)

        '''
        # normalize the features values of the given dataset:
        names = [col for col in self.df.columns]
        lastColumn = self.df.iloc[:, -1]
        x = self.df.iloc[:, :-1].values  # returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        df = pd.DataFrame(x_scaled)
        df = df.join(lastColumn)
        df.columns = names
        '''
        return self.df
