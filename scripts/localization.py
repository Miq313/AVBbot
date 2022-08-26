import os, json
import math

# Initializing robot's parameters
config_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.json")
with open(config_file_path, "r") as config_file:
    config = json.load(config_file)
    wheel_diameter = float(config["hardware"]["wheelDiameter"]) #mm
    step_angle = math.radians(float(config["hardware"]["stepAngle"])) #rads
    axel_length = float(config["hardware"]["axelLength"]) #mm

# Calculating other robot parameters
wheel_radius = wheel_diameter/2
step_distance = step_angle*wheel_radius
axel_radius = axel_length/2

# Reset position in the JSON file
def reset_cur_pos(x=0.0, y=0.0, dir=90.0):
    cur_pos = {
        "position": {
            "x": x,
            "y": y
        },
        "direction": dir
        }
    data_folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
    cur_pos_file_path = os.path.join(data_folder_path, "current_position.json")
    with open(cur_pos_file_path, "w") as cur_pos_file:
        cur_pos_file.write(json.dumps(cur_pos, indent = 4))

def update_cur_pos(movement):
    # Parsing movement data revceived from Pico
    movement = movement.split(":")
    trav_dir = str(movement[0])
    trav_dist = float(movement[1])

    # Reading current position from JSON
    data_folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
    cur_pos_file_path = os.path.join(data_folder_path, "current_position.json")
    with open(cur_pos_file_path, "r") as cur_pos_file:
        cur_pos = json.load(cur_pos_file)
        cur_pos["direction"] = float(cur_pos["direction"])
        cur_pos["position"]["x"] = float(cur_pos["position"]["x"])
        cur_pos["position"]["y"] = float(cur_pos["position"]["y"])

    # Calculating change in position
    if trav_dir == "F" or trav_dir == "B":
        delta_x = math.cos(math.radians(cur_pos["direction"]))*trav_dist*step_distance
        delta_y = math.sin(math.radians(cur_pos["direction"]))*trav_dist*step_distance
        if trav_dir == "B":
            delta_x = -delta_x
            delta_y = -delta_y
        # Updating new position
        cur_pos["position"]["x"] += delta_x
        cur_pos["position"]["y"] += delta_y
    elif trav_dir == "R" or trav_dir == "L":
        deltaDir = math.degrees(math.atan(trav_dist/axel_radius))
        if trav_dir == "L":
            deltaDir = -deltaDir
        # Updating new position    
        cur_pos["direction"] += deltaDir

    # Saving new position to JSON
    with open(cur_pos_file_path, "w") as cur_pos_file:
        cur_pos_file.write(json.dumps(cur_pos, indent = 4))

if __name__ == "__main__":
    reset_cur_pos()