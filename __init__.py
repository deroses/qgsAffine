# -*- coding: utf-8 -*-
"""
/***************************************************************************
 qgsAffine
                                 A QGIS plugin
 Apply affine transformations to selected geometries.
                             -------------------
        begin                : 2012-07-12
        copyright            : (C) 2012 by Mauricio de Paulo
        email                : mauricio.dev@gmail.com
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
def name():
    return "qgsAffine"
def description():
    return "Apply affine transformations to selected geometries."
def version():
    return "Version 0.5.0"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    # load qgsAffine class from file qgsAffine
    from qgsAffine import qgsAffine
    return qgsAffine(iface)
