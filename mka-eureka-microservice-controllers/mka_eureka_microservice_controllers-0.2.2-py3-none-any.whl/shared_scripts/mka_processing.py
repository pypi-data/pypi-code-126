import pandas as pd
import pathlib
# region Factorizing categorical columns
# This funcation will replace any categorical(object) feature with numbers for example (gender (F,M) 1,-1)
def factorize(_dataFrame):
    _copied = pd.DataFrame.copy(_dataFrame)
    for col in _dataFrame.columns:
        if _copied[col].dtype != 'int64' and _copied[col].dtype != 'float64':
            _copied[col], unique = pd.factorize(_copied[col])
    return _copied


# endregion Factorizing categorical columns


    
def GetTemplateGuidFromPath(path): 
    '''
    ----------
    Definition
    ----------
        Return template name from given path \n
        template name is the top level folder from given path

    ----------
    Example
    ----------
            path='123/usr/home/dataframe.xlsx'
            GetTemplateGuidFromPath(path) ----> 123

    ----------
    Parameters
    ----------
    files_list :list non empty files objects from user,``required``

    template_guid : str ,``required``
        parameter specify the folder that will be file saved in

    source : str ,``required``
        parameter return file content if source(reuqest) 'from_service'

    '''
    return pathlib.Path(path).parts[0]
