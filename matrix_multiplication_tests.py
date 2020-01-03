import matrix_multiplication as mm


# unit tests here
# test matrix multiplication:
# [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[5,4,3,2,1]] by
# [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
# results in [[55,55,55,55,55],[55,55,55,55,55],[55,55,55,55,55],[55,55,55,55,55],[35,35,35,35,35]]

def test_matmult():
    a = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
    b = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
    expected_answer = [[55, 55, 55, 55, 55], [55, 55, 55, 55, 55], [55, 55, 55, 55, 55], [55, 55, 55, 55, 55],
                       [35, 35, 35, 35, 35]]
    answer = mm.matmul(mm.Matrix(values=a), mm.Matrix(values=b))
    if answer == expected_answer
        return True
    else:
        print(expected_answer)
        print(answer)
        return False


print("Starting tests..")
print(test_matmult())
