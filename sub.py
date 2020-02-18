def pizza_challenge(file_name):
    # read input from input_file.in
    f = open(file_name, "r") 

    # M: the maximum number of slices
    # N: the number of different types of pizzas

    M,N = [int(i) for i in list(f.readline().split())]
    pizza_types =[int(i) for i in list(f.readline().split())] 
    f.close()

    slices = 0
    K = 0
    ordered_pizzas = []
    while slices<=M:
        if pizza_types == []:
            break
        max_num = max(pizza_types)
        index_max = pizza_types.index(max_num)
        if slices+max_num<M:
            slices+= max_num
            pizza_types = list(filter(lambda a: a!=max_num,pizza_types))
            K+=1
            ordered_pizzas.append(index_max)
        else:
            pizza_types.pop()
    ordered_pizzas.reverse()
    return K,ordered_pizzas
    






