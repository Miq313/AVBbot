import math
from datetime import datetime
import json

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "utils"))
from mapping_classes import Point, Line, showPlot

# Reading environment type from config file
config_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.json")
with open(config_file_path, "r") as config_file:
    config = json.load(config_file)
    environment = config["environment"]
    room_name = config["current_room"]
    if environment == "development":
        need_plot = True
    else:
        need_plot = False

# Read wall data from CSV file
data_folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
map_walls_file = os.path.join(data_folder_path, f"map_walls__{room_name}.csv")
with open(map_walls_file, "r") as map_walls_file:
    next(map_walls_file) # Skip header line
    wall_lines = []
    for row in map_walls_file:
        row = row.split(",")
        wall_lines.append(
            Line(
                Point(
                    float(row[0]),
                    float(row[1])
                ),Point(
                    float(row[2]),
                    float(row[3])
                )
            )
        )

# Read grid data from CSV file
map_gridpoints_file = os.path.join(data_folder_path, f"map_gridpoints__{room_name}.csv")
with open(map_gridpoints_file, "r") as map_gridpoints_file:
    next(map_gridpoints_file) # Skip header line
    gridpoints = []
    for row in map_gridpoints_file:
        row = row.split(",")
        gridpoints.append(
            Point(
                float(row[0]),
                float(row[1])
            )
        )

# Plot everything for visualization purposes
if need_plot:
    for wallLine in wall_lines:
        wallLine.plot("g", 2)
    for gridpoint in gridpoints:
        gridpoint.plot("b")

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

# Navigation algorithm
def navigate(nav_point_A, nav_point_B):
    if need_plot:
        nav_point_A.plot("r")
        nav_point_B.plot("r")
    # time1 = datetime.now()
    last_points = [nav_point_A]
    nav_paths = []
    segment_count = 0
    graph = {nav_point_A:[]}
    while len(nav_paths) == 0:
        segment_count += 1
        # Try to connect every last point to final destination (nav_point_B)
        for last_point in last_points:
            proposed_line = Line(last_point, nav_point_B)
            if proposed_line.intersectsWall(wall_lines) == False:
                nav_paths.append(proposed_line)
                graph[last_point] = [nav_point_B]
                if need_plot:
                    proposed_line.plot("green")
        # Try to connect every last point to every (unused) gridpoint
        last_points_old = last_points
        last_points = []
        if len(nav_paths) == 0:
            for last_point in last_points_old:
                proposed_lines = last_point.connectToGrid(gridpoints, wall_lines, omittedPoints=last_points_old)
                for proposed_line in proposed_lines:
                    last_points.append(proposed_line.p2)
                    graph[last_point] = last_points
                    if need_plot:
                        if segment_count == 1:
                            proposed_line.plot("blue")
                        elif segment_count == 2:
                            proposed_line.plot("orange")
                        elif segment_count == 3:
                            segment_count.plot("purple")
                        elif segment_count == 4:
                            proposed_line.plot("grey")
        print(segment_count)

    # delta = datetime.now() - time1
    # print(delta.seconds)

    finPath = find_path(graph, nav_point_A, nav_point_B)
    for index in range(len(finPath)-1):
        x = Line(finPath[index],finPath[index+1])
        if need_plot:
            x.plot("b")
    print(x)

if __name__ == "__main__":
    nav_point_A = Point(1120,414)
    nav_point_B = Point(596,936)
    navigate(nav_point_A, nav_point_B)
    if need_plot:
        showPlot()