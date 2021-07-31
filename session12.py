import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have 3 edges/vertices.')
        self.no_vertices = n
        self.circum_radius = R
        self.no_edges = n
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def no_vertices(self):
        return self._n
    
    @property
    def no_edges(self):
        return self._n
    
    @property
    def circum_radius(self):
        return self._R

    @no_vertices.setter
    def no_vertices(self, n):
        self._n = n
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None 
        self._area = None 
        self._perimeter = None

    @no_edges.setter
    def no_edges(self, n):
        self._n = n
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None 
        self._area = None 
        self._perimeter = None

    @circum_radius.setter
    def circum_radius(self, R):
        self._R = R
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None 
        self._area = None 
        self._perimeter = None
    
    @property
    def area(self):
        if self._area is None:
            print("Area is executed")
            self._area = math.pi * self.radius ** 2
        return self._area

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            print("interior_angle is executed")
            self._interior_angle = (self._n - 2) * 180.0 / self._n
        return self._interior_angle 

    @property
    def edge_length(self):
        if self._edge_length is None:
            print("edge_length is executed")
            self._edge_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._edge_length
    
    @property
    def apothem(self):
        if self._apothem is None:
            print("apothem is executed")
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            print("area is executed")
            self._area = self._n / 2.0 * self.edge_length * self.apothem
        return self._area 
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            print("perimeter is executed")
            self._perimeter = self._n * self.edge_length
        return self._perimeter 
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.no_edges == other.no_edges 
                    and self.circum_radius == other.circum_radius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.no_vertices > other.no_vertices
        else:
            return NotImplemented

class Polygon_Sequence:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('number of vertices for largest polygon in the sequence must be greater than 3')
        self._m = m
        self._R = R

    def __iter__(self):
        return self.PolygonIter(self._m, self._R)

    class PolygonIter:
        def __init__(self,m,R):
            self.i = 3
            self._m = m 
            self._R = R 

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self._m:
                raise StopIteration
            else:
                result = Polygon(self.i, self._R)
                self.i += 1
                return result
    
        
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(n={self._m}, R={self._R})'

def is_iterable(obj):
    try:
        iter(obj)
        return True

    except TypeError:
        return False