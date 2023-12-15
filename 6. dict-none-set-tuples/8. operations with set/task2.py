my_friend = {'Bill', 'Ash', 'Jim'}
jack_friends = {'Bill', 'Kir'}

union_me_jack = my_friend | jack_friends
print('Все наши друзья с Джеком', union_me_jack)

terry_friends = {'Zara', 'Pit'}
union_me_jack_terry = my_friend | jack_friends | terry_friends
print('Все наши друзья с Джеком и Терри', union_me_jack_terry)

jim_friends = {'Bill', 'Charmander'}
union_me_jim = my_friend | jim_friends
print('Все наши друзья с Джимом', union_me_jim)
