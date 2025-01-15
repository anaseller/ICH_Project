# Даны формулы: ¬((A ∨ B) ∧ (C ∨ D)) и ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)).
# Используя закон Де Моргана, докажите, что эти формулы эквивалентны.

# Согласно закону Де Моргана:
# ¬((A ∨ B) ∧ (C ∨ D)) = ¬(A ∨ B) ∨ ¬(C ∨ D)
# ¬(A ∨ B) = ¬A ∧ ¬B
# ¬(C ∨ D) = ¬C ∧¬D
# => ¬((A ∨ B) ∧ (C ∨ D)) = ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D))
# ∧ and
# ∨ or

not((A or B) and (C or D)) и (not A and not B) or (not C and not D)
not((A or B) and (C or D)) = not(A or B) or not(C or D)
not(A or B) = not A and not B
not(C or D) = not C and not D
=> not((A or B) and (C or D)) = (not A and not B) or (not C and not D)
