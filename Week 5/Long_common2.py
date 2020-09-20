import numpy as np

def LongSequence(num1, num2, len_n1, len_n2):

    
    Matrix = np.zeros((len_n2+1, len_n1+1))

    for i in range(1,len_n2+1):
        for j in range(1,len_n1+1):
            if num1[j-1] == num2[i-1]:
                Matrix[i][j] = Matrix[i-1][j-1]+1
            else:
                Matrix[i][j] = max(Matrix[i-1][j], Matrix[i][j-1])
    return Matrix[len_n2][len_n1]






if __name__ == "__main__":
    n = int(input())
    number1 = list(map(int, input().split()))
    n2 = int(input())
    number2 = list(map(int, input().split()))

    p = int(LongSequence(number1, number2, n, n2))
    print(p)
    