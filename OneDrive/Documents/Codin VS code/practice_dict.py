nepali = {
    "Topi":"Cap",
    "Himalaya" : "Mountains"
}

print("Choose any one Word from the option : ", nepali.keys())
b= input ("Enter any word :")
print("The meaning of the word that you entered is", nepali[b])
print("The meaning of the word that you entered is", nepali.get(b))