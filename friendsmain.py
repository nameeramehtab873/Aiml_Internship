with open("friends.txt","w")as f:
    for i in range(3):
        name=input(f"enter friend name{i+1}:")
        f.write(name+"\n")
        print("friends name saved to friends.txt")



        