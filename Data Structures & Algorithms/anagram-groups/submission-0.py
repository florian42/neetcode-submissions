
class AnagramStr:
    def __init__(self, string: str):
        self.string = string
        self.counter = Counter(string)

    def __repr__(self):
        return self.string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for string in strs:
            key = frozenset(Counter(string).items())
            buckets[key].append(string)

        return list(buckets.values())



        