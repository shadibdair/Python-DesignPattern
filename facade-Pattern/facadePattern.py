class _IgnitionSystem(object):
    @staticmethod
    def produce_spark():
        return True
class _Engine(object):

    def __init__(self):
        self.revs_pre_minute=0
        
    def turnon(self):
        self.revs_pre_minute = 2000

    def turnof(self):
        self.revs_pre_minute = 0
    
class _FuelTank(object):

    def __init__(self,level=30):
        self._level = level

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self,level):
        self.level=level

class _DashboardLight(object):

    def __init__(self, is_on=False):
        self._is_on=_is_on

    def __str__(self):
        return self.__class__.__name__

class _HandBreakeLight(_DashboardLight):
    pass

class _FogLampLight(_DashboardLight):
    pass
class _Dashboard(object):
    def __init__(self):
        self.lights={"handbreak": _HandBreakeLight(),"fog": _FogLampLight()}

    def show(self):
        for lights in self.lights.values():
            lights.status_check()

# Facade
class Car(object):
    def __init__(self):
        self.ignition_system = _IgnitionSystem()
        self.engine = _Engine()
        self.fuel_tank= _FuelTank()
        self.dashboard = _Dashboard()

def main():
    car = Car()
    car.start()
    car.drive()

    car.switch_fog_lights("ON")
    car.switch_fog_lights("OFF")
    car.park()
    car.fill_up_tak()
    car.drive()

if __name__ == "__main__":
    main()
