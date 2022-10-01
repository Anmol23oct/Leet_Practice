class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        print(c)
        for i in word:
            c[i] -= 1
            
            s = []
            print("values",c.values())
            for j in c.values():
                print("j",j)
                if j:
                    s.append(j)
                print("s",s)
            if len(set(s)) == 1:
                return True
            
            c[i] += 1
        return False