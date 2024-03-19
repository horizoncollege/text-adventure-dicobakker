import json
import random

# Define constants for map dimensions
MAP_WIDTH = 15
MAP_HEIGHT = 15

# Function to generate a map with base ground "PLATLAND"
def generate_platland_map():
    platland_map = [[{"hoogte": 0, "positie": [x + 1, y + 1]} for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
    return platland_map

# Function to overwrite values on a map
def overwrite_values(original_map, overwrite_map):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            original_map[y][x].update(overwrite_map[y][x])
    return original_map

# Main function to generate and save the map as JSON
def main():
    # Generate base map with "PLATLAND"
    base_map = generate_platland_map()

    # Save final map as JSON
    with open("map.json", "w") as json_file:
        json.dump(base_map, json_file, indent=4)

if __name__ == "__main__":
    main()
