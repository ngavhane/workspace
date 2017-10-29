"""
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12







Number of comparisons in worst case is O(m*(n-m+1)). Although strings which have repeated characters are not
 likely to appear in English text, they may well occur in other applications (for example, in binary texts).
 The KMP matching algorithm improves the worst case to O(n). We will be covering KMP in the next post.
 Also, we will be writing more posts to cover all pattern searching algorithms and data structures
"""


# Python program for Naive Pattern Searching
def search(pat, txt):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one
    for i in xrange(N-M+1):

        # For current index i, check for pattern match
        for j in xrange(M):
            if txt[i+j] != pat[j]:
                break
        if j == M-1: # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print "Pattern found at index " + str(i)

# Driver program to test the above function
txt = "AABAACAADAABAAABAA"
pat = "AABA"
search (pat, txt)