def spiralOrder(matrix):
    start_row = 0
    end_row = len(matrix) - 1
    start_column = 0
    end_column = len(matrix[0]) - 1

    column_row = 0
    row_flip = False
    column_flip = False

    result = []
    import pdb; pdb.set_trace()
    while start_row <= end_row and start_column <= end_column:
        if column_row == 0:
            if not column_flip:
                for j in range(start_column, end_column + 1):
                    result.append(matrix[start_row][j])
                start_row = start_row + 1
            else:
                for j in range(end_column, start_column - 1, -1):
                    result.append(matrix[end_row][j])
                end_row = end_row - 1
            column_flip = not column_flip
            column_row = 1

        elif column_row == 1:
            if not row_flip:
                for i in range(start_row, end_row + 1):
                    result.append(matrix[i][end_column])
                end_column = end_column - 1
            else:
                for i in range(end_row, start_row - 1, -1):
                    result.append(matrix[i][start_column])
                start_column = start_column + 1
            row_flip = not row_flip
            column_row = 0
    return result


spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
