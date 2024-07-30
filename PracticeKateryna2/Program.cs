using System;
using System.Linq;

class Program
{
    static void Main()
    {
        // Read the number of integers
        Console.WriteLine("Enter the number of integers:");
        int p = int.Parse(Console.ReadLine());

        // Read the integers
        Console.WriteLine("Enter the integers separated by spaces:");
        int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();

        // Calculate LCM of the numbers
        int lcm = numbers[0];
        for (int i = 1; i < numbers.Length; i++)
        {
            lcm = LCM(lcm, numbers[i]);
        }

        // Output the result
        Console.WriteLine($"The LCM of the given numbers is: {lcm}");
    }

    static int GCD(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    static int LCM(int a, int b)
    {
        return (a / GCD(a, b)) * b;
    }
}