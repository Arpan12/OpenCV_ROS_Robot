#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('robot_description')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import CVBridgeSub


class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = CVBridgeSub.imgmsg_to_cv2(data)
      #print(data)
      #cv_image = np.frombuffer(data, dtype=np.uint8).reshape(data.height, data.width, -1)
    except CvBridgeError as e:
      print(e)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    # try:
    #   self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    # except CvBridgeError as e:
    #   print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)