def digit_sum(n):
    let = []
    n = str(n)
    for i in n:
        i = int(i)
        let.append(i)
    return sum(let)
print digit_sum(raw_input("Enter a positive integer:"))
