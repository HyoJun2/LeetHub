class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary, key 값을 알파벳들을 정렬한 값으로 사용
        answer = {}
            
        for word in strs:
            key = "".join(sorted(word))
            
            if key not in answer:
                answer[key] = [word]
            else:
                answer[key].append(word)
        
        return answer.values()