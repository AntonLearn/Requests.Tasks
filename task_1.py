import requests

def who_is_most_intelligence(all_heroes, dict_heroes):
    l_all_heroes = len(all_heroes)
    for i_hero in range(l_all_heroes):
        name_hero = all_heroes[i_hero]['name']
        intelligence_hero = all_heroes[i_hero]["powerstats"]["intelligence"]
        if name_hero in dict_heroes:
            if intelligence_hero > dict_heroes[name_hero]:
                dict_heroes[name_hero] = intelligence_hero
    max_intelligence = 0
    for hero in dict_heroes:
        if dict_heroes[hero] > max_intelligence:
            max_intelligence = dict_heroes[hero]
            name_most_intelligence = hero
    return f'Самый умный герой {name_most_intelligence}, уровень интеллекта {max_intelligence}'

URL_HEROES = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
HEROES = {"Hulk": 0, "Captain America": 0, "Thanos": 0}

if __name__ == '__main__':
    print(who_is_most_intelligence(requests.get(URL_HEROES).json(), HEROES))