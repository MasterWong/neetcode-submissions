class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        for element in nums:
            if element not in numsDict:
                numsDict[element] = 1
            else:
                numsDict[element] += 1
        freqDict = {}
        print(numsDict)
        for key, value in numsDict.items():
            print(freqDict)
            if value not in freqDict:
                freqDict[value] = [key]
            else :
                freqDict[value].append(key)

        answer = []
        print(freqDict)
        keyOfAns = list(freqDict.keys())
        keyOfAns.sort()
        keyOfAns.reverse()
        print(keyOfAns)
        i = 0
        while len(answer) < k:
            answer = answer + freqDict[keyOfAns[i]]
            i+=1

        return answer

        