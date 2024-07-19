spam = ['apples','bananas','tofu']
bacon = ''
for letter in range(len(spam)-1):
    bacon = bacon + spam[letter] +','
bacon = bacon+spam[len(spam)-1]

print(bacon)

