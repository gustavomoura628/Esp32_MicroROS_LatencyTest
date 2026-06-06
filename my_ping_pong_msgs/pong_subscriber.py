import rclpy
from rclpy.node import Node
from my_ping_pong_msgs.msg import PingPong
import time

class PongSubscriber(Node):
    def __init__(self):
        super().__init__('pong_subscriber')
        self.publisher_ = self.create_publisher(PingPong, 'game_of_ping_pong', 10)
        self.subscription = self.create_subscription(
            PingPong,
            'game_of_ping_pong',
            self.listener_callback,
            10)
        self.subscription
    
    def listener_callback(self, msg):
        if msg.status == 'ping':
            self.get_logger().info(f'Received: {msg.status} with timestamp {msg.timestamp_sec}')
            response_msg = PingPong()
            response_msg.timestamp_sec = int(time.time_ns()//1_000_000_000)
            response_msg.timestamp_nsec = int(time.time_ns()%1_000_000_000)
            response_msg.status = 'pong'
            self.publisher_.publish(response_msg)
            self.get_logger().info(f'Publishing: {response_msg.status} with timestamp {response_msg.timestamp_sec}')

def main(args=None):
    rclpy.init(args=args)
    pong_subscriber = PongSubscriber()
    rclpy.spin(pong_subscriber)
    pong_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

