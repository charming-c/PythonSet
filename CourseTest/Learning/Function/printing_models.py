def print_models(unprinted_designed, completed_models):
    while unprinted_designed:
        current_designed = unprinted_designed.pop()
        print(f"Printing model:{current_designed}")
        completed_models.append(current_designed)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# 可以传入一个切片防止修改列表
unprinted_designed = ['phone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designed[:],completed_models)
show_completed_models(completed_models)
print(unprinted_designed)