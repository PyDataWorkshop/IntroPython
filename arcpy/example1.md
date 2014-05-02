Printing the spatial reference of a feature class
==================================================


This first example script reports the spatial reference (coordinate system) of a feature class stored in a geodatabase:

<pre><code>
# Opens a feature class from a geodatabase and prints the spatial reference
 
import arcpy
 
featureClass = "C:/Data/USA/USA.gdb/StateBoundaries"
 
# Describe the feature class and get its spatial reference   
desc = arcpy.Describe(featureClass)
spatialRef = desc.SpatialReference
 
# Print the spatial reference name
print spatialRef.Name

</code></pre>
