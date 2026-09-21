import csv
##imdb file has no header row
def load_casts(filename: str) -> dict:
    """Read cast file with no header. Return (title, year) -> director and actors."""
    casts = {}
##director and actor pairs with top rated movies
    infile = open(filename, 'r', encoding = 'utf-8')
    reader = csv.reader(infile)

    for row in reader:
        if len(row) < 8:
            continue
        title = row[0].strip()
        year = row[1].strip()
        director = row[2].strip()
        actors = []
        i = 3
        while i < 8:
            if row [i].strip() != '':
                actors.append(row[i].strip())
            i += 1
        casts[(title, year)] = (director, actors)
    infile.close()
    return casts


def display_top_collaborations(limit=None) ->None:
    """Show director and actor pairs on top rated movies, most pairs first."""
    rated = set()
    infile = open('imdb-top-rated.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(infile)

    for row in reader:
        title = row['Title'].strip()
        year = row['Year'].strip()
        rated.add((title, year))
    infile.close()
    casts = load_casts('imdb-top-casts.csv')
    counts = {}

    for key in rated:
        if key not in casts:
            continue
        director, actors = casts[key]
        for actor in actors:
            pair = (director, actor)
##see how many movies they share
            if pair not in counts:
                counts[pair] = 0
            counts[pair] += 1
    ranking = []

    for pair in counts:
##highest count first
        ranking.append((pair[0], pair[1], counts[pair]))
    ranking.sort(key=lambda item: item[2], reverse=True)
    print('Top collaborations(top rated movies)')
    i = 0

    while i < len(ranking):
        if limit is not None and i >= limit:
            break
        print(i + 1, ranking[i][0], ranking[i][1], ranking[i][2])
        i +=1

##total box office per actor
def display_top_actors(limit=None) -> None:
    """Show actors ranked by total box office on top grossing movies."""
    grossing = {}
    infile = open('imdb-top-grossing.csv', 'r', encoding='utf-8')
    reader = csv.DictReader(infile)

    for row in reader:
        title = row['Title'].strip()
        year = row['Year'].strip()
        money = int(row['USA Box Office'].strip())
        grossing[(title, year)] = money
    infile.close()
    casts = load_casts('imdb-top-casts.csv')
    totals = {}

    for key in grossing:
        if key not in casts:
            continue
        director, actors = casts[key]
        money = grossing[key]
        for actor in actors:
            if actor not in totals:
                totals[actor] = 0
            totals[actor] = totals[actor] + money
    ranking = []

    for actor in totals:
        ranking.append((actor, totals[actor]))
    ranking.sort(key=lambda item: item[1], reverse=True)
    print('Top actors by box office (top grossing movies)')
    i = 0

    while i < len(ranking):
          if limit is not None and i >= limit:
              break
          print(i + 1, ranking[i][0], ranking[i][1])
          i = i + 1

##shows 10 of each
def main() -> None:
    """Test part a and b with first 10 results each."""
    display_top_collaborations(10)
    print()
    display_top_actors(10)
if __name__ == '__main__':
      main()
    
            

