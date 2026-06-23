MAP = {
    "}": "{",
    ")": "(",
    "]": "["
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        if len(s) % 2 != 0:
            return False
        for index, char in enumerate(s):
            if char in MAP.values():
                stack.insert(0, char)
            if char in MAP.keys():
                if len(stack) == 0:
                    return False
                if len(stack) > 0:
                    if not MAP[char] == stack.pop(0):
                        return False
        return len(stack) == 0