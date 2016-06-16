 #!/usr/bin/env python
import roslib; roslib.load_manifest('smart_motor')
import rospy, serial, smartMotor, math
from geometry_msgs.msg import Twist

m = smartMotor.SmartMotor('/dev/ttyUSB1',9600)
m.setupSerialConnection()

def main():
    rospy.init_node('SmartMotor_Controller')
    rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.spin()

def callback(_twist):
    rospy.loginfo("Received a /cmd_vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"  % (_twist.linear.x, _twist.linear.y, _twist.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]" % (_twist.angular.x, _twist.angular.y, _twist.angular.z))
    cmd_twist_x = _twist.linear.x
    cmd_twist_r = _twist.angular.z

    if rospy.has_param("wheleDistance") and rospy.has_param("wheleRadius"):
        #get params
        wheleDistance = rospy.get_param("wheleDistance")
        wheleRadius = rospy.get_param("wheleRadius")
        #calculate speed (rad/s)
        right_whele_speed = ( (2*cmd_twist_x) + (wheleDistance*cmd_twist_r) ) / (2*wheleRadius)
        left_whele_speed  = ( (2*cmd_twist_x) - (wheleDistance*cmd_twist_r) ) / (2*wheleRadius)
        #make speed (rad/s) to speed (rps)
        right_whele_speed = right_whele_speed / (2*math.pi)
        left_whele_speed = left_whele_speed / (2*math.pi)
        #log the speed
        rospy.loginfo("right_whele_speed: %f left_whele_speed:%f r:%f" % (right_whele_speed,left_whele_speed,wheleRadius))
        #deliver the speed to Motor (1 rps = 60 rpm = 32768)
        m.updateVelocity(_MotorNum= 129,_Acceleration= 1000,_velocity= int(right_whele_speed * 32768))
        m.updateVelocity(_MotorNum= 130,_Acceleration= 1000,_velocity= int(left_whele_speed * 32768) * -1)
    else:
        rospy.logerr("Please input param 'wheleDistance' or 'wheleRadius'")


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
