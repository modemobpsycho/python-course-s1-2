value = [1, 2, 3]

match value:
    case int() | float():
        print("Имеем дело с числом")
    case str():
        print("Имеем дело со строкой")
    case list():
        print("Имеем дело со списком")
    case  _:
        print(f"Лучше с этим дел не иметь")