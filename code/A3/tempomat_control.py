from enum import Enum
class OperatingMode(Enum):
    NOTHING = 1
    SLOW_DOWN = 2
    ACCELERATE = 3
    EMERGENCY_STOP = 4

def tempomat_control(speed, wanted_speed):
    if wanted_speed < 0:
        return OperatingMode.EMERGENCY_STOP
    elif speed < 0.0 or speed > 300.0:
        return OperatingMode.NOTHING
    elif speed / float(wanted_speed) < .98:
        return OperatingMode.ACCELERATE
    elif speed / float(wanted_speed) > 1.02:
        return OperatingMode.SLOW_DOWN
    else:
        return OperatingMode.NOTHING


CheckResult.check(tempomat_control(50, -3), OperatingMode.EMERGENCY_STOP)
CheckResult.check(tempomat_control(50, 49), OperatingMode.SLOW_DOWN)
CheckResult.check(tempomat_control(50, 51), OperatingMode.NOTHING)
CheckResult.check(tempomat_control(50, 55), OperatingMode.ACCELERATE)
