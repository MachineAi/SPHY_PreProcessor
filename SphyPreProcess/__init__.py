# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SphyPreProcess
                                 A QGIS plugin
 A tool to convert raw data into SPHY model input data
                             -------------------
        begin                : 2015-06-23
        copyright            : (C) 2015 by W. Terink, FutureWater
        email                : w.terink@futurewater.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SphyPreProcess class from file SphyPreProcess.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SPHY_preprocess import SphyPreProcess
    return SphyPreProcess(iface)
