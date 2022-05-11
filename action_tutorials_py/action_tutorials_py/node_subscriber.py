from time import sleep

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from tutorial_interfaces.msg import Num

class Subscriber(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        #self.subscription  =  self.create_subscription(String, 'topic2',self.listener_callback,10)
        self.subscription  =  self.create_subscription(Num,'topic2',self.listener_callback,10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%i"' % msg.num)
        

def main(args=None):
    rclpy.init(args=args)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    #node.destroy_node()
    minimal_subscriber = Subscriber()
    rclpy.spin(minimal_subscriber)
    rclpy.shutdown()


if __name__ == '__main__':
    main()