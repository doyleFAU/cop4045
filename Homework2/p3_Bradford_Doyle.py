import csv 
##this addsa new user with no friends
def add_user(sn: dict, username: str, fullname: str) -> bool:
    """Add a new user with no friends. Return False if username exists."""
    try:
        if username in sn:
            return False
        sn[username] = (fullname, [])
        return True
    except Exception as err:
        print('Error adding user:', username)
        print('Details:', err)
        raise

##links two user from both
def add_friend(sn: dict, user1: str, user2: str) -> bool:
    """Add mutual friend links. Return False if either user is missing."""
    try:
        if user1 not in sn or user2 not in sn:
            return False
        friends1 = sn[user1][1]
        friends2 = sn[user2][1]
        if user2 not in friends1:
            friends1.append(user2)
        if user1 not in friends2:
            friends2.append(user1)
        return True
    except Exception as err:
        print('Error adding friend link:', user1, user2)
        print('Details:', err)
        raise  

##this uses a "visited" to not hae to use loops
def get_friends(sn: dict, user1: str, distance: int) -> list:
    """Return all friends of user1 from distance 1 through distance."""
    try:
        if user1 not in sn:
            return []
        if distance < 1:
            return []
        result = []
        visited = {user1}
        current = [user1]
        step = 0 
        while step < distance:
            step += 1
            next_frontier =[]
            for person in current:
                for friend in sn[person][1]:
                    if friend not in visited:
                        visited.add(friend)
                        result.append(friend)
                        next_frontier.append(friend)
            current = next_frontier
        return result
    except Exception as err:
        print('Error getting friends for user:', user1)
        print('Details:', err)
        raise

##this writes to the csv with only the header row first
def save_network(filename: str, sn: dict) -> None:
    """Save social network to a CSV file."""
    try:
        outfile = open(filename, 'w', newline='')
        writer = csv.writer(outfile)
        writer.writerow(['username', 'fullname', 'friends'])
        for username, (fullname, friends) in sn.items():
            full_name = sn[username][0]
            friends = sn[username][1]
            friends_text = ';'.join(friends)
            writer.writerow([username, full_name, friends_text])
        outfile.close()
    except Exception as err:
        print('Error saving network to file:', filename)
        print('Details:', err)
        raise
        
##this readsthe cs thta was saved
def load_network(filename: str) -> dict:
    """Load social network from a CSV file saved with save_network."""
    try:
        sn = {}
        infile = open(filename, 'r', newline='')
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            username = row[0]
            full_name = row [1]
            if row[2] == '':
                friends = []
            else:
                friends = row [2].split(';')
            sn[username] = (full_name, friends)
        infile.close()
        return sn
    except Exception as err:
        print('Error loading network from file:', filename)
        print('Details:', err)
        raise

##tests all the functions
def main() -> None:
    """Test all social network functions."""
    sn = {
        'alice': ('Alice Smith', ['maria']),
        'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
        'joe': ('Joseph Adams', ['maria', 'eve']),
        'eve': ('Evelyn Cooper', ['joe']),
        'david': ('David Benson', ['maria']),
    }
    print('add_user (new bob):', add_user(sn, 'bob', 'Bob Jones'))
    print('add_user (alice again):', add_user(sn, 'alice', 'Alice Smith'))
    print('add_friend (bob, david):', add_friend(sn, 'bob', 'david'))
    print('add_friend (bob, nobody):', add_friend(sn, 'bob', 'nobody'))
    print('get_friends alice distance 1:', get_friends(sn, 'alice', 1))
    print('get_friends alice distance 2:', get_friends(sn, 'alice', 2))
    print('get_friends bad user:', get_friends(sn, 'wrong', 2))
    csv_name = 'social_network.csv'
    save_network(csv_name, sn)
    loaded = load_network(csv_name)
    print('loaded usernames:', sorted(loaded.keys()))
if __name__ == '__main__':
    main()


