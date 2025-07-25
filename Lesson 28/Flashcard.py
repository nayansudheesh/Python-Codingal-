class flashcard:

    def __init__(self, word , meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+ ' ( '+self.meaning+')'
    
flash = []
print("Welcome to flashcard app")

while(True):
    word = input("Enter the name you want to add to the flashcard")
    meaning = input("Enter the meaning for the word you have added as name of the flashcard")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want another flashcard , 1 if you want to stop:"))

    if(option):
        break
print("Your flashcard")
for i in flash:
    print(">",i)
    