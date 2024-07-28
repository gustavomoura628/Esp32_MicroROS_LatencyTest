import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
import time

class PingPublisher(Node):
    def __init__(self):
        super().__init__('ping_publisher')
        self.publisher_ = self.create_publisher(Header, '/microROS/ping', 10)
        self.timer = self.create_timer(1.0/30, self.timer_callback)
    
    def timer_callback(self):
        msg = Header()
        msg.stamp = self.get_clock().now().to_msg()
        msg.frame_id = 'ping_computer'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.frame_id} with timestamp {msg.stamp}')
    
def main(args=None):
    rclpy.init(args=args)
    ping_publisher = PingPublisher()
    rclpy.spin(ping_publisher)
    ping_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

