class game
{
    public static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}

// ----------------------------------------------------------------------------------------------------------------------------------------------------------------
using System;
using System.IO;
using Newtonsoft.Json;

class Program
{
    static void Main()
    {
        // Step 1: Read the JSON data from the file
        string jsonFilePath = "map.json";
        string jsonText = File.ReadAllText(jsonFilePath);

        // Step 2: Parse the JSON into an array of objects
        var mapData = JsonConvert.DeserializeObject<MapItem[]>(jsonText);

        // Define the size of the map
        int mapWidth = 15;
        int mapHeight = 15;

        // Step 3: Generate the map array and fill it with data from the JSON
        int[,] mapArray = new int[mapHeight, mapWidth];
        foreach (var item in mapData)
        {
            int xPos = item.Position[0];
            int yPos = item.Position[1];
            int height = item.Height;

            // Set the height at the correct position in the map array
            mapArray[yPos, xPos] = height;
        }

        // Now you have the map data in the mapArray, which you can further use
        // for example, for rendering a visual map or for other processing.

        // Example: print the map data to the console
        for (int y = 0; y < mapHeight; y++)
        {
            for (int x = 0; x < mapWidth; x++)
            {
                Console.Write(mapArray[y, x] + " ");
            }
            Console.WriteLine();
        }
    }
}

// Define a class to represent the structure of the JSON items
public class MapItem
{
    public int Height { get; set; }
    public int[] Position { get; set; }
}


// ----------------------------------------------------------------------------------------------------------------------------------------------------------------












class player
{
//hier moet de x en y coordienaten van de speler
}
class inventory
{

}

class items
{

}
