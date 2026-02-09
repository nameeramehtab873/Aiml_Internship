search_name=input("enter name to search in friends.txt:")
found=False
with open("friends.txt","r")as f:
    for line in f:
        if search_name.lower()==line.strip().lower():
            found=True
            break
        if found:
            print("found")
        else:
            print("not found")