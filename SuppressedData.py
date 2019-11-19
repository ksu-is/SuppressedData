>>> #set the map document we're working on
mxd = arcpy.mapping.MapDocument(r"Trowell_GunViolence.mxd")
#set the dataframe and layer we're searching in. 2nd parameter in df is the dataframe you want to work in, enter empty string
#for default df; 2nd parameter in lyr is the layer you want to work in. Case sensitive!
df = arcpy.mapping.ListDataFrames(mxd, "DeathsbyFirearm")[0]   
lyr = arcpy.mapping.ListLayers(mxd, "SoutheasternStates", df)[0]

#create feature layer (temp layer) to copy to; 1st parameter input layer, 2nd parameter output layer
arcpy.MakeFeatureLayer_management("Features.gdb/SoutheasternStates", "SuppressedData_lyr")
#select by attribute
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", "Crude_Ra_1 = Suppressed")
#selection is made, time to copy to new layer from selection
arcpy.CopyFeatures_management("SuppressedData_lyr", "Features.gdb/Crude_Ra_1")
