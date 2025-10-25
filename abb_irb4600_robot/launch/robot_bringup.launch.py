from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import (
    LaunchConfiguration,
    PathJoinSubstitution,
    Command,
    FindExecutable,
)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot_controllers = PathJoinSubstitution(
        [FindPackageShare("abb_irb4600_robot"), "config", "ros_controllers.yaml"]
    )

    initial_positions_file = PathJoinSubstitution(
        [FindPackageShare("abb_irb4600_description"), "config", "initial_positions.yaml"]
    )

    default_rviz_config = PathJoinSubstitution(
        [FindPackageShare("abb_irb4600_robot"), "rviz", "abb_irb4600_robot.rviz"]
    )

    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "prefix",
            default_value="",
            description="The prefix appended to URDF",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "controller",
            default_value="joint_trajectory_controller",
            description="Which controller should be started?",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "controller_config",
            default_value=robot_controllers,
            description="Path to the configuration file for ros2_control"
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "initial_positions_file",
            default_value=initial_positions_file,
            description="Path to the initial positions configuration"
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_mock_hardware",
            default_value="true",
            description="Should mock (simulated) hardware be used?",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rws_ip",
            default_value="None",
            description="IP of RWS computer. \
            Used only if 'use_fake_hardware' parameter is false.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rws_port",
            default_value="80",
            description="Port at which RWS can be found. \
            Used only if 'use_fake_hardware' parameter is false.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "configure_via_rws",
            default_value="true",
            description="If false, the robot description will be generated from \
            joint information in the ros2_control xacro. \
            Used only if 'use_fake_hardware' parameter is false.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz",
            default_value="true",
            description="Should RViz be launched",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz_config_file",
            default_value=default_rviz_config,
            description="The configuration file to use for RViz",
        )
    )

    prefix = LaunchConfiguration("prefix")
    controller = LaunchConfiguration("controller")
    controller_config = LaunchConfiguration("controller_config")
    initial_positions_file = LaunchConfiguration("initial_positions_file")
    use_mock_hardware = LaunchConfiguration("use_mock_hardware")
    rws_ip = LaunchConfiguration("rws_ip")
    rws_port = LaunchConfiguration("rws_port")
    configure_via_rws = LaunchConfiguration("configure_via_rws")
    rviz = LaunchConfiguration("rviz")
    rviz_config_file = LaunchConfiguration("rviz_config_file")

    robot_description = Command([
        PathJoinSubstitution([FindExecutable(name="xacro")]),
        " ",
        PathJoinSubstitution(
            [FindPackageShare("abb_irb4600_description"), "urdf", "abb_irb4600_40_255.xacro"]
        ),
        " prefix:=", prefix,
        " initial_positions_file:=", initial_positions_file,
        " use_mock_hardware:=", use_mock_hardware,
        " rws_ip:=", rws_ip,
        " rws_port:=", rws_port,
        " configure_via_rws:=", configure_via_rws,

    ])

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[
            {"robot_description": robot_description},
            controller_config,
        ],
        output="both",
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description}],
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager", "controller_manager",
        ],
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[controller, "--controller-manager", "controller_manager"],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_file],
        condition=IfCondition(rviz),
    )

    nodes = [
        control_node,
        robot_state_publisher_node,
        joint_state_broadcaster_spawner,
        robot_controller_spawner,
        rviz_node
    ]

    return LaunchDescription(declared_arguments + nodes)
