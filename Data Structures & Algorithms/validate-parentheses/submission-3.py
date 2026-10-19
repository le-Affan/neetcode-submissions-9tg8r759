class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
            
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
                continue

            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                # could use a hashmap to make this code cleaner but whatever
                if i == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif i == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif i == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        
        return True
