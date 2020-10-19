class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[:m]
        i = 0
        j = 0
        if nums1[0] < nums2[0]:
            nums1.insert(1, nums2[0])
            j += 1
        while j < n:
            if nums1[i] <= nums2[j]:
                while True:
                    try:
                        if nums1[i] < nums2[j]:
                            if i == n:
                                try:
                                    nums1.append(nums2[j])
                                    j += 1
                                except:
                                    break
                            else:
                                i += 1
                        else:
                            nums1.insert(i, nums2[j])
                            break
                    except:
                        break
        print(nums1)
x = Solution()
x.merge([1,2,3,0,0,0], 3, [2,5,6], 3)