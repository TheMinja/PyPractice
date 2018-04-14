from enum import Enum
import math

class Pro(Enum):
    free_speed_rpm = 18730
    free_current = .7
    maximum_power = 347
    stall_torque = 6.28
    stall_current = 134
    motor_kt = stall_torque/stall_current
    resistance = 12/stall_current
    motor_kv = ((free_speed_rpm/60)*math.pi*2)/(12-resistance*free_current)

class Bag(Enum):
    free_speed_rpm = 13180
    free_current = 1.8
    maximum_power = 149
    stall_torque = 3.81
    stall_current = 53
    motor_kt = stall_torque/stall_current
    resistance = 12/stall_current
    motor_kv = ((free_speed_rpm/60)*math.pi*2)/(12-resistance*free_current)

class Cim(Enum):
    free_speed_rpm = 5330
    free_current = 2.7
    maximum_power = 337
    stall_torque = 21.33
    stall_current = 131
    motor_kt = stall_torque/stall_current
    resistance = 12/stall_current
    motor_kv = ((free_speed_rpm/60)*math.pi*2)/(12-resistance*free_current)

class MiniCim(Enum):
    free_speed_rpm = 5840
    free_current = 3
    maximum_power = 215
    stall_torque = 12.48
    stall_current = 89
    motor_kt = stall_torque / stall_current
    resistance = 12 / stall_current
    motor_kv = ((free_speed_rpm / 60) * math.pi * 2) / (12 - resistance * free_current)