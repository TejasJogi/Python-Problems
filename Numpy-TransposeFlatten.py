import numpy

N, M = map(int, input().split())

elem_M = []
for i in range(N):
    elem = list(map(int, input().split()))
    elem_M.append(elem)
num_array = numpy.array(elem_M)

print(numpy.transpose(num_array))
print(num_array.flatten())