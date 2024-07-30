using System;
using System.Text;

class Program
{
    static void Main()
    {
        // Input: t1, t2, t3 - the times each guest takes to eat the pie individually
        Console.OutputEncoding = UTF8Encoding.UTF8;
        Console.WriteLine("Введіть три значення:");
        string[] input = Console.ReadLine().Split();
        double t1 = double.Parse(input[0]);
        double t2 = double.Parse(input[1]);
        double t3 = double.Parse(input[2]);

        // Calculate the combined rate of eating
        double combinedRate = 1 / t1 + 1 / t2 + 1 / t3;

        // Time required for guests to eat the pie together
        double timeToEat = 1 / combinedRate;

        // Output the time, rounded to 2 decimal places
        Console.WriteLine($"Час, необхідний для з'їдання пирога: {timeToEat:F2} годин");
    }
}