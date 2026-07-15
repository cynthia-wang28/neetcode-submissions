class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = ""
        back = ""
        for char in s:
            if char.isalnum():
                char = char.lower()
                front = front + char
                back = char + back
        return front == back
        