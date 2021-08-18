 
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for val in path.split('/'):
            if val == '.' or not val:
                continue
            if val == '..':
                if len(stack) > 0:
                    stack.pop()
                continue
            stack.append(val)
        
        return '/' + ('/'.join(stack))
                    
                    
