# ---------------------------------------------------------------------------
# Buffer_Test.py
# Created on: Thu Mar 18 2010 02:32:19 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
BufferTest_shp = "D:\\gis\\scripts\\Python\\Test\\BufferTest.shp"
nymc_shp = "D:\\gis\\data\\Municipal\\NY\\New_York_City\\Community_Districts\\nymc_09c_av\\nymc.shp"

# Process: Buffer...
gp.Buffer_analysis(nymc_shp, BufferTest_shp, "500 Feet", "FULL", "ROUND", "ALL", "")

