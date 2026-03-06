import json
from datetime import date
from pathlib import Path 
import random

DATA_FILE = Path('data/recipe_history.json')

def load_history():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_history(history):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def get_sámi_recipes():
    '''16 real traditional Sámi recipes'''
    return {
        'Bidos': {'ingredients': ['reindeer meat', 'potato', 'carrot', 'onion'], 'time': '2 hours', 'steps': 'Cut meat and boil slowly with vegetables.', 'fact': 'The mostfamous Sámi reindeer soup.'},
        'Suovas': {'ingredients': ['reindeer meat', 'salt'], 'time': '2-3 days', 'steps': 'Salt the reindeer meat for about a day, then cold-smoke it for 1-2 days over birch or willow wood. Slice thinly and quickly sear on high heat before serving.', 'fact': 'Suovas is a traditional Sámi delicacy of salted and cold-smoked reindeer meat. Thinly sliced and seared, it is often served with lingonberries, pickled mushrooms or in flatbread. It is considered one of the finest smoked meat in the world.'},
        'Renskav': {'ingredients': ['reindeer meat', 'butter', 'pepper', 'salt', 'cream'], 'time': '45 minutes', 'steps': 'Reindeer meat (usually the hindquarters) is thinly sliced ​while frozen, making the process easier. The meat is fried in butter or reindeer fat until golden brown, then cream is added to create a sauce.', 'fact': 'Traditionally served with fried onion, mashed potatoes and lingonberry jam and sometimes pickles. There are variations with the addition of wild mushrooms (chanterelles) and onions.'},
        'Gahkku': {'ingredients': ['flour', 'milk', 'salt', 'butter'], 'time': '20 minutes', 'steps': 'Mix dough and bake flatbread on a hot pan', 'fact': 'Traditional soft and chewy Sami bread. Historically baked over an open fire or on hot stones.'},
        'Kaffeost': {'ingredients': ['cheese', 'coffee'], 'time': '5 minutes', 'steps': 'Cut cheese into cubes place it in the bottom of a cup and fill it with freshly brewed coffee.', 'fact': 'The cheese used is leipäjuusto, a spongy and slightly sweet cheese, traditionally made from reindeer milk, but now more often made from cow\'s or goat\'s milk. Initially, the drink helped reindeer herders warm up and replenish sodium deficiency. Sometimes served with cloudberry jam'},
        'Finnbeaf': {'ingredients': ['thinly sliced ​​reindeer (reinskav)', 'butter', 'mushrooms', 'onion', 'cream', 'sour cream', 'juniper berries', 'bacon'], 'time': '40 minutes', 'steps': 'Quickly sauté thin slices of frozen venison, bacon, mushrooms, and onions in butter. Then add water, sour cream, and cream, juniper berries, and a couple of slices of bacon, then simmer, covered, for about 10–15 minutes.', 'fact': 'This dish originates from the northern regions of Norway. Brown cheese (brunost) is often added to add sweetness and depth of flavor to the sauce.'},
        'Reindeer broth': {'ingredients': ['reindeer bones', 'spices', 'reindeer meat'], 'time': '6-7 hours', 'steps': 'Cover the reindeer bones completely with water, allowing the liquid to cover the bones. Cover the pot and set over medium heat. As it boils, a gray foam will begin to form—this is scale; skim it off with a slotted spoon. Once the broth boils, remove the lid and continue cooking, skimming off any new scale that appears. After boiling, it\'s recommended to add the spices. Cook the broth for 4-5 hours. Strain the finished soup through a sieve or cheesecloth.', 'fact': 'The Sámi people revere and love this broth; it can be said to be the basis of a diet.'},
        'Fish and cloudberry salad': {'ingredients': ['fish', 'cloudberries.'], 'time': '10 minutes', 'steps': 'Finely chop the fish, add berries, salt or sugar to taste.', 'fact': 'This salad has long been referred to among the Sámi people as “national”.'},
        'Smoked Arctic Char': {'ingredients': ['arctic char', 'salt'], 'time': 'several days', 'steps': 'Hang the fish, dry it, and then smoke it for several days on alder or willow using either the cold or hot method, which will give it a unique flavor and preserve the healthy fats.', 'fact': 'It has a rich aroma, the meat is dense but tender.'},
        'Birch Sap Drink': {'ingredients': ['birch sap'], 'time': '5 minutes', 'steps': 'Place crushed birch sap scale in a teapot and pour boiling water over it.', 'fact': 'This drink has a specific taste, is invigorating and rich in vitamins.'},
        'Sámi fish soup': {'ingredients': ['fish', 'onion', 'cloudberry', 'blueberry'], 'time': '1 hour', 'steps': 'Place the whole onion into the water at the very beginning of cooking and remove it at the end. Place fish head, then the body, and then the tail into the pot of water — so the fish swims into the net, not out of it — as if it were swimming into the pot. At the final stage of cooking, add cloudberries and blueberries to the soup.', 'fact': 'You can add potatoes and spices.'},
        'Blodplättar - traditional reindeer blood pancakes': {'ingredients': ['reindeer blood', 'rye flour', 'milk', 'onion', 'spises', 'butter',  'reindeer fat'], 'time': '1 hour', 'steps': 'Mix the completely thawed and strained reindeer blood (500 ml) with milk (200 ml) in a deep bowl, gradually pour in rye flour (200-250 g), stirring constantly with a whisk to avoid lumps, add fried onions, salt and spices to the mixture, let the dough “rest” for 30 minutes so that the flour swells and fry in a heated and greased frying pan in small portions like for pancakes for 2-3 minutes on each side until the edges become crispy.', 'fact': 'Traditionally served with lingonberry jam.'}
    }

def main():
    print('Buorre beaivi and Hello! 🌲')
    print('Welcome to Sámi Home Recipe Generator\n')         

    print('The Sámi are the indigenous people of Sápmi (Northern Finland, Norway, Sweden and Russia).')
    print('Traditional Sámi cuisine is simple, sustainable and deeply connected to nature - based on reindeer meat, fish, wild berries and herbs.\n"')
    print('Let\'s see what delicious Sámi dishes you can cook from what you already have at home today.')

    # === ADDING PRODUCTS ONE AT A TIME ===
    ingredients = []
    print('Enter the ingredients you have at home one by one.')
    print('When you\'re finished, just press Enter without typing anything.\n')

    while True:
        item = input('Ingredient: ').strip().lower()
        if not item:
            break

        ingredients.append(item)
        print(f'✅ Added: {item}')

    recipes = get_sámi_recipes()
    full_matches = []
    partial_matches = []

    for name, data in recipes.items():
        recipe_ings = data['ingredients']
        if all (ing in ' '.join(ingredients) for ing in recipe_ings):
            full_matches.append((name, data))
        elif any(ing in ' ' .join(ingredients) for ing in recipe_ings):
            partial_matches.append((name, data))

    today = date.today().isoformat()

    if full_matches:
        print('\n' + '='*65)
        print(f'🎉 Perfect! You can make these {len(full_matches)} Sámi recipes right now:')
        print('='*65)
        for name, data in full_matches:
            print(f'\n🍲 {name} ({data['time']})')
            print(f'Ingredients needed: {', '.join(data['ingredients'])}')
            print(f'Fact: {data['fact']}')
            print(f'Steps:\n{data['steps']}')
        history = load_history()
        history.append({'date': today, 'recipe': full_matches[0][0]})
        save_history(history)

    elif partial_matches:
        print(f'\nI found {len(partial_matches)} recipes that use some ingredients you have:')
        for name, data in partial_matches:
            print(f'\n🍲 {name} ({data['time']})')
            print(f'Ingredients needed: {', '.join(data['ingredients'])}')
            print(f'Fact: {data['fact']}')
            print(f'Steps:\n{data['steps']}')

    else:
        print(f'\nI couldn\'t find any recipes that match your ingredients this time.')
        print('Here\'s a random traditional Sámi recipe for inspiration:\n')

        name, data = random.choice(list(recipes.items()))
        print(f'🥳 {name} ({data['time']})')
        print(f'Ingredients needed: {', '.join(data['ingredients'])}')
        print(f'Fact: {data['fact']}')
        print(f'Steps:\n{data['steps']}')

        history = load_history()
        history.append({'date': today, 'recipe': name})
        save_history(history)

    history = load_history()
    if len(history) > 1:
        print('\nDearvvuođat / Warm regards 🌲 Enjoy Sámi cooking!')

if __name__ == '__main__':
    main()
    input('\nPress Enter to close...')                                  
                                
  