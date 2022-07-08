from wencaipy.common.wcParameter import SQLITE_PATH_RR_PC 


def data_to_excel(data=None,file_name=None):
        try:
            data.to_excel(f"{SQLITE_PATH_RR_PC }/{file_name}.xlsx")
            
            print(f"Save data to excel <{file_name}.xlsx> finish !")
        except Exception as e:
            print(e)
    