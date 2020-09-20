import numpy as np

def LongSequence(num1,num2,num3, len_n1, len_n2, len_n3):

    Matrix = np.zeros((len_n1+1, len_n2+1, len_n3+1))

    for i in range(1, len_n1+1):
        for j in range(1, len_n2+1):
            for k in range(1, len_n3+1):
                if (num1[i-1] == num2[j-1] and num1[i-1] == num3[k-1]):
                    Matrix[i][j][k] = Matrix[i-1][j-1][k-1] + 1
                else:
                    Matrix[i][j][k] = max(max(Matrix[i-1][j][k], Matrix[i][j-1][k]), Matrix[i][j][k-1])
    return int(Matrix[len_n1][len_n2][len_n3])



if __name__ == "__main__":
    n1 = int(input())
    number1 = list(map(int, input().split()))

    n2 = int(input())
    number2 = list(map(int, input().split()))

    n3 = int(input())
    number3 = list(map(int, input().split()))

    p = LongSequence(number1,number2, number3, n1, n2, n3)

    print(p)