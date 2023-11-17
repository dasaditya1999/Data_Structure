class Solution:
    # res = ""
    def DecimalToBinary(self,num,res):
        # global res
        if num>1:
            self.DecimalToBinary(num//2, res)
        res = res + str(num%2)
        return res

    def findPossibleBinaryNumbers(self,n):
        enumerateTill = 2**n - 1
        possibleBinaryNumbers = []
        for i in range(0,enumerateTill+1):
            res = ""
            resulted_binary = self.DecimalToBinary(i, res)
            possibleBinaryNumbers.append(resulted_binary)

        for i in range(0,len(possibleBinaryNumbers)):
            if len(possibleBinaryNumbers[i]) != n:
                zeros_to_be_added = n - len(possibleBinaryNumbers[i])
                possibleBinaryNumbers[i] = (zeros_to_be_added*'0')+possibleBinaryNumbers[i]
        return possibleBinaryNumbers

    def findDifferentBinaryString(self, nums: list[str]) -> str:
        print('Hey')
        possibleBinary = self.findPossibleBinaryNumbers(len(nums))
        print(possibleBinary)

        for i in possibleBinary:
            if i not in nums:
                print(i)
                break


sol = Solution()
nums = ['010','000','111']
sol.findDifferentBinaryString(nums)