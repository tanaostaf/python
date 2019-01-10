from math import pow
import timeit

print("power by 3: ")

print("shift power      : "  + str(timeit.timeit('10 << 3',number = 1000000)))
print("power by operator: "  + str(timeit.timeit('10 ** 3',number = 1000000)))
print("math_pow         : "  + str(timeit.timeit('pow(10.0, 3)',number = 1000000)))

def reverse(s : str):
  return "".join(reversed(s))

print("---------------------------------------")
print("reverse list of strings: ")

print("by loop          : " + str(timeit.timeit('for _ in data: _ = "".join(reversed(_))', "data = ['math', 'test', 'pow', 'shift']", number = 100000 )))
print("by map()         : " + str(timeit.timeit('map(reverse, data)', "data = ['math', 'test', 'pow', 'shift']",  number = 100000, globals = {'reverse' : globals().get('reverse')} )))
input ('Press ENTER to exit') 