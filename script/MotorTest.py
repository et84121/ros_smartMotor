import smartMotor

def print_help():
    print("input '{MotorNum} test' to test the Motor")
    print("      '{MotorNum} s'    to stop the Motor")
    print("      '{MotorNum} up {V}' to updateVelocity the Motor")
    print("      'exit' to exit the program")
    print("      'help' to print this text again")
    print("ps: If MotorNum is zero ,serial output will not add motor ID")


SM = smartMotor.SmartMotor("/dev/ttyUSB0",9600)
SM.setupSerialConnection()
print_help()

while(1):
    msg = str(input("input your command : ")).split(" ")
    if msg[0] == 'exit':
        exit()
    elif msg[0] == 'help':
        print_help()
    elif int(msg[0]) == 0:
        if msg[1] == 'test':
            SM.move_test(0)
        if msg[1] == 's':
            SM.stop(0)
        if msg[1] == 'up':
            SM.updateVelocity(_velocity=int(msg[2]),_Acceleration=1000,_MotorNum=0)
    elif int(msg[0]) != 0:
        motorNum = int(msg[0])
        motorNum = motorNum + 128
        if msg[1] == 'test':
            SM.move_test(motorNum)
        if msg[1] == 's':
            SM.stop(motorNum)
        if msg[1] == 'up':
            SM.updateVelocity(_velocity=int(msg[2]),_Acceleration=1000,_MotorNum=motorNum)
    else:
        print("Can't find the command")
