using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter the number of digits:");
        int p = int.Parse(Console.ReadLine());

        if (p == 1)
        {
            Console.WriteLine("2");
            return;
        }

        long[,] dp = new long[p + 1, 4];

        // Base cases
        dp[1, 0] = 1; // Single '5'
        dp[1, 2] = 1; // Single '9'

        for (int i = 2; i <= p; i++)
        {
            dp[i, 0] = dp[i - 1, 2] + dp[i - 1, 3];
            dp[i, 1] = dp[i - 1, 0];
            dp[i, 2] = dp[i - 1, 0] + dp[i - 1, 1];
            dp[i, 3] = dp[i - 1, 2];
        }

        long result = dp[p, 0] + dp[p, 1] + dp[p, 2] + dp[p, 3];
        Console.WriteLine($"Number of valid numbers with {p} digits: {result}");
    }
}