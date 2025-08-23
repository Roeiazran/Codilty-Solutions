
using System;

public class Program
{
    public static int Main()
    {
        int[] arr = { 0,0,1,1,1 };

        Console.WriteLine(MaxConsecutiveOnes(arr, 1));
        return 0;
    }

    /* 
        Problem: Given array of positive integers, find the shortest subarray with sum ≥ S.
        Idea: Expand right until sum ≥ S, then shrink from left to minimize length.
        Complexity: O(n).
    */
    public static int ShortestSubArray(int[] A, int S)
    {
        int n = A.Length;
        int left = 0, minLength = n + 1, sum = 0;

        for (int right = 0; right < n; right++) 
        {
            sum += A[right];

            while (sum >= S && left <= right) 
            {
                minLength = Math.Min(minLength, right - left + 1);
                sum -= A[left];
                left++;
            }
        }
        return (minLength <= n)? minLength : 0;
    }

    /*
        Problem: Given a string, find the longest substring with unique characters.
        Idea: Use a hashset/dictionary to track seen chars. Expand right, and if a duplicate appears, move left until it’s removed.
        Complexity: O(n).
    */
    public static int LongestSubStringWithoutRepitition (string S)
    {
        int left = 0, maxLength = 0, n = S.Length;
        HashSet<char> letters = new HashSet<char>();

        for (int right = 0; right < n; right++) 
        {
            while (letters.Contains(S[right]) && left <= right)
            {
                letters.Remove(S[left]);
                left++;
            }

            letters.Add(S[right]);
            maxLength = Math.Max(maxLength, right - left + 1);
        }

        return maxLength;
    }
    
    /*
        Problem: Count how many subarrays have sum less than K.
        Idea: Expand right, shrink left if sum ≥ K, and at each step count (right - left + 1) new subarrays.
        Complexity: O(n).
    */
    public static int CountSubArraySummedLessedThanK (int[] A, int K) 
    {
        int left = 0, sum = 0, count = 0, n = A.Length;

        for (int right = 0; right < n; right++)
        {
            sum += A[right];

            while (left <= right && sum > K) 
            {
                sum -= A[left];
                left++;
            }

            count += (right - left + 1);
        }

        return count;
    }

    /*
        Problem: Given a binary array, find the longest subarray containing only 1s after flipping at most K zeros.
        Idea: Count zeros in the window. If count > K, shrink from left.
        Complexity: O(n).
    */
    public static int MaxConsecutiveOnes (int[] A, int K)
    {
        int left = 0, maxLength = 0, n = A.Length, zeros = 0;

        for (int right = 0; right < n; right++)
        {
            if (A[right] == 0) zeros++;

            while (zeros > K)
            {
                if (A[left] == 0) zeros--;
                left++;
            }
            maxLength = Math.Max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    public static int MaxConsecutiveOnesV2 (int[] A, int K)
    {
        int left = 0, maxLength = 0, n = A.Length;

        for (int right = 0; right < n; right++)
        {
            if (A[right] == 0)
            {
                if (K == 0)
                {
                    while (A[left] != 0 && left <= right) left++;
                    left++;
                }
                else K--;
            }
            maxLength = Math.Max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    /*
        Problem: Given string s and pattern t, find the smallest substring in s that contains all chars of t.
        Idea: Expand right until all chars covered, then shrink from left to minimize.
        Complexity: O(n).
    */
    public static int SmallestWindowContainingAllCharacters(string s, string t)
    {
        Dictionary<char, int> dict = new Dictionary<char, int>();
        int n = s.Length, minLength = n + 1, covered = 0, left = 0;

        /* Build dictionary of required chars */
        foreach (char c in t) 
        {
            if(dict.ContainsKey(c)) dict[c] += 1;
            else dict[c] = 1;
        }

        covered = dict.Count;

        for (int right = 0; right < n; right++)
        {
            char r = s[right];
            if (!dict.ContainsKey(r)) continue;

            dict[r] -= 1;
            if (dict[r] == 0) covered -= 1;

            if (covered == 0) 
            {
                char l = s[left];

                while (left <= right)
                {
                    if (! dict.ContainsKey(l))
                    {
                        left++;
                        continue;
                    }

                    if (dict[l] < 0)
                    {
                        dict[l] += 1;
                        left++;
                    }
                    else break;
                }
            }
            minLength = Math.Min(minLength, right - left + 1);
        }

        return minLength <= n ? minLength : 0;
    }

}

