import random

word_list = [
    "apple", "table", "grape", "stone", "beach",
    "smile", "light", "train", "dream", "plant",
    "chair", "water", "cloud", "flame", "green",
    "laugh", "sweet", "power", "brush", "quick"
]

CurrentWord = random.choice(word_list)
GuessCount = 6

print("📣 Wordle Game! 5 harfli kelimeyi tahmin et. 6 hakkın var.")
# DEBUG: Gizli kelimeyi görmek istersen açabilirsin
print(f"(Gizli kelime: {CurrentWord})")

while GuessCount > 0:
    UserInput = input("Enter a 5-letter word: ").lower()

    if len(UserInput) != 5:
        print("Lütfen 5 harfli bir kelime gir.")
        continue

    if UserInput == CurrentWord:
        print("Congratulations! Doğru bildin!")
        break

    # Renkli değerlendirme
    result = ["⬜"] * 5
    temp_word = list(CurrentWord)

    # YEŞİL harfler (doğru yer)
    for i in range(5):
        if UserInput[i] == CurrentWord[i]:
            result[i] = "🟩"
            temp_word[i] = None

    # SARI harfler (yanlış yer)
    for i in range(5):
        if result[i] == "⬜" and UserInput[i] in temp_word:
            result[i] = "🟨"
            temp_word[temp_word.index(UserInput[i])] = None

    # Harf ve renk çıktısı
    for i in range(5):
        print(f"{UserInput[i].upper()} {result[i]}", end="  ")
    print("\n")

    GuessCount -= 1

if GuessCount == 0 and UserInput != CurrentWord:
    print(f"Tahmin hakkın bitti! Kelime: {CurrentWord.upper()}")
