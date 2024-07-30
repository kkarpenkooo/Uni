using System;
using System.Text;

class Program
{
    static void Main()
    {
        Console.OutputEncoding = UTF8Encoding.UTF8;
        Console.WriteLine("Введіть довжину послідовності n:");
        int n = int.Parse(Console.ReadLine());

        if (n == 1)
        {
            Console.WriteLine("2");
            return;
        }
        if (n == 2)
        {
            Console.WriteLine("4");
            return;
        }

        const int MOD = 12345;
        int[,] dp = new int[n + 1, 3];

        // Initial conditions
        dp[1, 0] = 1; // "0"
        dp[1, 1] = 1; // "1"
        dp[1, 2] = 0; // No sequence "11" of length 1

        for (int i = 2; i <= n; i++)
        {
            dp[i, 0] = (dp[i - 1, 0] + dp[i - 1, 1] + dp[i - 1, 2]) % MOD;
            dp[i, 1] = dp[i - 1, 0];
            dp[i, 2] = dp[i - 1, 1];
        }

        int result = (dp[n, 0] + dp[n, 1] + dp[n, 2]) % MOD;
        Console.WriteLine($"Кількість шуканих послідовностей: {result}");
    }
}