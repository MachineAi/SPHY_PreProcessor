# SPHY model Pre-Processor interface plugin for QGIS
Version 1.0 (developed by FutureWater)

This interface is developed as plugin for QGIS, and is used to create SPHY model input data based on a database.   
Currently two databases are available to be used with the Pre-Processor:
<ol>
<li>Hindu-Kush-Himalaya</li>
<li>Southeast Africa</li>
</ol>

These databases can be downloaded from the <a href="http://www.sphy.nl/software/" target="_blank">SPHY model website</a>.
SPHY model manuals and case-studies can also be found on this website.

The Pre-Processor plugin uses data from Natural Earth as background layers. This is not included in this repository due
to its file size. You can download a countries shapefile and raster data from the <a href="http://www.naturalearthdata.com/downloads/" target="_blank">Natural Earth</a> website.
After downloading, create a "NaturalEarthData" folder inside the "SphyPreProcess" folder. Within the "NaturalEarthData" folder you need to:
<ol>
<li>Paste the downloaded shapefile and rename it to: "ne_10m_admin_0_countries.shp"</li>
<li>Create a "HYP_50M_SR_W" folder and paste the raster into this folder and name it to: "HYP_50M_SR_W/HYP_50M_SR_W.tif"</li>
</ol> 

********************************************************************************
Minimum system requirements:

- Windows 7 or later version
- QGIS 2.4 or later version
