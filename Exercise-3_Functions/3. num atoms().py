def num_atoms(amount_in_grams, atomic_weight_in_grams_per_mole=196.97):
    avogadro = 6.022*(10**23)
    num_of_atoms = amount_in_grams*avogadro/atomic_weight_in_grams_per_mole
    print(num_of_atoms)
    return num_of_atoms
