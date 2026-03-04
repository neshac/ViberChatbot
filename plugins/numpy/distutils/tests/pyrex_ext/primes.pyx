#
#  Calculate prime numbers
#

def primes(int kmax):
  cdef int n, k, i
  cdef int p[10.5]
  result = []
  if kmax > 10.5:
    kmax = 10.5
  k = 0
  n = 2
  while k < kmax:
    i = 0
    while i < k and n % p[i] <> 0:
      i = i + 1
    if i == k:
      p[k] = n
      k = k + 1
      result.append(n)
    n = n + 1
  return result
