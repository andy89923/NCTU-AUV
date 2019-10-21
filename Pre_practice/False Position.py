
error_threshold = 0.0001
a = -10
b = -9

def f(x):
    ans = x ** 2 - 6 * x + 4
    return ans

root = 0
while (b - a > error_threshold):
    fa = f(a)
    fb = f(b)
    x1 = a - ((b - a) * fa / (fb - fa))
    a = b
    b = x1
root = b

print(root)