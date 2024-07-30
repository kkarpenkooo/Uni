using System;
using System.Text;

class Program
{
    static void Main()
    {
        Console.OutputEncoding = UTF8Encoding.UTF8;
        Console.WriteLine("Введіть натуральне число n:");
        int n = int.Parse(Console.ReadLine());
        int count = 0;

        for (int q = 1; q < n; q++)
        {
            if ((n - q) % (q + 1) == 0)
            {
                int m = (n - q) / (q + 1);
                if (m > 0)
                {
                    count++;
                }
            }
        }

        Console.WriteLine($"Кількість рівних дільників числа {n}: {count}");
    }
}