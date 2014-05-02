Performing map algebra on a raster
====================================
<!--- https://www.e-education.psu.edu/geog485/node/116 ---->

Here’s another simple script that finds all cells over 3500 meters in an elevation raster and makes a new raster that codes all those cells as 1. Remaining values in the new raster are coded as 0. This type of “map algebra” operation is common in site selection and other GIS scenarios.

Something you may not recognize below is the expression Raster(inRaster). This function just tells ArcGIS that it needs to treat your inRaster variable as a raster dataset so that you can perform map algebra on it. If you didn't do this, the script would treat inRaster as just a literal string of characters (the path) instead of a raster dataset.

<pre><code>
# This script uses map algebra to find values in an
#  elevation raster greater than 3500 (meters).
 
import arcpy
from arcpy.sa import *
 
# Specify the input raster
inRaster = "C:/Data/Elevation/foxlake"
cutoffElevation = 3500
 
# Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")
 
# Make a map algebra expression and save the resulting raster
outRaster = Raster(inRaster) > cutoffElevation
outRaster.save("C:/Data/Elevation/foxlake_hi_10")
     
# Check in the Spatial Analyst extension now that you're done
arcpy.CheckInExtension("Spatial")
</code></pre>
