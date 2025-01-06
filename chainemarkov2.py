from creationmatrix import matrix



mat = matrix()
vect= matrix()


number_p=int(input("inserer le nomber des elements p : "))


print("cration matrix p :")
matrixp=mat.CreateMat(number_p, number_p) 
print("Matrix p:")
mat.ShowMat()

print("le vector solution :")
vector_b = matrix.Createvector(number_p+1)

print("la matrice transpose de matrix p :")
trnsp=matrix.transpose(mat.matrix)
for row in trnsp:
    print(row)

print("la subtraction entre la matrice diagonal et transpose de matrix :")
sub=matrix.substract(trnsp)
for row in sub:
    print(row)



print("Final matrice apres ajoute nouvelle row :")
vector = [1,1,1,1]  # faut change taille de vector vector la meme taille de matrice
mat.add_row(sub,vector)
for row in sub:
    print(row)

solution=matrix.gauss(sub,vector_b)
if solution is not None:
    print("Solution to the system:")
    print(solution)
else:
    print("No solution found.")


