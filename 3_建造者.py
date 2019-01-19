class 建造者(object):
    def __init__(self):
        self.builder = None
 
    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()
 
    def get_building(self):
        return self.builder.building
 
 
# Abstract Builder
class 造物(object):
    def __init__(self):
        self.building = None
 
    def new_building(self):
        self.building = 建筑物()
 
 
# Concrete Builder
class 造大楼(造物):
    def build_floor(self):
        self.building.floor = 'One'
 
    def build_size(self):
        self.building.size = 'Big'
 
 
class 造公寓(造物):
    def build_floor(self):
        self.building.floor = 'More than One'
 
    def build_size(self):
        self.building.size = 'Small'
 
 
# Product
class 建筑物(object):
    def __init__(self):
        self.floor = None
        self.size = None
 
    def __repr__(self):
        return 'Floor: %s | Size: %s' % (self.floor, self.size)
 
 
# Client
if __name__ == "__main__":
    director = 建造者()
    director.builder = 造大楼()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = 造公寓()
    director.construct_building()
    building = director.get_building()
    print(building)