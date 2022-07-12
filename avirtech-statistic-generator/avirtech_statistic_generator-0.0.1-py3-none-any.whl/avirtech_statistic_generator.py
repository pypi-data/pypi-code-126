from msilib.schema import Error
import arcpy
import tkinter as tk
from tkinter import messagebox
import tkFileDialog as filedialog
import os
from simpledbf import Dbf5

class avirtech_statistic_generator:
    @staticmethod
    def all_proces():
        mxd = arcpy.mapping.MapDocument("Current")
        arcpy.env.workspace = "CURRENT"
        df = arcpy.mapping.ListDataFrames(mxd)[0]

        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("","Input Crown Actual")
        folder_actual = filedialog.askdirectory()
        messagebox.showinfo("","Input Crown Model")
        folder_model = filedialog.askdirectory()
        messagebox.showinfo("", "Input folder to store result of statistics")
        jpg_statistic_loc = filedialog.askdirectory()
        root.destroy

        substring = ".shp"
        substring_2 = ".xml"
        substring_3 = "DESKTOP"

        data_actual = []
        for file in os.listdir(folder_actual):
            if file.find(substring) != -1 and file.find(substring_2) == -1 and file.find(substring_3) == -1:
                base_actual = os.path.splitext(file)[0]
                location_actual = os.path.join(folder_actual,file)
                new_layer = arcpy.mapping.Layer(location_actual)
                arcpy.mapping.AddLayer(df,new_layer,"BOTTOM")
                data_actual.append(base_actual)

        data_model = []
        for file in os.listdir(folder_model):
            if file.find(substring) != -1 and file.find(substring_2) == -1 and file.find(substring_3) == -1:
                base_model = os.path.splitext(file)[0]
                location_model = os.path.join(folder_model,file)
                new_layer = arcpy.mapping.Layer(location_model)
                arcpy.mapping.AddLayer(df,new_layer,"BOTTOM")
                data_model.append(base_model)

        # Process: Feature To Point
        arcpy.FeatureToPoint_management(str(data_actual[0]), os.path.join(jpg_statistic_loc, "point_291data_shp"), "CENTROID")

        # Process: Add Field
        arcpy.AddField_management(str(data_model[0]), "jarimodel", "DOUBLE", "3", "3", "", "", "NULLABLE", "NON_REQUIRED", "")

        # PROSES CalculateField Field Jarijari (SHP_dataMODEL)
        arcpy.CalculateField_management(str(data_model[0]), "jarimodel", "Sqr ([Shape_Area] /(3.14))", "VB", "")

        # Process: Spatial Join
        arcpy.SpatialJoin_analysis(str(data_model[0]),"point_291data_shp", os.path.join(jpg_statistic_loc,"spatialjoin_datamodel.shp"))

        # Process: Table to dBASE (multiple)
        arcpy.TableToDBASE_conversion("spatialjoin_datamodel", jpg_statistic_loc)

        #PROSES STATISTI
        from simpledbf import Dbf5
        import pandas as pd
        import matplotlib.pyplot as plt
        import os

        def ket(x):
            if x < (-1):
                return 'Under Estimate'
            elif x > (1):
                return 'Over Estimate'
            else:
                return "Pass"

        loc_dbf = os.path.join(jpg_statistic_loc,"spatialjoin_datamodel_1.dbf")
        df_ilham = Dbf5(loc_dbf).to_dataframe()

        modelaktual = (df_ilham[["Id_1", "JariJari", "jarimodel"]])
        # SCATTERPLOT

        modelaktual = (df_ilham[["Id_1", "JariJari", "jarimodel"]])
        # Perubahan nama kolom tabelnya
        modelaktual.columns = ['id', 'JariJari_Aktual', 'JariJari_Model']
        # print(modelaktual)

        all = modelaktual.assign(mae=lambda x: x.JariJari_Model - x.JariJari_Aktual).abs()
        all2 = all.assign(mape=lambda x: (((x.JariJari_Model - x.JariJari_Aktual).abs())/x.JariJari_Model)*100)
        all3 = all2.assign(selisih=lambda x: x.JariJari_Model - x.JariJari_Aktual)

        nilaimae = round(all2["mae"].mean(),4)
        nilaimape = round(all2["mape"].mean(),4)

        text = "Nilai MAE & Mape :"
        max_id = all2["id"].max()

        all3['ket'] = all3['selisih'].apply(ket)
        summary_of_ket = all3['ket'].value_counts()
        keterangan = list(all3["ket"])
        frequency = {}
        for kategori in keterangan:
            frequency[kategori] = keterangan.count(kategori)

        nilaimae_2 = str(round(all2["mae"].mean(),4))
        nilai_mape_2 = round(all2["mape"].mean(),4)

        # SCATTERPLOT
        plt.plot(modelaktual["id"], modelaktual["JariJari_Aktual"], 'ro', color='blue', marker="s")
        plt.plot(modelaktual["id"], modelaktual["JariJari_Model"], 'ro', color='red')
        plt.axis([0, (max_id + 10), 1, 7])
        plt.gcf().set_size_inches((18,10))
        plt.title("Scatter Plot Jari-jari Aktual & Jari-jari Model", fontsize=20)
        plt.legend(loc="lower right")
        plt.xlabel('id', fontsize=15)
        plt.text(1.1,1.5, (text))
        plt.text(1.1,1.3, (nilaimae_2))
        plt.text(1.1,1.1, (nilai_mape_2))
        plt.text(40,1.1 , (summary_of_ket))
        plt.ylabel('Jari-Jari', fontsize=15)
        plt.savefig(os.path.join(jpg_statistic_loc, "ScatterPLOT.jpg"),format="png")

# avirtech_statistic_generator.all_proces()