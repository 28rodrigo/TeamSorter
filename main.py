import random

# Function to read teams from a file
def read_teams(file_path):
    with open(file_path, 'r') as file:
        teams = [line.strip() for line in file.readlines()]
    return teams

# Function to generate all matchups in a round-robin format
def generate_round_robin_matchups(teams):
    matchups = []
    num_teams = len(teams)
    for i in range(num_teams):
        for j in range(i + 1, num_teams):
            matchups.append((teams[i], teams[j]))
    random.shuffle(matchups)
    return matchups

# Function to display matchups
def display_matchups(matchups):
    for match in matchups:
        print(f"{match[0]} vs {match[1]}")


# Function to display matchups
def write_matchups(matchups,file_path):
    with open(file_path, 'a') as file:
        for match in matchups:
            file.write(f"{match[0]} vs {match[1]}\n")
        file.close()

# Main function
def main():
    file_path = 'teams.txt'
    teams = read_teams(file_path)
    matchups = generate_round_robin_matchups(teams)
    write_matchups(matchups,"sorteio.txt")
    display_matchups(matchups)

if __name__ == "__main__":
    main()
