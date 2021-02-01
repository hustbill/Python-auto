# Use geoprocessing services in Python

import arcpy
import time

# Add a toolbox from a server
arcpy.ImportToolbox("http://flame7/arcgis/services;GP/BufferByVal", "mytools")

# Use GetParameterValue to get a featureset object with the default 
#   schema of the first parameter of the tool 'bufferpoints'
inFeatureSet = arcpy.GetParameterValue("bufferpoints", 0)

# Load a shapefile into the featureset
inFeatureSet.load("c:/base/roads.shp")

# Run a server tool named BufferPoints with featureset created above
result = arcpy.BufferPoints_mytools(inFeatureSet, "5 feet")

# Check the status of the result object every 0.2 seconds until it has a value 
#    of 4 (succeeded) or greater
while result.status < 4:
    time.sleep(0.2)

# Get the output FeatureSet back from the server and save to a local geodatabase
outFeatSet = result[0]
outFeatSet.save("c:/temp/base.gdb/towers_buffer")