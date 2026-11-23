class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #keep place of seen stuff
        seen = {}
        #turn nums list into KV dict pair, make the address book
        for index, number in enumerate(nums):
            #find the complement
            need = target - number
            #check if need is a numebr in seen
            if (need in seen):
                #return the index of the matching need and index of current
                return [seen[need], index]
            #add the current number to the seen list
            seen[number] = index 