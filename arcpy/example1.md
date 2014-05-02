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

- A comment begins the script to explain what’s going to happen.
- Case sensitivity is applied in the code. "import" is all lower-case. So is "print". The module name "arcpy" is always referred to as "arcpy," not "ARCPY" or "Arcpy". Similarly, "Describe" is capitalized in arcpy.Describe.
- The variable names featureClass, desc, and spatialRef that the programmer assigned are short, but intuitive. - By looking at the variable name, you can quickly guess what it represents.
- The script creates objects and uses a combination of properties and methods on those objects to get the job done. That’s how object-oriented programming works.
