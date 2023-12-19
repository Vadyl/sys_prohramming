def egyptian_fraction(numerator, denominator):
    result = []

    while numerator != 0:
        denomirator_res = -(-denominator // numerator)
        result.append(f"1/{denomirator_res}")

        numerator = numerator * denomirator_res - denominator
        denominator = denominator * denomirator_res

    return result



# 2, 3
# 6, 14
# 12, 13
a = int(input("numerator: "))
b = int(input("denumerator: "))

res = egyptian_fraction(a, b)
print(res)

