from time import sleep

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from tutorial_interfaces.msg import Num

class Publisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Num, 'topic2', 10)

    def publish_one_msg(self):
        #msg = String()
        msg = Num()
        i = 0
        #while rclpy.ok():
        #msg.data = 'Hello World: %d' % i
        msg.num = i 
        i += 1
        super().get_logger().info('Publishing: "%i"' % msg.num)
        self.publisher_.publish(msg)
        sleep(0.5)  # seconds

    def publish_multi_msg(self):
        msg = Num()
        i = 0
        while rclpy.ok():
            msg.num = i
            i += 1
            super().get_logger().info('Publishing: "%i"' % msg.num)
            self.publisher_.publish(msg)
            sleep(0.5)  # seconds
        

def main(args=None):
    rclpy.init(args=args)
    #create node in python WITHOUT CLASS and WITH CLASS
    """node = rclpy.create_node('publisher')

    publisher = node.create_publisher(String, 'topic', 10)

    msg = String()

    i = 0
    while rclpy.ok():
        msg.data = 'Hello World: %d' % i
        i += 1
        node.get_logger().info('Publishing: "%s"' % msg.data)
        publisher.publish(msg)
        sleep(0.5)  # seconds"""
    

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    #node.destroy_node()
    minimal_publisher = Publisher()
    minimal_publisher.publish_multi_msg()
    rclpy.shutdown()


if __name__ == '__main__':
    main()