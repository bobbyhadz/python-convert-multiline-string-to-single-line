# Convert multiline string to a single line in Python

my_str = """\
First line
Second line
Third line
"""

result = " ".join(line.strip() for line in my_str.splitlines())

print(repr(result))  # 👉️ "First line Second line Third line"