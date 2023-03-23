import requests


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


output = '0'
for i in range(134):
    out = []
    for j in range(50): 
        res = requests.get('http://10.10.8.10:1177/guess_bit?bit=' + str(i))
        out.append(len(res.content[9:-2]))

    if 307 in out:
        output += '1'
    else:
        output += '0'

print(text_from_bits(output))
