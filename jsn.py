
import json
# a=[23,4,23,4,244]
# b=json.dumps(a)
# print(b)
#
# c={
#     "a":1,
#     "ab":43
# }
# print(c)
# print(json.dumps(c))


# Step 1: Write normal text to samp.txt
with open("samp.txt", 'w') as f:
    f.write("This is normal text.\n")
    print(" Normal text written to samp.txt")

# Step 2: Write JSON data to samp.txt
jd = {
    "name": "Awais",
    "age": 23,
    "skills": ["Python", "Git"]
}

with open("samp.txt", 'a') as f:  # 'a' means append
    a=f.write("\nJSON Data Below:\n")
    f.write(json.dumps(jd, indent=4))  # JSON string likhna
    print("JSON data added to samp.txt")

# Step 3: Save JSON data to a .json file
with open("output.json", 'w') as jf:
    json.dump(jd, jf, indent=4)
    print(" JSON data written to output.json")

# Step 4: Read and print both files
print("\n Contents of samp.txt:")
with open("samp.txt", 'r') as f:
    print(f.read())

print("\n Contents of output.json:")
with open("output.json", 'r') as jf:
    print(jf.read())
with open("output.json", 'r') as f:
    data = json.load(f)  # Converts JSON → Python dict

print("✅ JSON loaded from output.json:")
print(data)
print("🔍 Access example:", data['name'])  # Accessing value



