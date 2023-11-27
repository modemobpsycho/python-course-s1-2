lang = input("Какой язык программирования будем учить?")

match lang:
    case "JavaScript":
        print("Ты можешь стать фронтенд разработчиком")
    case "Python":
        print("Ты можешь стать Data Scientist-ом")

    case "PHP":
        print("Ты можешь стать бекенд разработчиком")

    case "Solidity":
        print("Ты можешь стать Blockchain разработчиком")

    case "Java":
        print("Ты можешь стать мобильным разработчиком")
    case  _:
        print("Язык не важен, главное уметь решать задачи)")
