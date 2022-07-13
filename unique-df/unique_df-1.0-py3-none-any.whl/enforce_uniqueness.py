
import pandas as pd

def unique(csv_path_old, csv_path_new, unique_df_save_location):
    csv_path_old = '/Users/pierre.liebenberg/Desktop/Apollo tests/tpid_test5.csv'
    csv_path_new = '/Users/pierre.liebenberg/Desktop/Apollo tests/tpid_test5_copy.csv'

    df_old = pd.read_csv(csv_path_old)
    df_new = pd.read_csv(csv_path_new)

    cols = df_old.columns.values.tolist()

    # compare current tpid_db with csv attempting to upload and drop duplicates
    df_new = df_new[cols]
    df_current = df_old[cols]

    df_concat = pd.concat([df_new, df_current])
    df_concat = df_concat.loc[df_concat.astype(str).drop_duplicates(keep=False).index]

    df_concat.to_csv(unique_df_save_location)

# unique('/Users/pierre.liebenberg/Desktop/Apollo tests/tpid_test5.csv','/Users/pierre.liebenberg/Desktop/Apollo tests/tpid_test5_copy.csv','/Users/pierre.liebenberg/Desktop/Apollo tests/tpid_test5_copy_unique.csv')
