#!/usr/bin/env python
import serial, rospy, binascii, io

class SmartMotor:
    Acceleration   = None
    Velocity       = None
    Postion        = None
    Torque         = None
    Mode           = None
    Mode_dit        = {'P':Postion, 'V':Velocity, 'T':Torque}
    def __init__(self,_port,_baudrate):
        self.port     = _port
        self.baudrate = _baudrate
        
        rospy.loginfo("set SmartMotor port:%s baudrate:%d" % self.port,self.baudrate)
    
    def setupSerialConnection(self):
        self.ser = serial.Serial(
            port = self.port ,
            baudrate = self.baudrate,
            timeout = 120)
        try:
            self.ser.open()
        except :
            print("SmartMotor serial port open error. Port: %s baudrate:%s" % (self.port,self.baudrate))
            rospy.logerr("SmartMotor serial port open error. Port: %s baudrate:%s" % (self.port,self.baudrate))
                
    def giveupSerialConnection(self):
        try:
            self.ser.close()
        except:
            print("SmartMotor serialPort close error")
            rospy.logwarn("SmartMotor serial Port close error")
            
    def isConnected(self):
        if self.ser._isOpen():
            print('serialConnection open correctly')
            rospy.loginfo('SmartMotor serialConnection open correctly')
            return(True)
        else:
            print('serialConnection open fail')
            rospy.loginfo('SmartMotor serialConnection open fail')
            return(False)    
    
    def move_test(self, MotorNum=0):
        self.write(msg="MT\n")
        self.Mode = self.Mode_dit['T']
        self.write(msg="T=500\n")
        self.write(msg="G\n")
        
    def write(self, msg, MotorNum=0):
        MotorNum = str(MotorNum).encode('ascii')
        self.ser.write(msg.encode('ascii'))
        print(msg.encode('ascii'))
        
    def stop(self, MotorNum=0):
        if MotorNum == 0:
            self.write('S')
        else:
            self.write('S', MotorNum)
            
    def updateVelocity(self,_velocity,_Acceleration,_MotorNum):
        self.Velocity = _velocity
        self.Acceleration = _Acceleration
        self.write(msg='MV\n',MotorNum=_MotorNum)
        self.write(msg='A='+str(_Acceleration)+'\n',MotorNum=_MotorNum)
        self.write(msg='V='+str(_velocity)+'\n',MotorNum=_MotorNum)
        self.write(msg='G\n',MotorNum=_MotorNum)      