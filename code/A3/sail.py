from enum import Enum
class WindTo(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
class ShipPos(Enum):
    EUROPE = 1
    AFRICA = 2
    LOST = 3
    AMERICA = 4

def sail(ship_pos, wind_to):
    if ship_pos == ShipPos.LOST:
        return ShipPos.LOST
    elif ship_pos == ShipPos.EUROPE:
        if wind_to == WindTo.NORTH:
            return ShipPos.LOST
        elif wind_to == WindTo.SOUTH:
            return ShipPos.AFRICA
        elif wind_to == WindTo.EAST:
            return ShipPos.LOST
        elif wind_to == WindTo.WEST:
            return ShipPos.AMERICA
    elif ship_pos == ShipPos.AFRICA:
        if wind_to == WindTo.NORTH:
            return ShipPos.EUROPE
        elif wind_to == WindTo.SOUTH:
            return ShipPos.LOST
        elif wind_to == WindTo.EAST:
            return ShipPos.LOST
        elif wind_to == WindTo.WEST:
            return ShipPos.AMERICA
    elif ship_pos == ShipPos.AMERICA:
        if wind_to == WindTo.NORTH:
            return ShipPos.LOST
        elif wind_to == WindTo.SOUTH:
            return ShipPos.AFRICA
        elif wind_to == WindTo.EAST:
            return ShipPos.EUROPE
        elif wind_to == WindTo.WEST:
            return ShipPos.LOST
    return ShipPos.LOST

CheckResult.check(sail(ShipPos.EUROPE, WindTo.NORTH), ShipPos.LOST) #LOST
CheckResult.check(sail(ShipPos.AMERICA, WindTo.EAST), ShipPos.EUROPE) #EUROPE
CheckResult.check(sail(ShipPos.AFRICA, WindTo.NORTH), ShipPos.EUROPE) #EUROPE
