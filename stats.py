def count_words(sentence):
    words = sentence.split()

    return len(words)

def count_characters(sentence):
    sentence = sentence.lower()
    character_count = {}

    for c in sentence:
        if c not in character_count:
            character_count[c] = 0
        character_count[c] += 1

    return character_count

def sort_on(dict):
    return dict["num"]

def sort_character_counts(character_counts):
    character_list=[]
    for key,value in character_counts.items():
        if key.isalpha():
            character_list.append({"char": key, "num": value})
    character_list.sort(reverse=True, key=sort_on)
    return character_list
