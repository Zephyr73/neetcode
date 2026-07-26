class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        dict1 = {}
        for i, word in enumerate(strs):
            dict1[i] = {}
            for letter in word:
                if letter not in dict1[i]:
                    dict1[i][letter] = 1
                else:
                    dict1[i][letter] += 1

        visited = set()

        for i in range(len(strs)):
            if i not in visited:
                group = []
                for j in range(len(strs)):
                    if j not in visited and dict1[i] == dict1[j]:
                        group.append(strs[j])
                        visited.add(j)
                output.append(group)

        return output