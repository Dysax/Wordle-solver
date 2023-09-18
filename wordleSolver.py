from itertools import permutations

def get_input(prompt):
    return input(prompt).strip().upper().split()

def main():
    # Read 5-letter words from the file
    with open("C:\\Users\\luke1\\OneDrive\\Documents\\Wordle solver\\valid-wordle-words.txt", "r") as f:
        valid_words = set(line.strip().upper() for line in f)

    known_letters = get_input("Enter known letters separated by space: ")
    not_allowed = get_input("Enter not-allowed letters separated by space: ")
    fixed_positions = get_input("Enter fixed-position letters (like E5) separated by space: ")
    not_in_position = get_input("Enter letters that should not be in specific positions (like A5): ")

    fixed_dict = {}
    for item in fixed_positions:
        letter, pos = item[:-1], int(item[-1]) - 1
        fixed_dict[pos] = letter

    not_in_position_dict = {}
    for item in not_in_position:
        letter, pos = item[:-1], int(item[-1]) - 1
        not_in_position_dict[pos] = letter

    all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    permute_letters = known_letters.copy()
    for letter in all_letters:
        if letter not in known_letters and letter not in not_allowed:
            permute_letters.append(letter)

    for letter in fixed_dict.values():
        permute_letters.append(letter)

    perms = permutations(permute_letters, 5)
    filtered_perms = []

    for perm in perms:
        word = ''.join(perm)
        
        if word not in valid_words:
            continue

        skip = False
        for pos, letter in fixed_dict.items():
            if word[pos] != letter:
                skip = True
                break

        if skip:
            continue

        for pos, letter in not_in_position_dict.items():
            if word[pos] == letter:
                skip = True
                break

        if skip:
            continue

        if any(letter in word for letter in not_allowed):
            continue

        if not all(letter in word for letter in known_letters):
            continue

        filtered_perms.append(word)

    if not filtered_perms:
        print("No words found.")
    else:
        filtered_perms = list(set(filtered_perms))
        filtered_perms = filtered_perms[:50]

        print("Possible words:")
        for word in filtered_perms:
            print(word)

if __name__ == '__main__':
    main()
