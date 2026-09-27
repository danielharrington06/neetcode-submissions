class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(len(nums2)):
            nums1.pop()
        #insertion sort with nums2
        i = 0 # tracks nums2
        while i < len(nums2):
            inserted = False
            j = 0
            while not inserted and j < len(nums1):
                print(i, j)
                if nums1[j] > nums2[i]:
                    nums1.insert(j, nums2[i])
                    inserted = True
                j += 1
            if not inserted:
                nums1.append(nums2[i])  
            i += 1

        