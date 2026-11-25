import glob

char_list = []

# Read all .txt files in the current folder
for file in glob.glob("*.txt"):
    with open(file, "r") as f:
        data = f.read()
        for ch in data:
            char_list.append(ch)

print(char_list)
