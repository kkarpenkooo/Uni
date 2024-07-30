using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter the coordinates of the vector:");
        string[] input = Console.ReadLine().Split();

        int x1 = int.Parse(input[0]);
        int y1 = int.Parse(input[1]);
        int x2 = int.Parse(input[2]);
        int y2 = int.Parse(input[3]);

        double length = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2));
        Console.WriteLine($"{length:F6}");
    }
}