# 1 Mean
l = [int(input("Enter number: ")) for i in range(7)]
sum = 0
for i in l:
    sum += i
mean = sum / 7
print("mean is", mean)


# 2 Median
n = int(input("Enter how many datas to be entered: "))
l = [int(input("Enter number: ")) for j in range(n)]
l.sort()

if n % 2 == 0:
    median = (l[n//2] + l[n//2 - 1]) / 2
else:
    median = l[n//2]

print("median is", median)


# 3 Mode
d = {}
n = int(input("Enter how many datas to be entered: "))

for o in range(n):
    x = int(input("Enter number: "))
    d[x] = d.get(x, 0) + 1

max_freq = max(d.values())
modes = [k for k, v in d.items() if v == max_freq]

if max_freq == 1:
    print("No mode")
elif len(modes) == 1:
    print("Mode is", modes[0])
else:
    print("Modes are", modes)