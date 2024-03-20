import json

# Define constants for map dimensions
MAP_WIDTH = 15
MAP_HEIGHT = 15

# Function to generate a map with base ground "flat land"
def generate_flat_land_map():
    flat_land_map = [[{"type": "flat_land", "hight": 0, "thickness": 0, "position": [x + 1, y + 1]} for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
    return flat_land_map

# Function to generate a map with forests at specific locations
def generate_forrest_map(flat_land_map):
    forest_map = [row[:] for row in flat_land_map]  # Create a copy of the platland map

    # Define specific locations for forests
    forest_locations = [
        [(1, 9), (2, 9), (3, 9)],
        [(1, 10), (2, 10), (3, 10), (4, 10)],
        [(1, 11), (2, 11), (3, 11), (4, 11), (5, 11)],
        [(1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)],
        [(1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (6, 13), (7, 13)],
        [(1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14)],
        [(1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15)]
    ]

    # Place forests at specific locations
    for row in forest_locations:
        for x, y in row:
            forest_map[y - 1][x - 1] = {"type": "forest", "hight": 0, "thickness": 1, "position": [x, y]}

    return forest_map

def generate_zee_map():
    zee_map = [[{"type": "zee", "hight": -1, "thickness": 0, "position": [x + 1, y + 1]} for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
    return zee_map

# Function to overwrite values on a map
def overwrite_values(original_map, overwrite_map):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            original_map[y][x].update(overwrite_map[y][x])
    return original_map

def main():
    # Generate platland map
    base_map = generate_flat_land_map()

    # Generate bos map at specific locations on top of platland
    forest_map = generate_forrest_map(base_map)

    # Save final map as JSON
    with open("map.json", "w") as json_file:
        json.dump(forest_map, json_file, indent=4)

if __name__ == "__main__":
    main()
