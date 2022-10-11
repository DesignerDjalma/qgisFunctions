
from qgis.core import *

# Supply path to qgis install location
QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.

layer = qgis.utils.iface.mapCanvas().currentLayer()

field_name = "CODNUT2"
idx = layer.fields().indexOf(field_name)
unique_values = layer.uniqueValues(idx)

folder = "/path/to/folder"

for value in unique_values:
    
    file_path = f"{folder}/_{value}.shp"
    layer.selectByExpression(f"{field_name}='{value}'")
    
    QgsVectorFileWriter.writeAsVectorFormat(
        layer, file_path, 'utf-8', layer.crs(), "ESRI Shapefile", onlySelected=True
        )


import os # This is is needed in the pyqgis console also
from qgis.core import (
    QgsVectorLayer
)

# get the path to the shapefile e.g. /home/project/data/ports.shp
path_to_airports_layer = "testdata/airports.shp"

# The format is:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(path_to_airports_layer, "Airports layer", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)


# GEOPACKAGE

# get the path to a geopackage  e.g. /usr/share/qgis/resources/data/world_map.gpkg
path_to_gpkg = os.path.join(QgsApplication.pkgDataPath(), "resources", "data", "world_map.gpkg")
# append the layername part
gpkg_countries_layer = path_to_gpkg + "|layername=countries"
# e.g. gpkg_places_layer = "/usr/share/qgis/resources/data/world_map.gpkg|layername=countries"
vlayer = QgsVectorLayer(gpkg_countries_layer, "Countries layer", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)


# FASTEST WAY
vlayer = iface.addVectorLayer(path_to_airports_layer, "Airports layer", "ogr")
if not vlayer:
  print("Layer failed to load!")

# RASTER 
# get the path to a tif file  e.g. /home/project/data/srtm.tif
path_to_tif = "qgis-projects/python_cookbook/data/srtm.tif"
rlayer = QgsRasterLayer(path_to_tif, "SRTM layer name")
if not rlayer.isValid():
    print("Layer failed to load!")
# FAST
iface.addRasterLayer(path_to_tif, "layer name you like")


# first add the layer without showing it
QgsProject.instance().addMapLayer(rlayer, False)
# obtain the layer tree of the top-level group in the project
layerTree = iface.layerTreeCanvasBridge().rootGroup()
# the position is a number starting from 0, with -1 an alias for the end
layerTree.insertChildNode(-1, QgsLayerTreeLayer(rlayer))

# QgsProject.instance().removeMapLayer(layer_id)
QgsProject.instance().removeMapLayer(rlayer.id())

# lista de camadas carregadas e IDs de camada
QgsProject.instance().mapLayers()

# list of layer names using list comprehension
l = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
# dictionary with key = layer name and value = layer object
layers_list = {}
for l in QgsProject.instance().mapLayers().values():
  layers_list[l.name()] = l

print(layers_list)



country_layer = QgsProject.instance().mapLayersByName("countries")[0]

# ARVORES DE NOS DE CAMADAS E GRUPPOS
root = QgsProject.instance().layerTreeRoot()

