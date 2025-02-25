def calculate_love_score(name1, name2):
    true = "true"
    love = "love"
    count_t = 0
    count_l = 0
    for letter_check in true:
        count_t += name1.lower().count(letter_check)
        count_t += name2.lower().count(letter_check)
    for letter_check in love:
        count_l += name1.lower().count(letter_check)
        count_l += name2.lower().count(letter_check)
    print(f"True love: {count_t}{count_l}")

calculate_love_score("Angela Yu", "Jack Bauer")
