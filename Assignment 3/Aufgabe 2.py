# @Author: AlexanderKomi
# @Date:   10-Jul-2017
# @Email:  Alexander.Komischke@gmx.de
# @Last modified by:   AlexanderKomi
# @Last modified time: 11-Jul-2017



def trivia(velocity, aim_velocity):
    return False if velocity < 0 or velocity > 300 else True

def tempomat_control(velocity, aim_velocity):
    if aim_velocity < 0 :
        return 'EMERGENCY_STOP'
    if trivia(velocity, aim_velocity) :
        percentage = (aim_velocity/100) * 2
        if velocity < (aim_velocity - percentage) :
            return 'ACCERLATE'
        elif velocity > (aim_velocity + percentage):
            return 'SLOW_DOWN'
    return 'NOTHING'

print(tempomat_control(40, 40))
print(tempomat_control(80, 40))
print(tempomat_control(40, 80))
print(tempomat_control(-1,50))
