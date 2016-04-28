#!/usr/bin/env python  
import roslib; roslib.load_manifest('smart_motor')
import rospy, serial, tf.transformations, smartMotor
from geometry_msgs.msg import Twist

def callback(_twist):
    rospy.loginfo("Received a /cmd_vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"  % (_twist.linear.x, _twist.linear.y, _twist.linear.z))  
    rospy.loginfo("Angular Components: [%f, %f, %f]" % (_twist.angular.x, _twist.angular.y, _twist.angular.z))
    cmd_twist_x = _twist.linear.x
    cmd_twist_y = _twist.linear.y
    cmd_twist_r = _twist.angular.z
    
    if rospy.has_param("wheleDistance"):
        wheleDistance = rospy.get_param("wheleDistance")
        r = (2*cmd_twist_x) - (cmd_twist_r*wheleDistance) / (2*wheleDistance)
        right_whele_speed = (r+wheleDistance)*cmd_twist_r
        left_whele_speed  = r*cmd_twist_r
        rospy.loginfo("right_whele_speed: %f left_whele_speed:%f" % (right_whele_speed,left_whele_speed)) 
    else:
        rospy.logerr("Please input param 'wheleDistance'")
       
   
def main():
    rospy.init_node('SmartMotor_Controller')
    rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.spin()
    
    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
        