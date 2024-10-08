import numpy as np

#definimos las matrices A y B

A= np.array([[1, 2],
            [3, 4]])

B= np.array([[5, 6],
            [7, 8]])

#luego calculamos 2A

dos_A = 2*A

#luego se calcula Bt que seria la transposición de la matriz b

B_T = B.T

#realizamos la suma de 2A + B^T

resultado= dos_A + B_T

#imprimimos el resultado

print("la matriz resultante es:", resultado) 