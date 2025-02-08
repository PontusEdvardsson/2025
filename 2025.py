print("Vilka värden har A, B när din ekvation står på formen: ax + b = 0\n")
print("A:")
a = float(input())
print("B:")
b = float(input())
if(a != 0):
    x = ((0-b)/a)
    print("x är lika med",x)
else:
    print('Inga lösningar')