class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for bracket in s:
            if bracket not in hashmap:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[bracket]:
                        return False
        
        return not stack
