using System;

class Program
{
    static void Main()
    {
        // Input reading
        Console.WriteLine("Enter values for x and y:");
        int x = int.Parse(Console.ReadLine());
        int y = int.Parse(Console.ReadLine());

        // Calculate the minimum number of steps
        int steps = MinimumSteps(x, y);
        Console.WriteLine($"Minimum number of steps from {x} to {y}: {steps}");
    }

    static int MinimumSteps(int x, int y)
    {
        int distance = y - x;
        int stepLength = 1;
        int totalSteps = 0;

        while (distance > 0)
        {
            totalSteps++;
            distance -= stepLength;

            // Increase stepLength if the remaining distance allows it
            if (distance >= stepLength + 1)
            {
                stepLength++;
            }
        }

        return totalSteps;
    }
}