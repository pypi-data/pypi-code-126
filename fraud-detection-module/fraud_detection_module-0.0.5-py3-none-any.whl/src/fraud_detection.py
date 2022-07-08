import itertools
import numpy as np
import pandas as pd


class FraudDetectionClass:
    def transform(self, data):
        df_selected = data[
            [
                "CALL_DATETIME",
                "CALL_CALLING_PARTY",
                "CALL_CALLED_PARTY",
                "CALLTYPE",
                "NETWORK_ID",
                "LOC_ID",
                "CELL_ID",
            ]
        ]
        # Cleaining and sorting by time.

        df_selected_call = df_selected[df_selected["CALLTYPE"] == "VOICE"]
        df_selected_call.CALL_DATETIME = df_selected_call.CALL_DATETIME.apply(
            pd.to_datetime
        )
        df_selected_call.sort_values(by="CALL_DATETIME", inplace=True)
        df_selected_call.reset_index(inplace=True, drop=True)

        repeated_list = (
            df_selected_call.groupby(by="CALL_CALLING_PARTY")
            .apply(lambda x: tuple(x.index))
            .tolist()
        )

        fraud_list = []
        for i in repeated_list:
            if len(i) > 1:
                for j in list(itertools.combinations(i, 2)):
                    diff_sec = np.abs(
                        df_selected_call.iloc[j[0], 0] - df_selected_call.iloc[j[1], 0]
                    ).total_seconds()
                    cell_id_bool = (
                        df_selected_call.iloc[j[0], -1]
                        != df_selected_call.iloc[j[1], -1]
                    )
                    if diff_sec < 10 and cell_id_bool:
                        fraud_list.append(j)
        fraud_list = pd.DataFrame([fraud_list])
        return fraud_list
