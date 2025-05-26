#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------
# point2D.py
# An "abstract" class defining a 2D point
#
# Author: Jorge Londoño
#-----------------------------------------------------------------------

import math
from abc import ABC, abstractmethod

class Point2D(ABC):
    """Class representing points in the plane
    """

    def distance(self, other:'Point2D') -> float:
        """Computes the distance to other Point2D
        """
        return math.sqrt( (self.getX()-other.getX())**2 + (self.getY()-other.getY())**2 )
    
    @abstractmethod
    def __abs__(self) -> float:
        """Returns the distance to the origin (magnitude)
        
        Not defined, must be implemented in subclasses
        """
        pass
    
    @abstractmethod
    def angle(self) -> float:
        """Returns the angle to the x axis
        
        Not defined, must be implemented in subclasses
        """
        pass
    
    @abstractmethod
    def getX(self) -> float:
        """Returns the x component
        
        Not defined, must be implemented in subclasses
        """
        pass

    @abstractmethod
    def getY(self) -> float:
        """Returns the y component
        
        Not defined, must be implemented in subclasses
        """
        pass
    
    def __eq__(self, other:object) -> bool:
        """Returns True if the value of self is equal (or very close) to the value of other
        """
        if other is not None:
            if isinstance(other, Point2D):
                if self.distance(other)<1E-15:
                    return True
        return False