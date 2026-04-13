class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = s.replace(" ", "").lower()
        charList = []
        for char in newString:
            if (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('0') and ord(char) <= ord('9')):
                charList.append(char) 

        lastIdx = len(charList) - 1
        frontIdx = 0
        print(charList)
        while lastIdx > frontIdx:
            if charList[lastIdx] != charList[frontIdx]:
                return False
            else:
                lastIdx -= 1
                frontIdx += 1

        return True
