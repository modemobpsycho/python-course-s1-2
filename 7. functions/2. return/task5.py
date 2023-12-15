def format_name_list(names: list[dict]) -> str:
    sp = []
    for i in names:
        sp.append(i['name'])
    if len(sp) == 0:
        return ''
    elif len(sp) == 1:
        return sp[0]
    else:
        if len(sp) == 2:
            return f'{sp[0]} и {sp[1]}'

        else:
            a = ''
            for i in range(1, len(sp) - 1):
                a += (sp[i - 1] + ', ')
            a += f'{sp[-2]} и {sp[-1]}'
            return a


assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {
                        'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {
                        'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'

assert format_name_list([{'name': 'Bart'}]) == 'Bart'

assert format_name_list([]) == ''

assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {
                        'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'

assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {
                        'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'

assert format_name_list(
    [{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'

print('Проверки пройдены')
