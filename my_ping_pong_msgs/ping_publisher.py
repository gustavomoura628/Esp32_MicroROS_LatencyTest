import rclpy
from rclpy.node import Node
from my_ping_pong_msgs.msg import PingPong
import time

class PingPublisher(Node):
    def __init__(self):
        super().__init__('ping_publisher')
        self.publisher_ = self.create_publisher(PingPong, 'game_of_ping_pong', 10)
        self.subscription = self.create_subscription(
            PingPong,
            'game_of_ping_pong',
            self.listener_callback,
            10)
        self.subscription
        self.timer = self.create_timer(1.0, self.timer_callback)
    
    def timer_callback(self):
        msg = PingPong()
        msg.timestamp_sec = int(time.time_ns()//1_000_000_000)
        msg.timestamp_nsec = int(time.time_ns()%1_000_000_000)
        msg.status = 'ping'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.status} with timestamp {msg.timestamp_sec}')
    
    def listener_callback(self, msg):
        if msg.status == 'pong':
            self.get_logger().info(f'Received: {msg.status} with timestamp {msg.timestamp_sec}')

def main(args=None):
    rclpy.init(args=args)
    ping_publisher = PingPublisher()
    rclpy.spin(ping_publisher)
    ping_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

