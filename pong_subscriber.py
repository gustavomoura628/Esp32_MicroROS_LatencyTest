import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from rclpy.qos import QoSProfile, ReliabilityPolicy
import time

class PongSubscriber(Node):
    def __init__(self):
        super().__init__('pong_subscriber')
        qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,depth=1)
        self.subscription = self.create_subscription(
            Header,
            '/microROS/pong',
            self.listener_callback,
            qos_profile)
        self.subscription
    
    def listener_callback(self, msg):
        current_stamp = self.get_clock().now().to_msg()
        self.get_logger().info(f'Received: {msg.frame_id} with timestamp {msg.stamp}')
        difference_in_nanoseconds = (current_stamp.sec - msg.stamp.sec)*1000000000 + current_stamp.nanosec - msg.stamp.nanosec
        difference_in_milliseconds = difference_in_nanoseconds/1000000.0
        self.get_logger().info(f'Time difference = {difference_in_milliseconds} milliseconds')

def main(args=None):
    rclpy.init(args=args)
    pong_subscriber = PongSubscriber()
    rclpy.spin(pong_subscriber)
    pong_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

