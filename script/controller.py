#!/usr/bin/env python
import roslib; roslib.load_manifest('smart_motor')
import rospy, serial, smartMotor
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('SmartMotor_Controller')
    rospy.Subscriber('/cmd_vel', Twist, callback)

    # setup the SmartMotor
    m = smartMotor.SmartMotor('/dev/ttyUSB0',9600)
    m.setupSerialConnection()

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
            #calculate speed
            right_whele_speed = ( (2*cmd_twist_x) + (wheleDistance*cmd_twist_r) ) / (2*wheleRadius)
            left_whele_speed  = ( (2*cmd_twist_x) - (wheleDistance*cmd_twist_r) ) / (2*wheleRadius)
            #log the speed
            rospy.loginfo("right_whele_speed: %f left_whele_speed:%f r:%f" % (right_whele_speed,left_whele_speed,r))
            #deliver the speed to Motor
            m.updateVelocity(_MotorNum= 1,_Acceleration= 1000,_velocity= right_whele_speed)
            m.updateVelocity(_MotorNum= 2,_Acceleration= 1000,_velocity= left_whele_speed)
        else:
            rospy.logerr("Please input param 'wheleDistance' or 'wheleRadius'")


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
