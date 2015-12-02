def histogram(str1):
    dt1 = {}
    for c in str1:
        if c not in dt1:
            dt1[c] = 1
        else:
            dt1[c] += 1
    return dt1

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse
print histogram('Naveen')
