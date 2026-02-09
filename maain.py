filename=input("enter file name to count lines(example:marks.txt):")
with open(filename,"r")as f:
    lines=f.readlines()
    print(f"total lines in {filename}:{len(lines)}")