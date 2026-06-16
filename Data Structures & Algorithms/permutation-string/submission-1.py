from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # --- 1. Your s1 map logic (This was good) ---
        # I've made it slightly cleaner using .get()
        letters = defaultdict(int)
        for char in s1:
            letters[char] += 1
        
        # --- 2. Your pointer setup (This was also good) ---
        l, r = 0, len(s1) - 1
        
        # This is the main logical fix.
        # We must build the *first* window *before* we start sliding.
        window_freq = defaultdict(int)
        for i in range(l, r + 1):
            window_freq[s2[i]] += 1

        # --- 3. Check the first window ---
        if window_freq == letters:
            return True

        # --- 4. Now, a simple loop to *slide* the window ---
        # The loop's only job is to Add, Remove, Check, and Slide.
        
        # We move r one step to prepare for the loop
        r += 1
        
        while r < len(s2):
            # A. ADD the new char that just entered the window
            window_freq[s2[r]] += 1
            
            # B. REMOVE the old char that just left the window
            window_freq[s2[l]] -= 1
            if window_freq[s2[l]] == 0:
                del window_freq[s2[l]]

            # C. CHECK if the maps match
            if window_freq == letters:
                return True
            
            # D. SLIDE the pointers for the next iteration
            l += 1
            r += 1

        # If the loop finishes, we found no match
        return False