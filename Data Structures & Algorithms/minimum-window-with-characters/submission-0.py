class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        countT, window = {}, {}

        # filling map counT (baseline comparison)
        for c in t:
            countT[c] = 1+countT.get(c,0)

        have, need = 0, len(countT) # measure how far we are from the result
        res, resLen = [-1,-1], float("infinity")
        l=0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0) #sliding window count set

            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need: #reducing from left to see if we find smaller
                if (r-l+1) < resLen: #new optimum found
                    res = [l,r]
                    resLen = (r-l+1)
                
                # keep popin from the left in our window
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l +=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        




        
            

        