def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False

        return True

    return False