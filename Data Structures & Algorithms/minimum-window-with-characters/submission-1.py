# YOU DID THIS YOURSELF !!

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        # Create the frequency map for the target string 't'
        goal = defaultdict(int)
        for char in t:
            goal[char] += 1
        
        # 'have' tracks how many char counts we've matched
        # 'need' is the total number of unique chars we must match
        have, need = 0, len(goal)
        
        # (length, left_index, right_index)
        res = (float("inf"), 0, 0)
        
        window_counts = defaultdict(int)
        l = 0
        
        # EXPAND 'r'
        for r in range(len(s)):
            char_r = s[r]
            
            # Add the new char to the window's count
            window_counts[char_r] += 1
            
            # Check if this char just met our requirement
            if char_r in goal and window_counts[char_r] == goal[char_r]:
                have += 1
            
            # CONTRACT 'l'
            # As long as the window is valid, try to shrink it
            while have == need:
                current_len = r - l + 1
                
                # Check if this is a new shortest window
                if current_len < res[0]:
                    res = (current_len, l, r)
                
                # Remove the leftmost char from the window
                char_l = s[l]
                window_counts[char_l] -= 1
                
                # Check if removing this char broke the requirement
                if char_l in goal and window_counts[char_l] < goal[char_l]:
                    have -= 1
                
                # Move the left pointer
                l += 1

        # If res[0] is still infinity, no valid window was found
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]