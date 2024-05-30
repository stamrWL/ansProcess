from enum import Enum,IntEnum


class UsstEventStatus:
    wait = 0
    run = 1
    end = 2
    abnormal = 3

class UsstEventType(IntEnum):
    InitTask = -1

    preTransmission = 0
    Transmission = 1

    preProcess = 10
    waitProcess = 11
    Process = 12

    preAllocation = 30
    waitAllocation = 31
    Allocation = 32

    End = 40

    AbnormalEnd = 50        