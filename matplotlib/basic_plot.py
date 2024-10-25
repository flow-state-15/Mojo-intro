import matplotlib
matplotlib.use('Agg') # sets backend before importing pyplt. trying to fix no display issue
import matplotlib.pyplot as plt

print("debug breakpoint 1")
x = [1,2,3,4]
y = [1,2,3,4]

plt.scatter(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("plot test")
plt.draw()
print("debug breakpoint 2")

plt.savefig('testimg.png')
