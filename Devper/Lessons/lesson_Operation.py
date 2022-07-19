# 空格也占位
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

#查询位置
astring = "Hello world!"
print(astring.index("o"))

#统计个数
astring = "Hello world!"
print(astring.count("l"))

#截取
astring = "Hello world!"
print(astring[3:7])

astring = "Hello world!"
print(astring[3:7:2])

astring = "Hello world!"
print(astring[3:7])   #截取输出
print(astring[3:7:1]) #跳过step输出

#反转输出
astring = "Hello world!"
print(astring[::-1])

#大小写转换
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

#开头结尾是否包含某字符串
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("!"))
print(astring.endswith("asdfasdfasdf"))

#以空分割数据
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))