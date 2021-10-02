def lengthOfLongestSubstring(s: str) -> int:
    best = 0
    while len(s) > best:
        track = [''] * len(s)
        for i in s:
            if i in track:
                last = i
                break
            else:
                track += i
        best = max(best, len(track))
        s = s[track.index(i) + 1:]
    return best

def lengthOfLongestSubstring(s):
    track = {}
    best = start = 0
    for i, c in enumerate(s):
        if c in track and start <= track[c]: #In track so update start to new dupe location
            start = track[c] + 1             #Note: needs <= to ignore other dupes that have been passed already
        else:
            best = max(best, i - start + 1)
        track[c] = i
    return best

#s = "pwwkew"
s = "abcabcbb"
print(lengthOfLongestSubstring(s))