print("Enter a string of 3 words")
w1 = input("Enter first word: ")
w2 = input("Enter second word: ")
w3 = input("Enter third word: ")
class reversal:
    def __init__(self,w1,w2,w3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
    def reverse(self):
        return self.w1[::-1] , self.w2[::-1], self.w3[::-1]
r = reversal(w1,w2,w3)
reversed_words = r.reverse()
print("reversed words are:", reversed_words)