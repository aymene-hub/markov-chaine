from creationmatrix import matrix




vect_c = matrix()


number_p=int(input("inserer le nomber des elements p : "))
print("la creation de vecteur initial pi:")
vect_c.CreateMat(1,number_p)
print("le vecteur initial pi:")
vect_c.ShowMat()



mat = matrix()
mat.CreateMat(number_p, number_p)  # Input a nxn5 matrix
print("Matrix:")
mat.ShowMat()

# verifier si la matrice est stochastique 
#print("Rows sum to one:", matrix.rows_sum_to_one(mat.matrix))

# Matrix power
power = int(input("Enter the power matrix : "))
result = matrix.puiss(mat.matrix, power)  # Raise to the input power
print(f"Matrix  power {power}:")
for row in result:
    print(row)

#pi de puissance n = vector pi0 * matrice p de puissance n 
print(f"pi a la puissance {power} egal :")
pin=matrix.matrix_multiply(vect_c.matrix,result)
for row in pin:
    print(row)