s = "jgiAkjffaAUGDJiiijjh@@###"
q = ["j", "A", "@"]

hash_list = [0] * 127

for ch in s:
    ascii_val = ord(ch)
    hash_list[ascii_val] += 1

for ch in q:
    acscii_val = ord(ch)
    print(hash_list[ascii_val])