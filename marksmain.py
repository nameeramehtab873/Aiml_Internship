student_name=input("enter student name:")
marks=input("enter marks:")
with open("marks.txt","a")as f:
    f.write(f"{student_name}-{marks}\n")
    print("marks appended to marks.txt")

filename=input("enter file name to count lines(example:marks.txt):")
with open(filename,"r")as f:
    lines=f.readlines()
    print(f"total lines in {filename}:{len(lines)}")