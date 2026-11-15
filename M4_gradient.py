
import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return (x + 3) ** 2

def derivative(x):
    return 2 * (x + 3)

x = 2
learning_rate = 0.1
iterations = 100

points = [x]

for i in range(iterations):
    grad = derivative(x)
    x = x - learning_rate * grad
    points.append(x)

    print("Iteration:", i + 1, "x =", x, "y =", function(x))

print("\nLocal Minimum x:", x)
print("Minimum value y:", function(x))

# Plot graph
X = np.linspace(-5, 4, 100)
Y = function(X)

plt.plot(X, Y, label="y = (x+3)^2")
plt.plot(points, [function(p) for p in points], 'ro-', label="Iterations")
plt.scatter(x, function(x), color='green', label="Minimum Point")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient Descent")
plt.legend()
plt.grid()
plt.show()
