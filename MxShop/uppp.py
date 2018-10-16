# def solve(s):
#     upper = sum(l.isupper() for l in s)
#     lower = sum(l.islower() for l in s)
#     return [s.lower(), s.upper()][upper > lower]#[upper]
#
# kk = solve("kkUpLsdLLLLjjjhhhhhhh")
# print(kk)
# list1 = ['sdsd', "dsdsdsdww", "dsdsd33"]
# print(list1[True])
#
# bb = slice(0, 2, 1)
# print(bb.start)
# print(bb.stop)
# print(bb.step)
#
# a = list()

s = "HelloWorld"
bb = slice(5, 50, 2)

print(bb.indices(len(s)))
