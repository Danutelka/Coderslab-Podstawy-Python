def chessboard(n=8):
    chess = ""
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                chess += "#"
            else:
                chess += " "
        chess += " \n"
    return chess


s = chessboard(8)
print(s)

