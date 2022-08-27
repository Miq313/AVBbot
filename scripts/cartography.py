import json
import math

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "utils"))
from mapping_classes import Point, Line, showPlot

# Reading environment type from config file
config_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.json")
with open(config_file_path, "r") as config_file:
    config = json.load(config_file)
    environment = config["environment"]
    if environment == "development":
        need_plot = True
    else:
        need_plot = False

def create_map(room_name):
    # Spatial data input, read from csv
    data_folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
    spatial_data_file = os.path.join(data_folder_path, f"spatial_data__{room_name}.csv")
    with open(spatial_data_file, "r") as file:
        next(file) # skip header
        spatial_lines = []
        wall_points =[]
        for row in file:
            row = row.split(",")
            spatial_lines.append(
                Line(
                    Point(
                        float(row[0]),
                        float(row[1])
                    ),
                    Point(
                        float(row[2]),
                        float(row[3])
                    )
                )
            )
            wall_points.append(
                Point(
                    float(row[2]),
                    float(row[3])
                )
            )


    # Plot spatial_lines for visualization purposes
    if need_plot:
        for spatial_line in spatial_lines:
            spatial_line.plot(color='black')

    # Creating wall parameters by connecting all wallpoints with each other and checking which don't intersect with spatial_lines
    wall_lines = []
    for wall_point in wall_points:
        for wall_point_connecting in wall_points:
            if wall_point != wall_point_connecting:
                proposed_wall_line = Line(wall_point,wall_point_connecting)
                is_wall_line = True
                for spatial_line in spatial_lines:
                    if len(set([proposed_wall_line.p1, proposed_wall_line.p2, spatial_line.p1, spatial_line.p2])) == 4 and proposed_wall_line.intersects(spatial_line): # If intersects, but not including when "intersects" by the two lines sharing an endpoint
                        is_wall_line = False
                        if need_plot:
                            proposed_wall_line.plot(color='r', linewidth=0.5) # Plot failed wall line in red
                if is_wall_line:
                    wall_lines.append(proposed_wall_line)
                    if need_plot:
                        proposed_wall_line.plot(color='g', linewidth=2) # Plot successful wall line in green


    # Finding extrema points to create grid
    x_max = x_min = wall_lines[0].p1.x
    y_max = y_min = wall_lines[0].p1.y
    for wall_line in wall_lines:
        x_max = max([wall_line.p1.x,wall_line.p2.x,x_max])
        x_min = min([wall_line.p1.x,wall_line.p2.x,x_min])
        y_max = max([wall_line.p1.y,wall_line.p2.y,y_max])
        y_min = min([wall_line.p1.y,wall_line.p2.y,y_min])

    # Calculating grid parameters based on config file
    config_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.json")
    with open(config_file_path, "r") as config_file:
        config = json.load(config_file)
        wall_buffer = float(config["hardware"]["maxChassisRadius"])*1.5 #cm
    interval_x = interval_y = 20
    num_x_points = int((math.ceil(x_max) - math.floor(x_min))/interval_x)
    num_y_points = int((math.ceil(y_max) - math.floor(y_min))/interval_y)

    # Creating grid
    grid_points = []
    for x_points in range(0,num_x_points+1):
        for y_points in range(0,num_y_points+1):
            x_point = math.floor(x_min)+interval_x*x_points
            y_point = math.floor(y_min)+interval_y*y_points
            grid_point = Point(x_point, y_point)
            for wall_line in wall_lines:
                if grid_point.distanceToLine(wall_line) < wall_buffer:
                    grid_points.append(grid_point)
                    if need_plot:
                        grid_point.plot("y") # Plot successful grid point in yellow
                    break


    # Saving final map to CSV file
    data_folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
    map_walls_file = os.path.join(data_folder_path, f"map_walls__{room_name}.csv")
    with open(map_walls_file, "w") as file:
        file.write("x1,y1,x2,y2\n")
        for wall_line in wall_lines:
            file.write(str(wall_line.p1.x)+","+str(wall_line.p1.y)+","+str(wall_line.p2.x)+","+str(wall_line.p2.y)+"\n")

    map_gridpoints_file = os.path.join(data_folder_path, f"map_gridpoints__{room_name}.csv")
    with open(map_gridpoints_file, "w") as file:
        file.write("x,y\n")
        for grid_point in grid_points:
            file.write(str(grid_point.x)+","+str(grid_point.y)+"\n")

    if need_plot:
        showPlot()

if __name__=="__main__":
    create_map("room_1")