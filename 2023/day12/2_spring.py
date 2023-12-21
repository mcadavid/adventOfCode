from functools import cache

def f(line):
    springs, report = line.split()
    springs, report = (springs+'?') * 5, eval(report) * 5
    # springs, report = (springs+'?'), eval(report)
    #print(springs, report)

    @cache
    def dp(position, n, result=0):
        if position == len(springs): 
            return n == len(report) # 0?

        if springs[position] in '.?': 
            result += dp(position+1, n)

        try:
            q = position + report[n]
            if '.' not in springs[position:q] and '#' not in springs[q]:
                result += dp(q+1, n+1)
        except IndexError: pass

        return result

    return dp(0, 0)

print(sum(map(f, open('input.txt'))))