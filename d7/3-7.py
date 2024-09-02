strings = ["level", "radar", "hello", "world", "noon", "racecar", "python"]
count = 0
index = 0
while index < len(strings):
    s = strings[index]
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1
    index += 1
print("Number of strings where the first and last characters are the same:", count)
