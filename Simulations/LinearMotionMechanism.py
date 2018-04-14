import matplotlib.pyplot as plt
from enum import Enum
from matplotlib import pyplot as plt
import numpy as np


class Pro(Enum):
    free_speed_rpm = 18730
    free_current = .7
    maximum_power = 347
    stall_torque = 6.28
    stall_current = 134
    motor_kt = 6.28/134
    resistance = 12/134
    motor_kv = ((18730/60)*np.pi*2)/(12-(12/34)*.7)


class Bag(Enum):
    free_speed_rpm = 13180
    free_current = 1.8
    maximum_power = 149
    stall_torque = 3.81
    stall_current = 53
    motor_kt = 3.81/53
    resistance = 12/53
    motor_kv = ((13180/60)*np.pi*2)/(12-(12/53)*1.8)


class Cim(Enum):
    free_speed_rpm = 5330
    free_current = 2.7
    maximum_power = 337
    stall_torque = 21.33
    stall_current = 131
    motor_kt = 21.33/131
    resistance = 12/131
    motor_kv = ((5330/60)*np.pi*2)/(12-(12/131)*2.7)


class MiniCim(Enum):
    free_speed_rpm = 5840
    free_current = 3
    maximum_power = 215
    stall_torque = 12.48
    stall_current = 89
    motor_kt = 12.48 / 89
    resistance = 12 / 89
    motor_kv = ((5840 / 60) * np.pi * 2) / (12 - (12/89) * 3)


gear_ratio = None
motor = None
motor_count = None
mass_on_system = None
velocity_constant = None
torque_constant = None
pulley_radius = None
motor_resistance = None
current_voltage = 0
current_mechanism_position = 0
current_mechanism_velocity = 0
current_mechanism_acceleration = 0
position_values = []
velocity_values = []
acceleration_values = []
time = []


class MotorType(Enum):
    pro = 1
    bag = 2
    cim = 3
    mini_cim = 4


def __init__():
    global gear_ratio
    gear_ratio = 25
    global motor
    motor = MotorType.cim
    global motor_count
    motor_count = 2
    global mass_on_system
    mass_on_system = 30
    global pulley_radius
    pulley_radius = .855
    set_motor_values()


def set_motor_values():
    global velocity_constant
    global torque_constant
    global motor_resistance
    global motor_count
    if motor == MotorType.pro:
        velocity_constant = Pro.motor_kv.value
        torque_constant = Pro.motor_kt.value
        motor_resistance = Pro.resistance.value
    elif motor == MotorType.bag:
        velocity_constant = Bag.motor_kv.value
        torque_constant = Bag.motor_kt.value
        motor_resistance = Bag.resistance.value
    elif motor == MotorType.cim:
        velocity_constant = Cim.motor_kv.value
        torque_constant = Cim.motor_kt.value
        motor_resistance = Cim.resistance.value
    elif motor == MotorType.mini_cim:
        velocity_constant = MiniCim.motor_kv.value
        torque_constant = MiniCim.motor_kt.value
        motor_resistance = MiniCim.resistance.value
    else:
        raise TypeError('invalid motor type')
    torque_constant = torque_constant*2*motor_count


def update_voltage(voltage):
    global current_voltage
    current_voltage = voltage


def periodic(interval_in_ms):
    global current_voltage
    calculate_distance(interval_in_ms)
    calculate_mechanism_velocity(interval_in_ms, current_voltage)


def calculate_mechanism_acceleration(voltage):
    global current_mechanism_acceleration
    global torque_constant
    global gear_ratio
    global velocity_constant
    global motor_resistance
    global pulley_radius
    global mass_on_system
    global current_mechanism_velocity

    current_mechanism_acceleration = (-torque_constant * gear_ratio * gear_ratio / (velocity_constant * motor_resistance * pulley_radius * pulley_radius * mass_on_system) * current_mechanism_velocity + gear_ratio * torque_constant / (motor_resistance * pulley_radius * mass_on_system) * voltage)
    return current_mechanism_acceleration


def calculate_mechanism_velocity(interval_in_ms, voltage):
    global current_mechanism_velocity
    current_mechanism_velocity = current_mechanism_velocity + ms_to_seconds(interval_in_ms)*calculate_mechanism_acceleration(voltage)


def ms_to_seconds(time_in_ms):
    return time_in_ms * .001


def calculate_distance(interval_in_ms):
    global current_mechanism_position
    current_mechanism_position = current_mechanism_position + ms_to_seconds(interval_in_ms)*current_mechanism_velocity


def __main__():
    global current_mechanism_position
    global current_mechanism_velocity
    global current_mechanism_acceleration
    global position_values
    global velocity_values
    global acceleration_values

    __init__()
    i = 0
    while current_mechanism_position < 40:
        position_values.append(current_mechanism_position)
        velocity_values.append(current_mechanism_velocity)
        acceleration_values.append(current_mechanism_acceleration)
        time.append(i)

        update_voltage(12)
        periodic(1)
        i += 1
        if i%100 == 0:
            print(i, ':', "\tPosition", current_mechanism_position, " \t Velocity: ", current_mechanism_velocity, " \t Acceleration: ", current_mechanism_acceleration)


__main__()

plt.plot(time, velocity_values)
plt.plot(time, acceleration_values)
plt.plot(time, position_values)
plt.legend(['velocity', 'acceleration', 'position'], loc='upper right')

plt.show()

