import sys
len_p = int(input("Enter count of process: "))
len_r = int(input("Enter count of resource: "))

max = []
allocation = []
need = [[0 for _ in range(len_r)] for _ in range(len_p)]
resource = []
available = [0 for _ in range(len_r)]
safe_path = []

print("\nCount instances of resource: ")
i = 0
while i < len_r:
    try:
        p = int(input(f"R{i + 1} : "))
        i += 1
        resource.append(p)
    except:
        print("input is wrong!!")

print("\n\nMax matrix :")
i = 0
while i < len_p:
    try:
        p = list(map(int, input(f"P{i + 1} : ").split()))
        if len(p) != len_r:
            print("input is wrong!!")
            continue
        i += 1
        max.append(p)
    except:
        print("input is wrong!!")

print("\n\nAllocation matrix :")
i = 0
while i < len_p:
    try:
        p = list(map(int, input(f"P{i + 1} : ").split()))
        if len(p) != len_r:
            print("input is wrong!!")
            continue
        i += 1
        allocation.append(p)
    except:
        print("input is wrong!!")

for i in range(len_p):
    for j in range(len_r):
        need[i][j] = max[i][j] - allocation[i][j]
available = resource
# for i in range(len_p):
#     for j in range(len_r):
#         available[j] -= allocation[i][j]
#         if available[j] < 0 :
#             print("Somthing is wrong!")
#             sys.exit()
for _ in range(len_p):
    safe_check = True
    for i in range(len_p):
        check = True
        for j in range(len_r):
            if i in safe_path or available[j] < need[i][j]:
                check = False
                break
        if check:
            safe_path.append(i)
            for j in range(len_r):
                available[j] += allocation[i][j]
            safe_check = False
            break
    if safe_check:
        print("System is not safe!")
        sys.exit()

print("-------------------------")
print("\nSafe Path :")
# for x in safe_path:
#     print(f"p{x+1}", end=" -> ")
safe_path = [f"P{x+1}" for x in safe_path]
print(" -> ".join(safe_path))



#samp
# 5
# 3
# 10
# 5
# 7
# 7 5 3
# 3 2 2
# 9 0 2
# 2 2 2
# 4 3 3
# 0 1 0
# 2 0 0
# 3 0 2
# 2 1 1
# 0 0 2
