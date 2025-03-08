def lei_de_morgan(a, b):
    # Cálculo usando a Lei de Morgan
    neg_and = not (a and b)
    neg_a_or_neg_b = (not a) or (not b)

    neg_or = not (a or b)
    neg_a_and_neg_b = (not a) and (not b)

    # Resultados
    print("Valores: A =", a, ", B =", b)
    print("¬(A ∧ B) =", neg_and)
    print("¬A ∨ ¬B =", neg_a_or_neg_b)
    print("¬(A ∨ B) =", neg_or)
    print("¬A ∧ ¬B =", neg_a_and_neg_b)
    print("Lei de Morgan (1ª):", neg_and == neg_a_or_neg_b)
    print("Lei de Morgan (2ª):", neg_or == neg_a_and_neg_b)

# Teste a função com diferentes valores de A e B
print("Exemplo 1:")
lei_de_morgan(True, True)

print("\nExemplo 2:")
lei_de_morgan(True, False)

print("\nExemplo 3:")
lei_de_morgan(False, True)

print("\nExemplo 4:")
lei_de_morgan(False, False)
