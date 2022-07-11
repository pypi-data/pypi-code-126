from numpy import outer
import arcpy
import os
import Tkinter as tk
from tkinter import messagebox
import tkFileDialog as filedialog
from tkFileDialog import askopenfilename
from simpledbf import Dbf5
import pandas as pd
from os.path import exists
import random, shutil,configparser

class initiation_process:
    @staticmethod
    def initiate_process():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("","Please input your crown plot")
        global folder_plot
        folder_plot = filedialog.askdirectory()
        messagebox.showinfo("","Please input your area location")
        global area_location
        area_location = filedialog.askdirectory()
        messagebox.showinfo("","Please input folder to store result")
        global gdb_location
        gdb_location = filedialog.askdirectory()
        root.destroy

class starting_first:
    @staticmethod
    def starting_process():
        global mxd
        mxd = arcpy.mapping.MapDocument("Current")
        mxd.author = "Dwieka"
        arcpy.env.workspace = "CURRENT"
        global df
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        global plotting_data
        plotting_data = []
        global plotting_data_tif
        plotting_data_tif = []
        global plotting_area
        plotting_area = []

        substring_plot = ".shp"
        substring_plot_2 = ".xml"
        substring_plot_3 = "DESKTOP"

        for file in os.listdir(folder_plot):
            if file.find(substring_plot) != -1 and file.find(substring_plot_2) == -1 and file.find(substring_plot_3) == -1:
                base = os.path.splitext(file)[0]

                location_plot = os.path.join(folder_plot,file)
                new_layer = arcpy.mapping.Layer(location_plot)
                arcpy.mapping.AddLayer(df,new_layer,"BOTTOM")

                plotting_data.append(base)
            elif file.endswith('.tif') or file.endswith('.ecw'):
                data_process = os.path.join(folder_plot,file)
                data_show = file
                arcpy.MakeRasterLayer_management(data_process,data_show,"","")
                plotting_data_tif.append(file)

        for area in os.listdir(area_location):
            if area.find(substring_plot) != -1 and area.find(substring_plot_2) == -1 and area.find(substring_plot_3) == -1:
                base = os.path.splitext(area)[0]
                area_plot = os.path.join(area_location,area)
                new_layer = arcpy.mapping.Layer(area_plot)
                arcpy.mapping.AddLayer(df,new_layer,"BOTTOM")
                plotting_area.append(base)

class create_folder:
    def __init__(self,main_location):
        self.main_location = main_location
    
    def create_folder(self):
        folder_making = ["clip_ileaf","kmeans_raw","iso_result","leaf","dbf","outer_ring","palm_buffer_result","point_process"]

        for folder in folder_making:
            location = os.path.join(self.main_location,folder)
            os.mkdir(location)

            global location_masking
            location_masking = os.path.join(self.main_location,folder_making[0])
            global cluster_raw
            cluster_raw = os.path.join(self.main_location,folder_making[1])
            global iso_location
            iso_location = os.path.join(self.main_location,folder_making[2])
            global leaf_location
            leaf_location = os.path.join(self.main_location,folder_making[3])
            global dbf_location
            dbf_location = os.path.join(self.main_location,folder_making[4])
            global buffer_last_location
            buffer_last_location = os.path.join(self.main_location,folder_making[5])
            global palm_buffer_point_location
            palm_buffer_point_location = os.path.join(self.main_location,folder_making[6])
            global point_process
            point_process = os.path.join(self.main_location,folder_making[7])

class process_first:
    def __init__(self,loc_gdb,name):
        self.loc_gdb = loc_gdb
        self.name = name
        select_data = arcpy.SelectLayerByAttribute_management(plotting_area[0], "NEW_SELECTION", "\"ket\" = '{}'".format(str(areatype)))

        arcpy.SelectLayerByLocation_management(plotting_data[0], "INTERSECT", plotting_area[0], "", "NEW_SELECTION", "NOT_INVERT")

        arcpy.CopyFeatures_management(plotting_data[0],os.path.join(point_process,"{}_point".format(areatype)),"0","0","0")

        arcpy.gp.ExtractByMask_sa(plotting_data_tif[0],plotting_area[0],os.path.join(self.loc_gdb,self.name))

        arcpy.RasterToOtherFormat_conversion(os.path.join(self.loc_gdb,self.name),location_masking,"TIFF")

        arcpy.MakeRasterLayer_management(os.path.join(location_masking,"{}.tif".format(self.name)),"{}_exp".format(self.name),"","")

class processing_raster_medium_grass:
    def __init__(self,data,main_location):
        self.data = data
        self.main_location = main_location

        arcpy.CopyRaster_management(self.data, os.path.join(main_location,"ras_f"), "", "", "255", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "", "NONE")

        b1 = "f_b1"
        b2 = "f_b2"
        b3 = "f_b3"

        location_raster_calc = os.path.join(self.main_location,"vari_f")

        location_raster_calc_2 = os.path.join(self.main_location,"egi_f")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b1,"","","1")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b2,"","","2")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b3,"","","3")

        arcpy.gp.RasterCalculator_sa("(\"{}\" - \"{}\") / (\"{}\" + \"{}\" - \"{}\")".format(b2,b1,b2,b1,b3),location_raster_calc)

        arcpy.gp.RasterCalculator_sa("2 * (\"{}\"-\"{}\"-\"{}\")".format(b2,b1,b3),location_raster_calc_2)

        arcpy.CompositeBands_management("f_b1;f_b2;f_b3;vari_f1.tif", os.path.join(self.main_location,"composite"))

        arcpy.gp.IsoClusterUnsupervisedClassification_sa("composite","4",os.path.join(iso_location,"iso_weed"),"20","10","")

        arcpy.RasterToPolygon_conversion("iso_weed",os.path.join(iso_location,"rtpisoweed"))

        selection = arcpy.SelectLayerByAttribute_management("rtpisoweed", "NEW_SELECTION", "gridcode = 1")

        arcpy.CopyFeatures_management(selection,os.path.join(self.main_location,"ileaf.shp"))

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != plotting_data[0] and str(layer) != self.data and str(layer) != "ileaf" and str(layer) != plotting_area[0] and str(layer) != "crown_ring_fwd" and str(layer) != "crown_ring_nwd" and str(layer) != "nwd_point" and str(layer) != "wd_point" and str(layer) != "fwd_point":
                arcpy.mapping.RemoveLayer(df,layer)

class processing_raster_non_grassy:
    def __init__(self, data, main_location):
        self.data = data
        self.main_location = main_location
        arcpy.CopyRaster_management(self.data, os.path.join(self.main_location,"ras_f"), "", "", "255", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "", "NONE")

        b1 = "f_b1"
        b2 = "f_b2"
        location_raster_calc = os.path.join(self.main_location,"rasc_f")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b1,"","","1")

        arcpy.MakeRasterLayer_management(os.path.join(self.main_location,"ras_f"),b2,"","","2")

        arcpy.gp.RasterCalculator_sa("(\"{}\") / (\"{}\")".format(b2,b1),location_raster_calc)

        arcpy.gp.IsoClusterUnsupervisedClassification_sa("rasc_f","3",os.path.join(iso_location,"iso_f"),"20","10","")

        arcpy.RasterToPolygon_conversion("iso_f",os.path.join(iso_location,"rtpiso_f"))

        selection = arcpy.SelectLayerByAttribute_management("rtpiso_f", "NEW_SELECTION", "gridcode = 2")

        arcpy.CopyFeatures_management(selection,os.path.join(self.main_location,"ileaf.shp"))

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != plotting_data[0] and str(layer) != self.data and str(layer) != "ileaf" and str(layer) != plotting_area[0] and str(layer) != "crown_ring_fwd" and str(layer) != "crown_ring_wd" and str(layer) != "nwd_point" and str(layer) != "wd_point" and str(layer) != "fwd_point":
                arcpy.mapping.RemoveLayer(df,layer)

class processing_raster_full_grassy:
    def __init__(self,main_location,loc_gdb):
        self.main_location = main_location
        self.loc_gdb = loc_gdb
        arcpy.CopyRaster_management("fwd_exp", os.path.join(self.loc_gdb,"ras_f"), "", "", "255", "NONE", "NONE", "32_BIT_FLOAT", "NONE", "NONE", "", "NONE")

        b1 = "f_b1"
        b2 = "f_b2"
        b3 = "f_b3"

        arcpy.MakeRasterLayer_management(os.path.join(self.loc_gdb,"ras_f"),b1,"","","1")

        arcpy.MakeRasterLayer_management(os.path.join(self.loc_gdb,"ras_f"),b2,"","","2")

        arcpy.MakeRasterLayer_management(os.path.join(self.loc_gdb,"ras_f"),b3,"","","3")

        arcpy.gp.RasterCalculator_sa("\"{}\" / ((1.4 * (\"{}\" - \"{}\")) * \"{}\")".format(b2,b1,b2,b2), os.path.join(self.main_location,"ind"))

        arcpy.gp.IsoClusterUnsupervisedClassification_sa("ind","5",os.path.join(iso_location,"iso_flwd"),"20","10","")

        arcpy.RasterToPolygon_conversion("iso_flwd",os.path.join(iso_location,"rtpisoweed"))

        selection = arcpy.SelectLayerByAttribute_management("rtpisoweed", "NEW_SELECTION", "gridcode = 4")

        arcpy.CopyFeatures_management(selection,os.path.join(self.main_location,"ileaf.shp"))

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != plotting_data[0] and str(layer) != "fwd_exp" and str(layer) != "ileaf" and str(layer) != plotting_area[0] and str(layer) != "crown_ring_wd" and str(layer) != "crown_ring_nwd" and str(layer) != "nwd_point" and str(layer) != "wd_point" and str(layer) != "fwd_point":
                arcpy.mapping.RemoveLayer(df,layer)

        #processing_shape_full_grass

        arcpy.Near_analysis(plotting_data[0],plotting_data[0],"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")
        try:
            arcpy.AddField_management(plotting_data[0],"ket","TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(plotting_data[0], "buffer", "DOUBLE", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(plotting_data[0], "fidcopy", "SHORT", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")
        except Exception:
            pass

        arcpy.CalculateField_management(plotting_data[0], "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

        mylist_ket = (([str(row.getValue("ket")) for row in arcpy.SearchCursor(plotting_data[0], fields="ket")]))

        i = [i for i in mylist_ket if i == "Very Close"]

        if int(len(i)) <= 0.5:
            arcpy.CalculateField_management(plotting_data[0], "buffer", "[NEAR_DIST] / 1.5", "VB", "")

            arcpy.CalculateField_management(plotting_data[0], "fidcopy", "[FID]", "VB", "")
        elif int(len(i)) > 0.5:
            arcpy.CalculateField_management(plotting_data[0], "buffer", "[NEAR_DIST] / 1.2", "VB", "")

            arcpy.CalculateField_management(plotting_data[0], "fidcopy", "[FID]", "VB", "")

        mylist_dist = list(([float(row.getValue("NEAR_DIST")) for row in arcpy.SearchCursor(plotting_data[0], fields="NEAR_DIST")]))

        mylist_fid = list(([int(row.getValue("fidcopy")) for row in arcpy.SearchCursor(plotting_data[0], fields="fidcopy")]))

        ziped = dict(zip(mylist_dist,list(mylist_fid)))

        fids_to_delete = []
        for key, value in ziped.items():
            if float(key) <= 1.0:
                fids_to_delete.append(value)

        if len(fids_to_delete) > 0:
            for fid_to_delete in fids_to_delete:
                arcpy.SelectLayerByAttribute_management(plotting_data[0],"NEW_SELECTION","\"fidcopy\" = {}".format(fid_to_delete))

                arcpy.DeleteFeatures_management(plotting_data[0])

            arcpy.Near_analysis(plotting_data[0],plotting_data[0],"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")

            arcpy.CalculateField_management(plotting_data[0], "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

            arcpy.CalculateField_management(plotting_data[0], "buffer", "[NEAR_DIST] / 1.8", "VB", "")

            arcpy.CalculateField_management(plotting_data[0], "fidcopy", "[FID]", "VB", "")

        mylist_dist = list(([float(row.getValue("NEAR_DIST")) for row in arcpy.SearchCursor(plotting_data[0], fields="NEAR_DIST")]))

        for dist in mylist_dist:
            if float(dist) < 5.0:
                arcpy.SelectLayerByAttribute_management(plotting_data[0],"NEW_SELECTION","\"NEAR_DIST\" = {}".format(dist))

                arcpy.CalculateField_management(plotting_data[0], "buffer", "[NEAR_DIST] / 0.8", "VB", "")

        for fid in mylist_fid:
            selection = arcpy.SelectLayerByAttribute_management(plotting_data[0],"NEW_SELECTION","\"fidcopy\"={}".format(fid))

            arcpy.CopyFeatures_management(selection,os.path.join(palm_buffer_point_location,"palm_{}.shp".format(fid)))

        arcpy.SelectLayerByAttribute_management(plotting_data[0], "CLEAR_SELECTION")

        arcpy.Buffer_analysis(plotting_data[0], os.path.join(palm_buffer_point_location,"buffer_for_masking"), "buffer", "FULL", "ROUND", "NONE", "", "PLANAR")

        buffer_list = list(set([str(row.getValue("ORIG_FID")) for row in arcpy.SearchCursor("buffer_for_masking", fields="ORIG_FID")]))

        for buff in buffer_list:
            selection = arcpy.SelectLayerByAttribute_management("buffer_for_masking","NEW_SELECTION","\"fidcopy\"={}".format(buff))

            arcpy.Clip_analysis("ileaf","buffer_for_masking",os.path.join(location_masking,"ileaf_{}".format(buff)))

            arcpy.FeatureVerticesToPoints_management("ileaf_{}".format(buff), os.path.join(self.loc_gdb,"pointl_{}".format(buff)), "ALL")

            arcpy.PointDistance_analysis("palm_{}".format(buff),"pointl_{}".format(buff),os.path.join(self.loc_gdb,"path_{}".format(buff)))

            arcpy.TableToTable_conversion("path_{}".format(buff),dbf_location,"path_{}.dbf".format(buff))

            df_plot = Dbf5(os.path.join(dbf_location,"path_{}.dbf".format(buff))).to_dataframe()

            df_plot = df_plot.sort_values('DISTANCE',ascending=True)

            distance_used = list(df_plot["DISTANCE"])[len(df_plot)/3]

            arcpy.Buffer_analysis("palm_{}".format(buff),os.path.join(self.loc_gdb,"outer_{}".format(buff)),"{} Meters".format(distance_used),"FULL","ROUND","NONE","","PLANAR")

            substring = "pointl"
            substring_2 = "ileaf_"
            # substring_3 = "palm_{}".format(buff)
            substring_4 = "leaf_"

            for layer in arcpy.mapping.ListLayers(mxd):
                if str(layer).find(substring) != -1 or str(layer).find(substring_2) != -1 or str(layer).find(substring_4) != -1:
                    arcpy.mapping.RemoveLayer(df,layer)

        substring_merge = "outer"
        outer = []
        for merge in arcpy.mapping.ListLayers(mxd):
            if str(merge).find(substring_merge) != -1:
                outer.append(str(merge))

        s = ";".join(outer)

        arcpy.Merge_management(s,os.path.join(loc_gdb,"outer_ring"))

        arcpy.FeatureClassToFeatureClass_conversion("outer_ring",buffer_last_location,"crown_ring_fwd")

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != "crown_ring_fwd" and str(layer) != "crown_ring_wd" and str(layer) != "crown_ring_nwd" and str(layer) != "fwd_exp" and str(layer) != plotting_area[0] and str(layer) != plotting_data[0]:
                arcpy.mapping.RemoveLayer(df,layer)

class process_shape:
    def __init__(self,data_process,main_location,loc_gdb,export_name):
        self.data_process = data_process
        self.main_location = main_location
        self.loc_gdb = loc_gdb
        self.export_name = export_name

        arcpy.Near_analysis(self.data_process,self.data_process,"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")
        try:
            arcpy.AddField_management(self.data_process,"ket","TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "buffer", "DOUBLE", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")

            arcpy.AddField_management(self.data_process, "fidcopy", "SHORT", "10", "10", "", "", "NULLABLE", "NON_REQUIRED", "")
        except Exception:
            pass

        #Processing Shapefile
        arcpy.CalculateField_management(self.data_process, "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

        arcpy.CalculateField_management(self.data_process, "buffer", "[NEAR_DIST] / 1.5", "VB", "")

        arcpy.CalculateField_management(self.data_process, "fidcopy", "[FID]", "VB", "")

        mylist_dist = list(([float(row.getValue("NEAR_DIST")) for row in arcpy.SearchCursor(self.data_process, fields="NEAR_DIST")]))

        mylist_fid = list(([int(row.getValue("fidcopy")) for row in arcpy.SearchCursor(self.data_process, fields="fidcopy")]))

        ziped = dict(zip(mylist_dist,list(mylist_fid)))

        fids_to_delete = []
        for key, value in ziped.items():
            if float(key) <= 1.0:
                fids_to_delete.append(value)

        if len(fids_to_delete) > 0:
            for fid_to_delete in fids_to_delete:
                arcpy.SelectLayerByAttribute_management(self.data_process,"NEW_SELECTION","\"fidcopy\" = {}".format(fid_to_delete))

                arcpy.DeleteFeatures_management(self.data_process)

            arcpy.Near_analysis(self.data_process,self.data_process,"100 Meters","NO_LOCATION","NO_ANGLE","PLANAR")

            arcpy.CalculateField_management(self.data_process, "ket", "new_class( !NEAR_DIST!)", "PYTHON_9.3", "def new_class(x):\\n    if x <= 6.5:\\n        return \"Very Close\"\\n    elif x > 6.5 and x <= 7.5:\\n        return \"Close\"\\n    elif x >7.5:\\n        return \"Normal\"")

            arcpy.CalculateField_management(self.data_process, "buffer", "[NEAR_DIST] / 1.5", "VB", "")

            arcpy.CalculateField_management(self.data_process, "fidcopy", "[FID]", "VB", "")  

        mylist_dist = list(([float(row.getValue("NEAR_DIST")) for row in arcpy.SearchCursor(self.data_process, fields="NEAR_DIST")]))
        
        for dist in mylist_dist:
            if float(dist) < 5.0:
                arcpy.SelectLayerByAttribute_management(self.data_process,"NEW_SELECTION","\"NEAR_DIST\" = {}".format(dist))

                arcpy.CalculateField_management(self.data_process, "buffer", "[NEAR_DIST] / 0.8", "VB", "")

        for fid in mylist_fid:
            selection = arcpy.SelectLayerByAttribute_management(self.data_process,"NEW_SELECTION","\"fidcopy\"={}".format(fid))

            arcpy.CopyFeatures_management(selection,os.path.join(palm_buffer_point_location,"palm_{}.shp".format(fid)))
        
        arcpy.SelectLayerByAttribute_management(self.data_process, "CLEAR_SELECTION")

        arcpy.Buffer_analysis(self.data_process, os.path.join(palm_buffer_point_location,"buffer_for_masking"), "buffer", "FULL", "ROUND", "NONE", "", "PLANAR")

        buffer_list = list(set([str(row.getValue("ORIG_FID")) for row in arcpy.SearchCursor("buffer_for_masking", fields="ORIG_FID")]))

        for buff in buffer_list:
            selection = arcpy.SelectLayerByAttribute_management("buffer_for_masking","NEW_SELECTION","\"fidcopy\"={}".format(buff))

            arcpy.Clip_analysis("ileaf","buffer_for_masking",os.path.join(location_masking,"ileaf_{}".format(buff)))

            arcpy.SelectLayerByAttribute_management("buffer_for_masking", "CLEAR_SELECTION")

            arcpy.AddField_management("ileaf_{}".format(buff), "Shape_area", "DOUBLE")

            exp = "!SHAPE.AREA@SQUAREMETERS!"

            arcpy.CalculateField_management("ileaf_{}".format(buff), "Shape_area", exp, "PYTHON_9.3")

            area_list = list(set([float(row.getValue("Shape_area")) for row in arcpy.SearchCursor("ileaf_{}".format(buff), fields="Shape_area")]))

            max_area = max(area_list)

            selection_2 = arcpy.SelectLayerByAttribute_management("ileaf_{}".format(buff), "NEW_SELECTION", "Shape_area = {}".format(max_area))

            arcpy.MultipartToSinglepart_management("ileaf_{}".format(buff), os.path.join(self.loc_gdb,"expld_{}".format(buff)))

            arcpy.DeleteFeatures_management("ileaf_{}".format(buff))

            arcpy.Merge_management("ileaf_{};expld_{}".format(buff,buff),os.path.join(self.main_location,"ileafn_{}".format(buff)))

            area_list_new = list(set([float(row.getValue("Shape_area")) for row in arcpy.SearchCursor("ileafn_{}".format(buff), fields="Shape_area")]))

            max_area_new = max(area_list_new)

            selection_3 = arcpy.SelectLayerByAttribute_management("ileafn_{}".format(buff),"NEW_SELECTION","Shape_Area={}".format(max_area_new))

            arcpy.CopyFeatures_management(selection_3,os.path.join(leaf_location,"leaf_{}".format(buff)))

            arcpy.FeatureVerticesToPoints_management("leaf_{}".format(buff), os.path.join(self.loc_gdb,"pointl_{}".format(buff)), "ALL")

            arcpy.PointDistance_analysis("palm_{}".format(buff),"pointl_{}".format(buff),os.path.join(self.loc_gdb,"path_{}".format(buff)))

            arcpy.TableToTable_conversion("path_{}".format(buff),dbf_location,"path_{}.dbf".format(buff))

            df_plot = Dbf5(os.path.join(dbf_location,"path_{}.dbf".format(buff))).to_dataframe()

            max_distance_for_buffer = float(df_plot['DISTANCE'].max())

            arcpy.Buffer_analysis("palm_{}".format(buff),os.path.join(self.loc_gdb,"outer_{}".format(buff)),"{} Meters".format(max_distance_for_buffer),"FULL","ROUND","NONE","","PLANAR")

            substring = "pointl"
            substring_2 = "ileaf_"
            # substring_3 = "palm_{}".format(buff)
            substring_4 = "leaf_"

            for layer in arcpy.mapping.ListLayers(mxd):
                if str(layer).find(substring) != -1 or str(layer).find(substring_2) != -1 or str(layer).find(substring_4) != -1:
                    arcpy.mapping.RemoveLayer(df,layer)

        substring_merge = "outer"
        outer = []
        for merge in arcpy.mapping.ListLayers(mxd):
            if str(merge).find(substring_merge) != -1:
                outer.append(str(merge))

        s = ";".join(outer)

        arcpy.Merge_management(s,os.path.join(self.loc_gdb,"outer_ring"))

        arcpy.FeatureClassToFeatureClass_conversion("outer_ring",buffer_last_location,self.export_name)

        for layer in arcpy.mapping.ListLayers(mxd):
            if str(layer) != "crown_ring_fwd" and str(layer) != "crown_ring_nwd" and str(layer) != "crown_ring_wd" and str(layer) != plotting_data_tif[0] and str(layer) != plotting_data[0] and str(layer) != plotting_area[0]:
                arcpy.mapping.RemoveLayer(df,layer)

class all_process:
    @staticmethod
    def all_process():
        location = os.path.expanduser('~/Documents/Avirtech/Avirkey/Avirkey.ini')
        if exists(location):
            initiation_process.initiate_process()
            starting_first.starting_process()

            mylist_areatype = list(set([str(row.getValue("ket")) for row in arcpy.SearchCursor(plotting_area[0], fields="ket")]))

            outputgdb = "crowndetection.gdb"

            global areatype
            for areatype in mylist_areatype:
                if str(areatype) == "fwd":
                    name = "fwd"
                    os.mkdir(os.path.join(gdb_location,"fwd"))
                    fwd_location = os.path.join(gdb_location,"fwd")
                    arcpy.CreateFileGDB_management(fwd_location,outputgdb)

                    fwd_loc_gdb = os.path.join(fwd_location,outputgdb)

                    create_folder(fwd_location).create_folder()
                    process_first(fwd_loc_gdb,name)
                    processing_raster_full_grassy(fwd_location,fwd_loc_gdb)
                
                elif str(areatype) == "wd":
                    name = "wd"
                    data = "wd_exp"
                    data_process = "wd_point"
                    export_name = "crown_ring_wd"
                    os.mkdir(os.path.join(gdb_location,"wd"))
                    wd_location = os.path.join(gdb_location,"wd")
                    arcpy.CreateFileGDB_management(wd_location,outputgdb)

                    wd_loc_gdb = os.path.join(wd_location,outputgdb)

                    create_folder(wd_location).create_folder()
                    process_first(wd_location,name)
                    processing_raster_medium_grass(data,wd_location)
                    process_shape(data_process,wd_location,wd_loc_gdb,export_name)
                
                elif str(areatype) == "nwd":
                    name = "nwd"
                    data = "nwd_exp"
                    data_process = "nwd_point"
                    export_name = "crown_ring_nwd"
                    os.mkdir(os.path.join(gdb_location,"nwd"))
                    nwd_location = os.path.join(gdb_location,"nwd")
                    arcpy.CreateFileGDB_management(nwd_location,outputgdb)

                    nwd_loc_gdb = os.path.join(nwd_location,outputgdb)

                    create_folder(nwd_location).create_folder()
                    process_first(nwd_location,name)
                    processing_raster_non_grassy(data,nwd_location)
                    process_shape(data_process,nwd_location,nwd_loc_gdb,export_name)
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("showinfo","You don't have Avirkey or maybe your Avirkey is not properly installed, please generate your serial number first!")
            root.destroy
