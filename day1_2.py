import re

nums = "one|two|three|four|five|six|seven|eight|nine"
nums_re = re.compile(r'(?=(\d|%s))' % nums)
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

file = open(file="input1.txt")
lines = file.readlines()
sumatory = 0

for line in lines:
    numbers = []
    for num in nums_re.findall(line):
        if num in nums:
            num = str(nums.index(num) + 1)
        numbers.append(num)
    sumatory += int(numbers[0] + numbers[-1])

print(sumatory)
