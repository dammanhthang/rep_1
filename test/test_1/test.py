class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        for i in ransomNote:
            print(i, ransomNote.count(i), magazine.count(i))
            if ransomNote.count(i) <= magazine.count(i):
                count=count+1
        if count==len(ransomNote):
            return True
        else:
            return False
