from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
    
        # Step 2: Initialization of the stack
        stack = []
        
        # Step 3: Process each component
        for component in components:
            if component == '' or component == '.':
                continue  # Ignore empty components and current directory references
            elif component == '..':
                if stack:
                    stack.pop()  # Move up one directory level
            else:
                stack.append(component)  # Add valid directory name to the stack
        
        # Step 4: Construct the simplified path
        simplified_path = '/' + '/'.join(stack)
        return simplified_path

sol = Solution()
print(sol.simplifyPath("/home//foo/"))