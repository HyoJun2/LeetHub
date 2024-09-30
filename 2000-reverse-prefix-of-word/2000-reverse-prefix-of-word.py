class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # find
        # [::-1]
        loc = word.find(ch)
        answer = (word[:loc+1:][::-1] + word[loc+1:])
        
        return answer