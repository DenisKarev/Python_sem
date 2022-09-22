# Пример проверки ложности утверждения (X == Y) ⋁ (X -> (Y ⋀ Z)) для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not ((x == z) or (x <= (y and z))):
                print(x, y, z)
