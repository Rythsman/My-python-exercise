def sqrt(n):
        Eps = 0.0001
        result = float(n)
        while True:
                lastvalue = result
                result = result - result/2.0 + n / 2.0/result
                if abs(lastvalue - result) < Eps:
                        break
                
        return result
                
