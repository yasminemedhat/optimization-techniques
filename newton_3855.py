import math

# The wanted equation
def evaluateNewX(x):
    f1 = 2 * math.cos(x) - (0.2 * x)
    f2 = 2 * math.sin(x) + 0.2
    return x + (f1/f2)

def newtonMethod(x, iterations):
    i = 0
    old_x = x
    print("Initial guess for x: ", old_x)
    while i < iterations:
        new_x = evaluateNewX(old_x)
        error = abs(old_x - new_x) / new_x
        i +=1
        print("iteration ", i, "  x:", new_x, "   relative error: ", error)
        old_x = new_x
    return new_x


def main():
    initialGuess = 2.5 
    iterations = 3
    optimal_X = newtonMethod(initialGuess,iterations)
    print()
    print("Optimal x: ", optimal_X)
    f1 = 2 * math.cos(optimal_X) - (0.2 * optimal_X)
    print("value for first derivative of the function: ",f1)


if __name__ == '__main__':
    main()