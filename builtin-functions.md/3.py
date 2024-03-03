world = input()
if world.lower() == world[::-1].lower():
    print("YES")
elif world.lower() != world[::-1].lower():
    print("NO")