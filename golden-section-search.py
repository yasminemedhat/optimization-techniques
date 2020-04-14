import math 
r = 0.618
e = 0.382

def evaluateFX(x):
    return 2*math.sin(x)-0.1 * (x**2)


def goldenSectionMethod(xl,xu,tolerance):
    # first iteration
    x2 = xu - r * (xu - xl)
    x1 = xl + r * (xu - xl)
    fx2 = evaluateFX(x2)
    fx1 = evaluateFX(x1)
    i = 0

    while 1:
        i+=1
        error_bound = e * (xu-xl)
        print("iteration ", i, "   optimal point: ", max(fx1,fx2), "   error bound: ", error_bound)
        if (error_bound) < tolerance:
            if fx2 > fx1:
                return x2, fx2
            else:
                return x1, fx1
        if fx1 > fx2:
            xl = x2
            x2 = x1
            fx2 = fx1 
            x1 = xl + r * (xu - xl)
            fx1 = evaluateFX(x1)
        else: 
            xu = x1
            x1 = x2
            fx1 = fx2 
            x2 = xu - r * (xu - xl)
            fx2 = evaluateFX(x2)

def main():
    optimumX, fmax = goldenSectionMethod(0,4,0.06)
    print()
    print("optimum x: " , optimumX)
    print("fmax: ", fmax)

if __name__ == '__main__':
    main()

