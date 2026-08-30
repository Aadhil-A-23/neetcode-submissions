class Solution:

    def encode(self, strs: List[str]) -> str:
        encod = ""
        for char in strs:
            encod += str(len(char))+"#"+char
        return encod

    def decode(self, s: str) -> List[str]:
        decod = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            start = j + 1
            stop = start + length
            word = s[start:stop]
            decod.append(word)
            i = stop
        return decod