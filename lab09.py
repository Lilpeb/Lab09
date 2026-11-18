# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.



def two_sum(nums, target):
    # Outline (write your plan here first):
    #  
    # Create a list of numbers named 'nums' and one variable named 'target'
    # if the sum of i and j equle the target then return [i, j]
    # i must be less then j 
    # so my code needs to loop through the list and check is i and j equle the target 

    """
    nums: List[1,2,3,4,6,7,8,9] 
    target: 10
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    this should return [3,4] because 4 + 6 = 10
    """
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def max_profit(prices):
    # Outline:
    #   you have a list of stock prices for each day named prices, 
    # you want to find the maximum profit you can make by buying on one day and selling on a later day.
    # to do this, you can loop through the list of prices and keep track of the minimum price and maximum profit seen so far.
    # then finding the diffrence between the maximum price and minimum price will give you the maximum profit.


    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


def max_subarray(nums):
    # Outline:
    #   You have a list of numbers named nums.
    # you want to find the largest sum of any contiguous (in-a-row) block of numbers in nums.
    # to do this, you can loop through the list of numbers and keep track of the current sum and the maximum sum seen so far.
    # if the current sum becomes negative, reset it to 0. The maximum sum seen so far will be the answer.
    
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
