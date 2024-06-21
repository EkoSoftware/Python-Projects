test = "bd3dae5fb91f88a4f0978222dfd58f59a124257cb081486387cbae9df11fb879"
res = ""
for i in test:
    res += str(hex(ord(i)))

print(res)
print(len(res))