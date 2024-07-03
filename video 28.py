#DIR() DA LOS COMANDOS DE CADA TIPO DE VARIABLE O LISTA
user_prompt = "Enter a todo:"
todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
