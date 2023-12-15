def get_domain_name(url):
    if '//' in url:
        a = url.split('//')
        if 'www' in a[1]:
            a[1] = a[1].split('.')
            return a[1][1]
        else:
            a[1] = a[1].split('.')
            return a[1][0]
    else:
        if 'www' in url:
            a = url.split('.')
            return a[1]
        else:
            a = url.split('.')
            return a[0]


assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") == 'github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')
