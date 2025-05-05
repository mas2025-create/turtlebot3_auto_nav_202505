# turtlebot_auto_nav/navigator.py

import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseStamped
import time

class AutoNavigator(Node):
    def __init__(self):
        super().__init__('auto_navigator')
        self.navigator = BasicNavigator()

        self.declare_parameter('goal_loop_rate', 10.0)
        self.loop_rate = self.get_parameter('goal_loop_rate').get_parameter_value().double_value

        self.goals = [
            self.make_pose(1.0, 0.0, 0.0),
            self.make_pose(1.0, 1.0, 1.57),
            self.make_pose(0.0, 1.0, 3.14),
            self.make_pose(0.0, 0.0, -1.57)
        ]
        self.current_goal_idx = 0
        self.timer = self.create_timer(1.0 / self.loop_rate, self.send_next_goal)

    def make_pose(self, x, y, yaw):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        import tf_transformations
        q = tf_transformations.quaternion_from_euler(0, 0, yaw)
        pose.pose.orientation.x = q[0]
        pose.pose.orientation.y = q[1]
        pose.pose.orientation.z = q[2]
        pose.pose.orientation.w = q[3]
        return pose

    def send_next_goal(self):
        if not self.navigator.isTaskComplete():
            return

        self.get_logger().info(f"Sending goal {self.current_goal_idx + 1}")
        self.navigator.goToPose(self.goals[self.current_goal_idx])
        self.current_goal_idx = (self.current_goal_idx + 1) % len(self.goals)

def main(args=None):
    rclpy.init(args=args)
    node = AutoNavigator()

    node.navigator.waitUntilNav2Active()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

