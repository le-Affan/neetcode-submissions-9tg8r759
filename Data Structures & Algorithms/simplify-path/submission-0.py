class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for i in path:
            if i != "/":
                curr += i
            
            if i == "/":
                if curr == "" or curr == ".":
                    curr = ""
                    continue

                elif curr == "..":
                    if stack:
                        stack.pop()              
                else:
                    stack.append(curr)
                
                curr = ""
        
        # process last token
        if curr == "" or curr == ".":
            pass
        elif curr == "..":
            if stack:
                stack.pop()
        else:
            stack.append(curr)


        res = ""

        for x in stack:
            res += "/" + x
        
        return res if res else "/"

