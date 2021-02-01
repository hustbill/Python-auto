ArcGIS ArcPy Examples
=====================


What is ArcPy?
--------------
ArcPy is a Python site package that provides a useful and productive way to perform geographic data analysis, data conversion, data management, and map automation with Python.

In the example, two string variables are used to define the input and output parameters to make the call to the tool easier to read. 
```python
import arcpy

roads = "c:/base/data.gdb/roads"
output = "c:/base/data.gdb/roads_Buffer"

# Run Buffer using the variables set above and pass the remaining 
# parameters in as strings
arcpy.Buffer_analysis(roads, output, "distance", "FULL", "ROUND", "NONE")

```

Use geoprocessing services in Python
-------------------------------------
In the following example, the GetParameterValue function is used to get a FeatureSet object from a server tool. This FeatureSet object contains the schema of the tool's input parameter. The FeatureSet object is then loaded with a feature class, and the server tool is executed on the server. The script ends by using the Result object's getOutput method to get the tool output's, which is then saved locally by using the FeatureSet save method.

