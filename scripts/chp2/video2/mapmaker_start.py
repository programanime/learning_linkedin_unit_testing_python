class Point():
    def __init__(self, name, latitude, longitude):
        self.name=name
        self._latitude=latitude
        self._longitude=longitude
        Point.check_parameters(latitude, longitude)
        Point.check_name(name)
    
    
    def check_name(name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
    
    
    def check_parameters(latitude, longitude):
        if  latitude < -90 or latitude >90 or longitude < -180 or longitude > 180:
            raise ValueError("Invalid latitude or longitude")
    
    def get_location(self):
        return (self._latitude, self._longitude)
    
