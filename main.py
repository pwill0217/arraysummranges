# Given a sorted integer array without duplicates,
# return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

def summaryRanges(nums):
    if not nums:
        return []

    ranges = []
    start = end = nums[0]

    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{end}")
            start = end = num

    # Add the last range
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{end}")

    return ranges

nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))  # Output: ['0->2', '4->5', '7']

#Here's a breakdown of how the code works:

#Initialization: The start and end pointers are initially set to the first element of the array (nums[0]). These pointers represent the current range being considered.

# through the array: The code iterates through the array starting from the second element (nums[1:]). It checks each number in the array.

#Updating pointers for consecutive sequences: If the current number (num) is consecutive to the previous number (end + 1), it updates the end pointer to include the current number in the range. This means the sequence continues.

#Handling breaks in the sequence: If the current number is not consecutive, it means there's a break in the sequence. In this case:

#If start and end are equal, it means there was only one number in the sequence. So, it appends that single number as a string to the ranges list.
#If start and end are different, it means there was a range of numbers. So, it appends the range in the format "start->end" to the ranges list.
#Updating pointers for the next range: After handling the break, it updates both start and end pointers to the current number (num). This initializes the next range.

#Handling the last range: After the loop finishes, it checks if there's a range left (i.e., if start is different from end). If there's a range, it appends it to the ranges list.

#Returning the summary: Finally, it returns the list of summary ranges.

#The f"{start}->{end}" syntax is a formatted string literal (f-string) in Python. It allows embedding Python expressions inside a string using curly braces {}. So, f"{start}->{end}" dynamically substitutes the values of start and end into the string to create the range representation.




