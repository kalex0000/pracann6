import numpy as np
# -------------------------------
# Fuzzy Set Operations
# -------------------------------
def fuzzy_union(A, B):
    """Union of two fuzzy sets"""
    return np.maximum(A, B)
def fuzzy_intersection(A, B):
    """Intersection of two fuzzy sets"""
    return np.minimum(A, B)
def fuzzy_complement(A):
    """Complement of a fuzzy set"""
    return 1 - A
# -------------------------------
# Example
# -------------------------------
# Suppose we have a universe of discourse X
X = np.array([0, 1, 2, 3, 4, 5])
# Define fuzzy sets A and B over X (membership values between 0 and 1)
A = np.array([0.1, 0.5, 0.7, 1.0, 0.4, 0.2])
B = np.array([0.6, 0.3, 0.8, 0.5, 0.9, 0.1])

# Perform operations
union_AB = fuzzy_union(A, B)
inter_AB = fuzzy_intersection(A, B)
comp_A = fuzzy_complement(A)
# Print results
print("Universe X:", X)
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Union (A ∪ B):", union_AB)
print("Intersection (A ∩ B):", inter_AB)
print("Complement (¬A):", comp_A)
