def make_square(num):
    if isinstance(num,(int,float)):
       
        return num * num
    else:
        return "Error! Give a valid number"

result = make_square(5.5)
print(result)