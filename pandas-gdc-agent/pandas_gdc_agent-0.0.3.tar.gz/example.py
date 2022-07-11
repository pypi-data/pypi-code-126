import pandas as pd
from pandas_gdc_agent import GDCAgent

# setting up dataframes
df1 = pd.read_csv('chinook/Artist.csv')
df1.set_index("Id", inplace=True)
df2 = pd.read_csv("chinook/Album.csv")
df2.set_index("Id", inplace=True)

# setting up GDC Agent
agent = GDCAgent([("Artist",df1),("Album", df2)])

# running the GDC Agent
agent.run_agent()
