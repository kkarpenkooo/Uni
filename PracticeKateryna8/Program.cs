using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static void Main()
    {
        Console.OutputEncoding = UTF8Encoding.UTF8;
        Console.WriteLine("Введіть слово:");
        string word = Console.ReadLine();
        word = word.ToLower(); // Case insensitive
        Dictionary<char, int> letterCounts = new Dictionary<char, int>();

        // Count occurrences of each letter
        foreach (char c in word)
        {
            if (letterCounts.ContainsKey(c))
            {
                letterCounts[c]++;
            }
            else
            {
                letterCounts[c] = 1;
            }
        }

        // Calculate the factorial of a number
        long Factorial(int n)
        {
            long result = 1;
            for (int i = 2; i <= n; i++)
            {
                result *= i;
            }
            return result;
        }

        // Total length of the word
        int n = word.Length;
        long totalAnagrams = Factorial(n);

        // Divide by the factorial of counts of each letter
        foreach (var count in letterCounts.Values)
        {
            totalAnagrams /= Factorial(count);
        }

        Console.WriteLine($"Кількість анаграм: {totalAnagrams}");
    }
}