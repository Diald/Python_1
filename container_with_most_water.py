'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
https://leetcode.com/problems/container-with-most-water/description/'''
def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_area = 0
        while left<right:
            current_area = min(height[left],height[right])*(right-left)
            max_area = max(current_area,max_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
if __name__ == "__main__":
    import doctest
    doctest.testmod()