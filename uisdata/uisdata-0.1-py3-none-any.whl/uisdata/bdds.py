from io import BytesIO
from io import StringIO
from zipfile import ZipFile
import re
import requests  # Dependency
import pandas as pd  # Dependency
import numpy as np  # Dependency


class bdds:
    """The bdds Class allows direct access to all BDDS archive
    It contains methods facilitating the production of subsets with labels and metadata
    To instantiate the class pick a UIS dataset from the list below 
    (use the name in quote excluding the parenthesis). Full walkthrough available at
    https://datalore.jetbrains.com/notebook/FaD1hIZ0s0XKrlZcWTMYVW/UrrXOcYJWCstRNMNPvzzPF/

    Parameter
    ----------
    datasetName : 
        {'SDG': 'Sustainable Development Goal (SDG 4)',
         'SDG11': 'Sustainable Development Goal (SDG 11)',
         'OPRI': 'Other Policy Relevant Indicators',
         'SCI': 'Research and Development (R&D) SDG 9.5',
         'DEM': 'Demographic and Socio-economic Indicators',
         'EDUNONCORE': 'Education Non Core Archive February 2020',
         'SCIARCHIVE': 'Research and Development (R&D) Archive March 2021',
         'INNOARCHIVE': 'Innovation Archive April 2017',
         'CLTEARCHIVE': 'Cultural employment Archive June 2019',
         'CLTTARCHIVE': 'Cultural trade Archive June 2021',
         'FILMARCHIVE': 'Feature Film Archive June 2019'}.

    Once the class is instantiated with a specific dataset, the following methods can be called:
    zipToLocalDir,
    dataTables:
        readmeFile,
        subsetData,
        longToWide,
        addMetadata,
        addLabel,
        allLabelMerge,
        subsetMetaDict,
        allMetaMerge,
        allLabelMetaMerge,
        uniqueVal,
        searchList,
        searchList_II.

    Note that the dataTables method is parent to all the following methods.
    """

    # Intantiate the class
    def __init__(self, datasetName):
        # Call get_URLandDate to return the archive URL and the dict keys (all available instantiate value)
        self.dsName = str(datasetName)
        # DataSet name length passed to dataTable method
        self.dsNameLength = len(datasetName) + 1
        try:
            # Get_URLandDate outputs a tuple
            self.url, self.updateDate = self.get_URLandDate()
        # Catch key error (wrong archive name) and return a list of available archive name
        except KeyError:
            raise KeyError(
                f'{self.dsName}, is not a valid BDDS archive name, please pick one from the following list (see class Docstring for more details): {self.dictKeyList}') from None
        # return a notification if can't connect to internet to retrieve url and release date (error type from requests module)
        except requests.exceptions.ConnectionError:
            print(
                "-- Cannot connect to internet. You will only be able to work with a local BDDS archive. To work with the online archives, reconnect to the internet and then re-instantiate the class")

    def get_URLandDate(self):
        """Get the URL and latest release date of the specified BDDS archive

        Parameter
        ----------
            none

        Returns
        -------
            a tuple of strings
                the url of the chosen bdds archive and the latest release date
        """
        # !!! Hardcoded URL for metadata file.
        # Note the name of each dataset in the file e.g. SDG...
        # ...must be exactly as the name of files prefix in SDG_DATA_NATIONAL.csv
        csv_url = "https://apimgmtstzgjpfeq2u763lag.blob.core.windows.net/content/MediaLibrary/python/BDDS_DatasetList_Name-URL.csv"
        urlData = requests.get(csv_url).content  # download file @ url location returns URL response object
        dsNameURLdf = pd.read_csv(StringIO(urlData.decode('utf-8')))  # transform URL object to text CSV file and read as a dataFrame
        dsNameURLdict = dict(zip(dsNameURLdf.dataset, dsNameURLdf.url))  # transforms the dataFrame's archive URL to a dict
        dsNameUpdatedict = dict(zip(dsNameURLdf.dataset, dsNameURLdf.release_date))  # transforms the dataFrame's release dates to a dict
        self.dictKeyList = list(dsNameURLdict.keys())  # list of dict keys (valid archive names) used in init when catching KeyError
        self.dictNameLabel = dict(zip(dsNameURLdf.dataset, dsNameURLdf.dataset_name))
        dsURL = dsNameURLdict[self.dsName]  # gets the specified archive's URL from dict
        dsUpdateDate = dsNameUpdatedict[self.dsName]  # gets the specified archive's latest update date from dict
        return dsURL, dsUpdateDate

    def zipToLocalDir(self, localDir):
        """Download a BDDS Zip archive to your local drive

        Parameter
        ----------
            localDir: Str
                a string; the full path where the zip archive is saved
                e.g. "C:\\Desktop\\"

        Returns
        -------
            ZIP
                a ZIP file containing a specific BDDS archive to your local drive
        """
        r = requests.get(self.url)
        with open(localDir + self.dsName + ".zip", 'wb') as f:
            f.write(r.content)

    def dataTables(self, localDir=None):
        """Access a Zip archive with 2 options: locally (will also notify user if a newer archive version is available)
        or online from the BDDS repo. Returns a dictionary of all the data files

        Parameter
        ----------
            localDir: str default is None
                a string; the full path where the zip archive is saved e.g. "C:\Desktop\SDG.zip"
                Default is None and the archive will be accessed online from the BDDS repo

        Returns
        -------
            dict
                a dictionary of dataFrames (all data files contained in a BDDS archive)
        """
        if localDir:
            print("-- localDir parameter specified, accessing ZIP archive locally")
            # Access local ZIP archive and and extract a list of file names from the zip
            self.read_URL_ZIP = ZipFile(localDir)  # read file-like object as zip file
            self.zip_File_List = self.read_URL_ZIP.namelist()  # listing names of files in the zip

            try:
                # Within a try, because being offline raises an attribute error since updateDate is not available
                # Get README file from archive and extract update date
                localReadme = self.readmeFile()  # get local archive release date
                # From README string, find sep ('Release date: '), return first 7 units of string to the right of sep
                left, sep, right = localReadme.partition('Release date: ')
                if sep:
                    releaseDate = (right[:7])
                    # print(releaseDate, self.updateDate)
                if not releaseDate == self.updateDate:  # compare local date to date fetched from current online repo (set in ini)
                    print("-- Notice: you are not working with the latest, *** ",
                          self.dsName, " *** archive you can download the most recent version here:\n ", self.url,
                          "\n or use the zipToLocalDir class method to download the latest version to your local drive, alternatively you can work purely online by omitting the localDir parameter in the dataTables method")
                else:
                    print("-- Notice: you are working with the most recent *** ", self.dsName,
                          " *** archive, released on: ", self.updateDate)
            except AttributeError:
                pass
        else:
            print("-- localDir parameter not specified, accessing ZIP archive from the BDDS online repo")
            # Download ZIP from BDDS repo and extract a list of file names from the zip
            get_URL_object = requests.get(self.url)  # download file @ url location returns URL response object
            read_URL = BytesIO(get_URL_object.content)  # gives file-like access to URL response object
            self.read_URL_ZIP = ZipFile(read_URL)  # read file-like object as zip file
            self.zip_File_List = self.read_URL_ZIP.namelist()  # listing names of files in the zip

        # Produce a dictionary containing all tables as dataFrame
        dataset_dict = {}
        for name in self.zip_File_List:
            if not str.lower("README") in str.lower(name):  # if name of file doesn't contain README
                asString = self.read_URL_ZIP.read(name).decode('utf8')  # read and decode specific list item as string
                readString = StringIO(asString)  # give file-like access to string
                df = pd.read_csv(readString, low_memory=False)  # read as a Pandas dataFrame
                trim_name = name[self.dsNameLength:-4]  # remove specific DS name and file extension from df name
                dataset_dict[trim_name] = df  # add dataFrame to dataset_dict

        # Additional data cleaning to mitigate human error from special releases; remove white space
        dataset_dict["DATA_NATIONAL"]["INDICATOR_ID"] = dataset_dict["DATA_NATIONAL"][
            "INDICATOR_ID"].str.strip().str.upper()
        dataset_dict["DATA_NATIONAL"]["COUNTRY_ID"] = dataset_dict["DATA_NATIONAL"][
            "COUNTRY_ID"].str.strip().str.upper()
        dataset_dict["LABEL"]["INDICATOR_ID"] = dataset_dict["LABEL"]["INDICATOR_ID"].str.strip().str.upper()
        dataset_dict["COUNTRY"]["COUNTRY_ID"] = dataset_dict["COUNTRY"]["COUNTRY_ID"].str.strip().str.upper()

        try:
            # Some Metadata data cleaning
            # Additional data cleaning to mitigate human error from special releases; remove white space
            dataset_dict["METADATA"]["INDICATOR_ID"] = dataset_dict["METADATA"]["INDICATOR_ID"].str.strip().str.upper()
            dataset_dict["METADATA"]["COUNTRY_ID"] = dataset_dict["METADATA"]["COUNTRY_ID"].str.strip().str.upper()
        except KeyError:
            pass

        try:
            # Additional data cleaning to mitigate human error from special releases; remove white space
            dataset_dict["DATA_REGIONAL"]["INDICATOR_ID"] = dataset_dict["DATA_REGIONAL"][
                "INDICATOR_ID"].str.strip().str.upper()
            dataset_dict["DATA_REGIONAL"]["COUNTRY_ID"] = dataset_dict["DATA_REGIONAL"][
                "COUNTRY_ID"].str.strip().str.upper()
        except KeyError:
            pass

        # Transorm metadata file to join multiple instance of Indic/Country/Year/Type
        # This will reshape the metadata file to be one row per Indic/Country/Year
        # Try is necessary since some archives do not contain a metadata file (e.g. CLTT)
        try:
            metaMod = dataset_dict["METADATA"]
            # Group by , if multiple intance exist...
            # ...forms a single row where multiple instances of the same metadata type are merged within the metadata columnn
            # ....reset_index -->  turn back pandas series to dataFrame

            # Additional data cleaning to mitigate human error from special releases; recast column type to string
            # empty cells are read to nan, nan is a float and join (next lines) doesn't concatenate float to string
            metaMod["METADATA"] = metaMod["METADATA"].astype(str)

            metaMod = metaMod.groupby(['INDICATOR_ID', 'COUNTRY_ID', 'YEAR', 'TYPE']) \
                ['METADATA'].agg(lambda col: '|'.join(col)).reset_index()

            dataset_dict['METADATA'] = metaMod  # Update dataFrame in dataset_dict
        except KeyError:
            pass

        # Some National data cleaning
        # Transform NaN to 'none'; try in case there is no Regional; keep VALUE col. as NAN to allow stat calculation
        dataset_dict["DATA_NATIONAL"] = dataset_dict["DATA_NATIONAL"].fillna('none')
        dataset_dict["DATA_NATIONAL"]["VALUE"] = dataset_dict["DATA_NATIONAL"]["VALUE"].replace('none', np.nan)

        try:
            # Some Regional data cleaning
            dataset_dict["DATA_REGIONAL"] = dataset_dict["DATA_REGIONAL"].fillna('none')
            dataset_dict["DATA_REGIONAL"]["VALUE"] = dataset_dict["DATA_REGIONAL"]["VALUE"].replace('none', np.nan)
        except KeyError:
            pass

        return dataset_dict

    def readmeFile(self):
        """Extracts the README file from the ZIP archive

        Parameter
        ----------
            none

        Returns
        -------
            String
                a Str with the README content
        """
        for name in self.zip_File_List:
            if str.lower("README") in str.lower(name):  # If file named README, process as String
                readme = self.read_URL_ZIP.read(name).decode('utf8')  # Read and decode specific list item as string
        return readme

    def subsetData(self, aDataSet, yearList, geoList, indicatorList, geoType="Country"):
        """Subsets the data

        Parameters
        ----------
            aDataSet : dataFrame
                a dataFrame to be subsetted
            yearList: a list of int
                a list of years to include in the subset
            geoList: a list of str
                a list of either 3-letter ISO country code or regions to include in the subset
            indicatorList: a list of str
                a list of indicator codes to include in the subset
            geoType: str {'Country','Region'} default is 'Country'
                a str to specify the geography type either Country or Regional data

        Returns
        -------
            DataFrame
                a DataFrame subsetted by a list of years, countries/regions and indicators
        """
        if geoType == "Country":
            aSubset = aDataSet[(aDataSet['INDICATOR_ID'].isin(indicatorList)) &
                               (aDataSet['COUNTRY_ID'].isin(geoList)) &
                               (aDataSet['YEAR'].isin(yearList))
                               ]
        elif geoType == "Region":
            aSubset = aDataSet[(aDataSet['INDICATOR_ID'].isin(indicatorList)) &
                               (aDataSet['REGION_ID'].isin(geoList)) &
                               (aDataSet['YEAR'].isin(yearList))
                               ]
        return aSubset

    def addMetadata(self, datasetNoMeta, metaDataSub, metadataType):
        """Merges the metadata to the data. This function only works on NATIONAL data.

        Parameters
        ----------
            datasetNoMeta: DataFrame
                a DataFrame receiving the metadata from another DataFrame
            metaDataSub: DataFrame
                a DataFrame giving metadata to another DataFrame
            metadataType: str e.g. {'Source:Data sources','Under Coverage:Students or individuals'}
                a string specifying the type of metadata merged to the dataset
                (the uniqueVal function can provide a list of all metadata type)

        Returns
        -------
            DataFrame
                a DataFrame with an extra column for a specific metadata type
        """
        # Subsetting the metadataset by metadata type
        metadataSubByType = metaDataSub[metaDataSub['TYPE'] == metadataType]
        # Joining metadata texts with the same YEAR/COUNTRY_ID/INDICATOR_ID/TYPE combination
        dataSubsetWithMeta = pd.merge(datasetNoMeta, metadataSubByType, how='left',
                                      on=['INDICATOR_ID', 'COUNTRY_ID', 'YEAR', ])
        # Drop metadata type and rename metadata column labels as metadata type
        dataSubsetWithMeta = dataSubsetWithMeta.drop(columns=['TYPE'])
        dataSubsetWithMeta = dataSubsetWithMeta.rename(columns={'METADATA': metadataType})
        # Replace none with nan for values
        dataSubsetWithMeta = dataSubsetWithMeta.fillna('none')
        dataSubsetWithMeta["VALUE"] = dataSubsetWithMeta["VALUE"].replace('none', np.nan)

        return dataSubsetWithMeta

    def addLabel(self, dataSetNoLabel, labelSet, labelType="Indic"):
        """Add a labels to a dataset
        Adds an additional column with the country or indicators name.

        Parameters
        ----------
            dataSetNoLabel: DataFrame
                the DataFrame containing the data
            labelSet: DataFrame
                the DataFrame containing the labels
            labelType: str {'Indic', 'Country'}
                a string specifying the type of label to merge

        Returns
        -------
            DataFrame
                a DataFrame with extra columns for labels
        """
        if labelType == "Indic":
            dataSetWithLabels = pd.merge(dataSetNoLabel, labelSet, how='left', on=["INDICATOR_ID"])
        elif labelType == "Country":
            dataSetWithLabels = pd.merge(dataSetNoLabel, labelSet, how='left', on=["COUNTRY_ID"])
        return dataSetWithLabels

    def uniqueVal(self, aDataSet, columnName):
        """Gets all unique values from a column

        Parameter
        ----------
            aDataSet: DataFrame
                a DataFrame containing the data
            columnName: String
                a String for the column name on which to gather unique values

        Returns
        -------
            List
                a list of unique values
        """
        # uniqueVal = aDataSet[columnName].drop_duplicates().sort_values().dropna().to_list()

        uniqueVal = aDataSet[columnName].drop_duplicates().sort_values().dropna().to_list()
        return uniqueVal

    # Hardcoded to search in the "LABEL" file, "INDICATOR_ID" column
    def searchList(self, dataTableDict, searchTermList, indic_or_region="Indic"):
        """Returns a list of INDICATOR_ID or REGION_ID containing the search
        string

        Parameter
        ----------
            dataTableDict: Dictionary
                a dictionary containing all the dataFrame of a specific BDDS archive (created from the dataTables method)
            searchTermList: List
                list of search terms
            indic_or_region: Str {'Indic', 'Region'} default is 'Indic'
                string specifying the type of data to search for; either Indicators or Regions

        Returns
        -------
            List
                a list containing all the search results (no duplicates)
        """

        def searchIt():
            for terms in searchTermList:  # Loop through all search Terms in searchTermList
                for indicOrRegion in fullListOfItems:  # Loop the search Term within the list of unique INDICATOR_ID or REGION_ID
                    match = re.search(terms, indicOrRegion,
                                      flags=re.IGNORECASE)  # Try to match the search Term within a INDICATOR_ID or REGION_ID
                    if match:
                        if indicOrRegion not in matchList:  # If indicators is not already in the list append to matchList
                            matchList.append(indicOrRegion)

        matchList = []
        if indic_or_region == "Indic":
            fullListOfItems = list(pd.unique(dataTableDict["DATA_NATIONAL"]["INDICATOR_ID"]))
            searchIt()
        elif indic_or_region == "Region":
            fullListOfItems = list(pd.unique(dataTableDict["DATA_REGIONAL"]["REGION_ID"]))
            searchIt()
        return matchList

    # !!!New search need test
    def searchList_II(self, searchTermsList, searchTable, searchColumn):
        """
        Search a String type column within a dataFrame and returns a list of results
        e.g. search "BUL" in the "INDICATOR_ID" column and returns a list of all indicators
        containing the string "BUL" such as "PER.BULLIED.1". This is useful for generating
        the list required to subset data.

        Parameters
        ----------
        searchTermsList : List of Strings
            A list of search values
        searchTable : Dataframe
            dataFrame within which to search
        searchColumn : String
            the name of the column within which to search

        Returns
        -------
        matchList : List
            List of of all unique values matching the search queries.

        """

        unique_values = pd.unique(searchTable[searchColumn])
        # unique_values = [i.lower() for i in list(unique_values)]
        # searchTermsList = [i.lower() for i in searchTermsList]

        # Search all query in unique values
        # !!! Creates an exception when hitting a nan (rare)
        matchList = []
        for query in searchTermsList:
            for term in unique_values:
                match = re.search(query, term, flags=re.IGNORECASE)
                if match:
                    if term not in matchList:
                        matchList.append(term)
        return matchList

    def allLabelMerge(self, dataTableDict, aDataSet, geoType="Country"):
        """Merges all labels (country and indicator labels) to a dataset

        Parameter
        ----------
            dataTableDict: Dictionary
                a dictionary containing all the dataFrame of a specific BDDS archive (created from the dataTables method)
            aDataSet: DataFrame
                a DataFrame on which to merge labels
            geoType: str, {'Country','Region'} default is 'Country'
                a string specifying the type of data in the dataset

        Returns
        -------
            DataFrame
                a DataFrame containing extra columns with the country/indicator labels
        """
        if geoType == "Country":
            aSetWithAllLabels = self.addLabel(aDataSet, dataTableDict["COUNTRY"], labelType="Country")
            aSetWithAllLabels = self.addLabel(aSetWithAllLabels, dataTableDict["LABEL"], labelType="Indic")
        elif geoType == "Region":
            aSetWithAllLabels = self.addLabel(aDataSet, dataTableDict["LABEL"], labelType="Indic")
        return aSetWithAllLabels

    # Using the dataTableDict helps enforce the method on the metadata file (otherwise the user could apply it on a data sheet without "TYPE" var)
    def subsetMetaDict(self, dataTableDict, yearList, geoList, indicatorList):
        """Creates a subset of the metadata file where each indicator/year/country data cube contains a dictionary of its metadata

        Parameter
        ----------
            dataTableDict: Dictionary
                a dictionary containing all the dataFrame of a specific BDDS archive (created from the dataTables method)
            yearList: List
                a list containing the years to include in the subset
            geoList: List
                a list of either 3-letter ISO country code or regions to include in the subset
            indicatorList: List
                a list containing the indicators to include in the subset

        Returns
        -------
            DataFrame
                a DataFrame containing the metadata of each indicator/country/year within a dict
        """
        # !!! Fixing bug when there is no metadata for current subset
        metaSubset = self.subsetData(dataTableDict["METADATA"], yearList, geoList, indicatorList, geoType="Country")
        if metaSubset.empty:
            return None

        # create a dict with key=indic/coutry/year value=dictionary of meta key=type:value=metadata point. (fastest of all method tried)
        dictMeta = metaSubset.pivot(index=["INDICATOR_ID", "COUNTRY_ID", "YEAR"],
                                    columns="TYPE",
                                    values="METADATA").to_dict('index')

        # Remove nan value from dict values; works with any level of nested dict (pivot creates a key:nan pair when type is missing)
        def cleanNullTerms(d):
            clean = {}
            for k, v in d.items():
                if isinstance(v, dict):  # Check if dict value (v) is a dict (nested dict)
                    nested = cleanNullTerms(
                        v)  # If value is a dict call back this function on that nested dict (will produce a clean dict without value=nan)
                    if len(nested.keys()) > 0:  # If the cleaned dict is not empty
                        clean[k] = nested  # The value of the parent dict is the cleaned nested dict
                # If value of a key is a string, add k-v pair to clean dict (will skip k:v=nan since they are float, effectively removing them)
                elif isinstance(v, str):
                    clean[k] = v
            return clean

        # Run that removes nan function on the dict
        dictMeta_noNull = cleanNullTerms(dictMeta)
        
        # Dict to list of list ... to dataframe
        listMeta_noNull = []
        for k, v in dictMeta_noNull.items(): 
            a, b, c = k                         #k is a tuple of ('INDICATOR_ID', 'COUNTRY_ID', 'YEAR')
            temp_list = [a, b, c, v]            #v is the full metadata string
            listMeta_noNull.append(temp_list)
        dfMetaFinal = pd.DataFrame(listMeta_noNull, columns = ['INDICATOR_ID', 'COUNTRY_ID', 'YEAR', 'metaDict'])
        return dfMetaFinal

    def allMetaMerge(self, dataTableDict, aDataSet, metaForm="Col"):
        """Merges all metadata to a dataset. This function works on NATIONAL data only.

        Parameter
        ----------
            dataTableDict: Dictionary
                a dictionary containing all the dataFrame of a specific BDDS archive (created from the dataTables method)
            aDataSet: DataFrame
                a DataFrame on which to merge labels
            metaForm: Str {'Col', 'Dict'} default is 'Col'
                a string to select how to return the metadata
                'Col' will return the metadata as columns and 'Dict' as a dictionary

        Returns
        -------
            DataFrame
                a DataFrame containing all the metadata as multiple columns or a dict
        """
        # Get list of unique values for indicator, country, year of aDataset
        yearList = self.uniqueVal(aDataSet, "YEAR")
        geoList = self.uniqueVal(aDataSet, "COUNTRY_ID")
        indicatorList = self.uniqueVal(aDataSet, "INDICATOR_ID")
        if metaForm == "Dict":
            # Uses subsetMetaDict method to provide a subset of the metadata with metadata as dict
            metaDictSub = self.subsetMetaDict(dataTableDict, yearList, geoList, indicatorList)
            # Fix issue when subsetMetaDict returns None (no metadata for the selected subset)
            if metaDictSub is None:
                dsWithMeta = aDataSet.copy()
                dsWithMeta["metaDict"] = np.nan
            else:
                # Merge data to metadata subset
                dsWithMeta = pd.merge(aDataSet, metaDictSub, how='left',
                                      on=['YEAR', 'COUNTRY_ID', 'INDICATOR_ID'])
                # # !!! Transform NaN to 'none' on Qual and Mag only (keep NaN in VALUE and metaDict coluns)
                dsWithMeta[["MAGNITUDE", "QUALIFIER"]] = dsWithMeta[["MAGNITUDE", "QUALIFIER"]].fillna('none')

        else:
            # Get all types of metadata
            allMetaType = self.uniqueVal(dataTableDict["METADATA"], "TYPE")
            # Keep var: loop will updates this df with new metadata after each iteration
            dsWithMeta = aDataSet
            # Loop over list of metadata type and
            for item in allMetaType:
                dsWithMeta = self.addMetadata(dsWithMeta, dataTableDict["METADATA"], item)
        return dsWithMeta

    def allLabelMetaMerge(self, dataTableDict, yearList, geoList, indicatorList, geoType="Country", metaForm='Col'):
        """Subset and merge all labels and metadata in a single process

        Parameter
        ----------
            dataTableDict: Dict
                a dictionary containing all the dataFrame of a specific BDDS archive (created from the dataTables method)
            yearList: List
                a list containing the years to include in the subset
            geoList: List
                a list of either 3-letter ISO country code or regions to include in the subset
            indicatorList: List
                a list containing the indicators to include in the subset
            geoType: Str {'Country', 'Region'}
                a string specifying the type of data in the dataset
            metaForm: str {'Col', 'Dict'} default is 'Col'
                a string to select how to return the metadata
                'Col' will return the metadata as columns and 'Dict' as a dictionary

        Returns
        -------
            DataFrame
                a DataFrame, a subset with all metadata and labels merged
        """
        if geoType == "Country":
            subset = self.subsetData(dataTableDict["DATA_NATIONAL"], yearList, geoList, indicatorList,
                                     geoType="Country")
            subset = self.allLabelMerge(dataTableDict, subset)
            subset = self.allMetaMerge(dataTableDict, subset, metaForm)
            #!!! Uncomment if streamlit app doesn't like nan with dict column
            # subset["metaDict"] = subset["metaDict"].fillna("none")

        elif geoType == "Region":
            subset = self.subsetData(dataTableDict["DATA_REGIONAL"], yearList, geoList, indicatorList, geoType="Region")
            subset = self.allLabelMerge(dataTableDict, subset, geoType="Region")
            # subset = self.allMetaMerge(dataTableDict, subset)   #No metadata for REGIONAL provided to date
        return subset

    def longToWide(self, dataTableDict, aDataSet, dataType="Data", wideOn="Year"):
        """ Reshape a data or metadata set from long to wide format
            Notes:  --> pivoting keeps only YEARS/INDICATOR_ID/COUNTRY_ID var.so add labels after pivoting
                    --> you cannot merge metadata to a wide format

        Parameters
        ----------
        dataTableDict: Dictionary
            a dictionary containing all the dataFrame of a specific BDDS archive (created from the dataTables method)
        aDataSet : DataFrame
            A dataset or a subset.
        dataType : Str, optional
            Specify the data type either data or metadata {"Data", "Meta"}. The default is "Data".
        wideOn : Str, optional
            Specify type of variable to be expanded into wide format {"Year", "Indic", "MetaType"}. The default is "Year".
            "Metatype" only works with metadata

        Returns
        -------
        A DataFrames in long format

        """
        if dataType == "Data":
            if wideOn == "Year":
                # Pivot data to expose all years on indicator / country combo
                dfWide = aDataSet.pivot(
                    index=['COUNTRY_ID', 'INDICATOR_ID'],
                    columns='YEAR',
                    values='VALUE').reset_index()

            elif wideOn == "Indic":
                # Pivot data to expose all indicators on year / country combo
                dfWide = aDataSet.pivot(
                    index=['YEAR', 'COUNTRY_ID'],
                    columns='INDICATOR_ID',
                    values='VALUE').reset_index()
            # dfWide.fillna('', inplace=True)
        elif dataType == "Meta":
            if wideOn == "MetaType":
                # Pivot metadata to expose all indicators types on year / country / indicator combo
                dfWide = aDataSet.pivot(
                    index=['YEAR', 'COUNTRY_ID', 'INDICATOR_ID'],
                    columns='TYPE',
                    values='METADATA').reset_index()

            else:
                # Get lists of indicator included in the subset
                yearList = self.uniqueVal(aDataSet, "YEAR")
                geoList = self.uniqueVal(aDataSet, "COUNTRY_ID")
                indicatorList = self.uniqueVal(aDataSet, "INDICATOR_ID")
                # Get metasubset with metadata as dict
                metaSub = self.subsetMetaDict(dataTableDict, yearList, geoList, indicatorList)

                if wideOn == "Year":
                    # Pivot metadata as dict to expose all years on country / indicator combo
                    dfWide = metaSub.pivot(
                        index=['COUNTRY_ID', 'INDICATOR_ID'],
                        columns='YEAR',
                        values='metaDict').reset_index()

                elif wideOn == "Indic":
                    # Pivot metadata as dict to expose indicators on country / year combo
                    dfWide = metaSub.pivot(
                        index=['COUNTRY_ID', 'YEAR'],
                        columns='INDICATOR_ID',
                        values='metaDict').reset_index()
            dfWide.fillna('none', inplace=True)
        return dfWide
