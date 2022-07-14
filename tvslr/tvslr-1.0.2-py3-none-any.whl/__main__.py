# __main__.py

import sys
import pandas as pd
from tvslr import TVSLR

def main():
    if len(sys.argv) > 3:
        filename = sys.argv[1]
        sheetname = sys.argv[2]
        subsetSize = sys.argv[3]
        
        df = pd.read_excel(filename, sheet_name=sheetname)

        X = df[df.columns[:-1]].to_numpy()
        y = df[df.columns[-1]].to_numpy()

        reg = TVSLR(X, y, subsetSize)
        betas = reg.run()
        print(betas)
        print("R-squared:", reg.cod)
        print("Adj. R-squared:", reg.adj_cod)
    else:
        exit()

if __name__ == "__main__":
    main()
    