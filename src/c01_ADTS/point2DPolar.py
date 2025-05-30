#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------
# Point2DPolar.py
# An implementation of the Point2D using the polar representation
#
# Author: Jorge Londoño
#-----------------------------------------------------------------------

import math
from .point2D import Point2D

class Point2DPolar(Point2D):
    """Class representing points in the plane using polar coordinates
    """

    def __init__(self, r:float, theta:float):
        """Constructs a Point2D instance from the x,y coordinates
        """
        self._radius = r
        self._theta = theta
        
    def __str__(self) -> str:
        """Returns a String representation of the point
        """
        return "Mag="+str(self._radius)+", angle="+str(self._theta)
    
    def __abs__(self) -> float:
        """Returns the distance to the origin (magnitude)
        """
        return self._radius
    
    def angle(self) -> float:
        """Returns the angle to the x axis
        """
        return self._theta

    def getX(self) -> float:
        """Returns the x component
        """
        return self._radius*math.cos(self._theta)

    def getY(self) -> float:
        """Returns the y component
        """
        return self._radius*math.sin(self._theta)