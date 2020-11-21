# You are given a string S made of lowercase English alphabets.
# Find the length of the smallest substring with the maximum number of distinct characters.

def maxdchar(str, n):

    count = [0] * 256

    for i in range(n):
        count[ord(str[i])] += 1

    maxd = 0

    for i in range(256):
        if (count[i] != 0):
            maxd += 1

    return maxd

def smallestsubstr(str):

    n = len(str)
    maxdt = maxdchar(str, n)
    minl = n

    for i in range(n):
        for j in range(n):

            substr = str[i:j]
            subl = len(substr)
            subdchar = maxdchar(substr, subl)

            if ((subl < minl) and (subdchar == maxdt)):
                minl = subl

    return minl

if __name__ == "__main__":

    str=input()
    l = smallestsubstr(str);
    print(l)
