# fungsi pertambahan
def plus (a,b):
    return a+b

# fungsi pengurangan
def minus (a,b):
    return a - b

# fungsi perkalian
def mult (a,b):
    return a * b

# fungsi pembagian
def div (a,b):
    if b == 0:
        return a / b

# Definisi fungsi pohon ekspresi
def tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression

        if operator == '+':
            return tree(left) + tree(right)
        elif operator == '-':
            return tree(left) - tree(right)
        elif operator == '*':
            return tree(left) * tree(right)
        elif operator == '/':
            if tree(right) == 0:
                return "Pembagian oleh nol tidak diperbolehkan"
            return tree(left) / tree(right)
    else:
        return expression

# Contoh pohon ekspresi
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi
result = tree(expression_tree)

print("Hasil Evaluasi pohon ekspresi:", result)
