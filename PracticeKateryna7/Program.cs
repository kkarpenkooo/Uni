using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter the coordinates and radii of the two circles:");
        string[] input = Console.ReadLine().Split();

        double x1 = double.Parse(input[0]);
        double y1 = double.Parse(input[1]);
        double r1 = double.Parse(input[2]);
        double x2 = double.Parse(input[3]);
        double y2 = double.Parse(input[4]);
        double r2 = double.Parse(input[5]);

        double distance = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2));

        if (distance == 0 && r1 == r2)
        {
            Console.WriteLine("-1"); // Infinite intersection points (coincident circles)
        }
        else if (distance == r1 + r2 || distance == Math.Abs(r1 - r2))
        {
            Console.WriteLine("1"); // Tangent circles (one point of intersection)
        }
        else if (distance < r1 + r2 && distance > Math.Abs(r1 - r2))
        {
            Console.WriteLine("2"); // Two points of intersection
        }
        else
        {
            Console.WriteLine("0"); // No intersection
        }
    }
}