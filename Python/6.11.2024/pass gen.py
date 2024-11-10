f = open("pass_gen.txt", "w")

# for c1 in range(97, 123):
#     for c2 in range(97, 123):
#         for c3 in range(97, 123):
#             for c4 in range(97, 123):
#                 p = chr(c1) + chr(c2) + chr(c3) + chr(c4)
#                 f.write(p + "\n")

for c4 in range(97, 123):
    p = "p" + chr(c4)
    f.write(p + "\n")