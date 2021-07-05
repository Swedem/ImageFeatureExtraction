# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FeatureExt
                                 A QGIS plugin
 Extract lines and polygon from image 
                             -------------------
        begin                : 2021-06-25
        copyright            : (C) 2021 by Kwesi_welbred
        email                : infofeedacc@gmail.com
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
    """Load FeatureExt class from file FeatureExt.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .FeatureExtraction import FeatureExt
    return FeatureExt(iface)
