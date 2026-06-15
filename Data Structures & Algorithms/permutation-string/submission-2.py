from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # This is the critical check I missed.
        # If s1 is longer, a permutation is impossible.
        if len(s1) > len(s2):
            return False

        # --- 1. Your s1 map logic (This was good) ---
        letters = defaultdict(int)
        for char in s1:
            letters[char] += 1
        
        # --- 2. Your pointer setup ---
        l, r = 0, len(s1) - 1
        
        # --- 3. Build the *first* window ---
        window_freq = defaultdict(int)
        for i in range(l, r + 1):
            window_freq[s2[i]] += 1

        # --- 4. Check the first window ---
        if window_freq == letters:
            return True

        # --- 5. Now, a simple loop to *slide* the window ---
        r += 1
        
        while r < len(s2):
            # A. ADD the new char
            window_freq[s2[r]] += 1
            
            # B. REMOVE the old char
            window_freq[s2[l]] -= 1
            if window_freq[s2[l]] == 0:
                del window_freq[s2[l]]

            # C. CHECK if the maps match
            if window_freq == letters:
                return True
            
            # D. SLIDE the pointers
            l += 1
            r += 1

        # If the loop finishes, we found no match
        return False