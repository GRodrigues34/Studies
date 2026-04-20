import pandas as pd

game = ['skyrim', 'elden ring', 'baldurs gate', 'mineirinho']

rating = [10,10,10,0]

recommend = [True,True,True,False]

data = {
    'Game': game,
    'Rating': rating,
    'Recommend': recommend
}

games = pd.DataFrame(data)
print(games)
print("\n")

games.to_csv("games.csv")
print("\n")

games.info()
print("\n")
c = games.columns
print(c)
print("\n")
i = games.index
print(i)
print("\n")
