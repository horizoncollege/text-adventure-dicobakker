class terminal_input {
    string terminal_input = Console.ReadLine("Links, Rechts, Boven, Onder");
    if (terminal_input == "Links") {
        player.x = player.x - 1;
    } else if (terminal_input == "Rechts") {
        player.x = player.x + 1;
    } else if (terminal_input == "Boven") {
        player.y = player.y - 1;
    } else if (terminal_input == "Onder") {
        player.y = player.y + 1;
    }
    echo player.x;
}

Console.Writeline("test");
