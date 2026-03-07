import re

# 1. 'a' followed by zero or more 'b'
print("1)")
pattern = r"ab*"
text = ["a", "ab", "abb", "abbb", "ac"]

for word in text:
    if re.fullmatch(pattern, word):
        print(word)

# 2. 'a' followed by two to three 'b'
print("\n2)")
pattern = r"ab{2,3}"
text = ["ab", "abb", "abbb", "abbbb"]

for word in text:
    if re.fullmatch(pattern, word):
        print(word)

# 3. lowercase letters joined with underscore
print("\n3)")
text = "hello_world test_case python_program"
pattern = r"[a-z]+_[a-z]+"
print(re.findall(pattern, text))

# 4. uppercase followed by lowercase
print("\n4)")
text = "Hello World Python REGEX Test"
pattern = r"[A-Z][a-z]+"
print(re.findall(pattern, text))

# 5. 'a' followed by anything ending with 'b'
print("\n5)")
pattern = r"a.*b"
text = ["ab", "acb", "a123b", "axxxb", "ac"]

for word in text:
    if re.fullmatch(pattern, word):
        print(word)

# 6. replace space, comma or dot with colon
print("\n6)")
text = "Python, is great. I love programming"
result = re.sub(r"[ ,\.]", ":", text)
print(result)

# 7. snake_case to camelCase
print("\n7)")
text = "snake_case_string"
result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)
print(result)

# 8. split string at uppercase letters
print("\n8)")
text = "SplitThisStringAtUppercase"
result = re.findall(r"[A-Z][^A-Z]*", text)
print(result)

# 9. insert spaces before capital letters
print("\n9)")
text = "InsertSpacesBetweenWords"
result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)

# 10. camelCase to snake_case
print("\n10)")
text = "camelCaseStringExample"
result = re.sub(r"([A-Z])", r"_\1", text).lower()
print(result)