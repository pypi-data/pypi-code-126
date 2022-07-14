import pandas, logging, datetime

class VBO():
    def __init__(self) -> None:
        self.header=[]
        self.colnames=[]
        self.units=[]
        self.comments=[]
        self.modules=[]
        self.data=[]
        self.df=pandas.DataFrame()
        self.start=None

    def read(self,filename):
        lines=[]
        with open(file, encoding="utf-8") as f:
            line=f.readline()
            while line!='':
                lines.append(line)
            f.close()

        self.start=lines.pop(0).split(' ')[3].replace('/','-')
        self.__sort(lines)
        self.__column_names()
        self.__data()

    def __columns_name(self):
        logging.info('Converting Column names')
        self.colnames=self.colnames[0].replace('\n','')
        cols=self.colnames.split(' ')
        self.colnames=[col for col in cols]

    def __data(self):
        logging.info('Converting data')
        rows=[]
        timecol=self.colnames.index('time')
        for line in self.data:
            line=line.split(' ')
            line=[item for item in line]
            line[timecol]=datetime.datetime.fromisoformat("%s %s:%s:%s.%s" %(
                self.date,
                line[timecol][0:2],
                line[timecol][2:4],
                line[timecol][4:6],
                line[timecol].split('.')[1]))
            rows.append(line)
        self.df=pandas.concat([self.data,pandas.DataFrame(rows,columns=self.colnames)])

        # changing the time to datetime
        self.df['time']=pandas.to_datetime(self.df['time'])
        self.df.set_index('time',drop=True,inplace=True)

    def __sorting(self,lines);
        try:
            current=[]
            while True:
                line=lines.pop(0)
                if line=='':
                    continue
                if line=='\n':
                    continue           
                match line:
                    case '[column names]\n':
                        logging.info('Processing column names')
                        current=self.colnames
                    case '[data]\n':
                        print('Processing data section')
                        current=self.data
                    case _:
                        current.append(line)
        except Exception as e:
            print(str(e))