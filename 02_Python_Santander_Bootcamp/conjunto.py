conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}


print()
print(" {:_^30} ".format("União"))
print("{:^9}".format(""), conjunto_a.union(conjunto_b))


print()
print(" {:_^30} ".format("Intersection"))
print("{:^12}".format(""), conjunto_a.intersection(conjunto_b))


print()
print(" {:_^30} ".format("Difference"))
print(" {:^12} ".format(""), conjunto_b.difference(conjunto_a))
print(" {:^12} ".format(""), conjunto_a.difference(conjunto_b))

print()
print(" {:_^30} ".format("Symmetric_difference"))
print(" {:^12} ".format(""), conjunto_b.symmetric_difference(conjunto_a))

conjunto_pertece_A = {1, 2, 3}
conjunto_pertece_B = {4, 1, 2, 5, 6, 3}

print()
print(" {:_^30} ".format("IsSubSet"))
print(" {:^12} ".format(""), conjunto_pertece_A.issubset(conjunto_pertece_B))
print("conjunto_pertence_A existe no conjunto_pertence_B")

print()
