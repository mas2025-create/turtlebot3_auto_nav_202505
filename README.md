# turtlebot3_auto_nav

Turtlebot3 が Gazebo 上の障害物を避けながらマップ内を自動巡回する ROS 2 パッケージです。

# 動作環境

- Ubuntu 22.04
- ROS 2 humbl
- Gazebo 11
- turtlebot3_simulations
- Navigation2

# セットアップ手順
### 環境変数の設定（Turtlebot3 Burger の使用を前提としたシミュレーション）
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
source ~/.bashrc

### ROS2 ワークスペース作成
mkdir -p ~/turtlebot_ws/src
cd ~/turtlebot_ws/src

### turtlebot3 パッケージのクローン
git clone -b humble-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone -b humble-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git

### 本パッケージを配置
git clone https://github.com/mas2025-create/turtlebot3_auto_nav_202505.git

### ビルド
cd ~/turtlebot_ws
source /opt/ros/humble/setup.bash
colcon build


# 実行方法
### 1つ目のターミナル ( gazebo起動 )
source ~/turtlebot_ws/install/setup.bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

### 2つ目のターミナル ( Navigation2 起動 )
source ~/turtlebot_ws/install/setup.bash
cd ~/turtlebot_ws/src/turtlebot3_auto_nav
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=maps/my_map.yaml

### 3つ目のターミナル ( 自動走行制御プログラム )
source ~/turtlebot_ws/install/setup.bash
ros2 run turtlebot3_auto_nav navigator





