class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        
        temp = code * 2
        for i in range(len(code)):
            if k > 0:
                code[i] = sum(temp[i+1:i+k+1])
            else:
                code[i] = sum(temp[i+len(code) + k : i+len(code)])
        return code