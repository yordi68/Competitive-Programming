class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = {}
        answer = []
        n = len(cpdomains)

        for i in range(n):
            cpdomains[i]= cpdomains[i].split()
            cpdomains[i][1] = cpdomains[i][1].split(".")
        dictionary = {}

        for item in cpdomains:
            length = len(item[1])

            for i in range(length):
                joined = ".".join(item[1][i:length])
                dictionary[joined] = dictionary.get(joined, 0) + int(item[0])

        for key in dictionary:
            answer.append(f'{dictionary[key]} {key}')

        return answer
