import smartMotor

SM = smartMotor.SmartMotor("/dev/ttyUSB0",9600)
SM.setupSerialConnection()

print("input 'test' to test the Motor")
print("      's'    to stop the Motor")
print("      'exit' to exit the program")

while(1):
    msg = input()
    if(msg == 'test'):
        SM.move_test(129)
    if(msg == 's'):
        SM.stop(129)
    if(msg == 'exit'):
        exit()
