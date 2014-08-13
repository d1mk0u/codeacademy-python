let = []
def digit_sum(n):
    n = str(n)
    for i in n:
        i = int(i)
        let.append(i)
    return sum(let)
print digit_sum(5555)
