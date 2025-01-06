class matrix:
    def __init__(self):
        self.matrix = []



    def CreateMat(self,p, t):
        # Create a matrix with p rows and t columns
        self.matrix = []
        for i in range(p):
            row = []
            for j in range(t):
                value = float(input(f"Enter element for row {i+1}, column {j+1}: "))
                row.append(value)
            self.matrix.append(row)
    
    def Createvector(p):
        b = []
        for i in range(p):
            value = float(input(f"Enter element for b[{i+1}]: "))
            b.append(value)
        return b


    def ShowMat(self):
        if not self.matrix:
            print("Matrix is empty. Please create a matrix first.")
        else:
            for row in self.matrix:
                print(' '.join(map(str, row)))


    def add_row(self, subtracted_matrix,new_row):
        
        
        if not self.matrix:
            print("Matrix is empty. Please create a matrix first.")
            return
        
        # Ensure the new row has the same number of columns as the matrix
        if len(new_row) != len(self.matrix[0]):
            print(f"Error: New row must have {len(self.matrix[0])} elements.")
            return
        
        # Add the new row to the matrix
        subtracted_matrix.append(new_row)
        
    
    def rows_sum_to_one(matrixf):
    
        for row in matrixf:
            if abs(sum(row) - 1) > 1e-9:
                return False
        return True
    

    
    def matrix_multiply(A, B):
        if len(A[0]) != len(B):
            raise ValueError("Incompatible dimensions for matrix multiplication.")
        return [
            [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))
        ]

    
    def puiss(A, n):
        if len(A) != len(A[0]):
            raise ValueError("Matrix must be square for exponentiation.")

        size = len(A)
        # Identity matrix
        result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

        # Exponentiation by squaring
        base = A
        while n > 0:
            if n % 2 == 1:
                result = matrix.matrix_multiply(result, base)
            base = matrix.matrix_multiply(base, base)
            n //= 2
        return result


    def diagones(n):
        """for i in range(n):
            for j in range(n):
                if i == j:
                    return 1
                else:
                    return 0"""
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    

    def transpose(matrixf):
        """for i in range(len(matrixf)):
            for j in range(len(matrixf[0])):
                matrixf[i][j]=matrixf[j][i]
                """
                
        return [[matrixf[j][i] for j in range(len(matrixf))] for i in range(len(matrixf[0]))]
    

    def substract(matrixf):
        """for i in range(len(A)):
            for j in range(len(B[0])):
                SUB[i][j]=A[i][j]-B[i][j]
                """
        # Create a diagonal matrix
        size = len(matrixf)
        diag_matrix = matrix.diagones(size)

        # Subtract each diagonal element
        result = [
            [matrixf[i][j] - diag_matrix[i][i] if i == j else matrixf[i][j] for j in range(len(matrixf[i]))]
            for i in range(len(matrixf))
        ]
        return result
    


    def gauss(A, B):
    
        n = len(A)
        m = len(A[0])  
        M = [row[:] + [B[i]] for i, row in enumerate(A)]
        for i in range(min(n, m)): 
            max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
            M[i], M[max_row] = M[max_row], M[i]  
            for j in range(i + 1, n):
                if M[i][i] == 0:
                    continue  
                factor = M[j][i] / M[i][i]
                M[j] = [M[j][k] - factor * M[i][k] for k in range(len(M[i]))]
        x = [0] * m  
        for i in range(min(n, m) - 1, -1, -1):
            if M[i][i] == 0:
                continue  
            x[i] = (M[i][-1] - sum(M[i][j] * x[j] for j in range(i + 1, m))) / M[i][i]

        return x 