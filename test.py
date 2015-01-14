import pycrypt

crypto = pycrypt.Ncaesar()
x = crypto.encrypt("text of your choice.")
print(x)
y = crypto.decrypt(x[0], x[1])
print(y)
