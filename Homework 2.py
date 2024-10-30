# Grant Browning
# UWYO COSC 1010
# Submission Date: 10/26/24
# HW 02
# Lab Section: Austin
# Sources, people worked with, help given to: GeeksforGeeks.org

def Translator(text):
    """Translates entered phrase to morse code."""

    Alpha_Translate = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
}

    morse_phrase = []

#if string_variable.isalpha():

    for letters in text.upper():
        if letters in Alpha_Translate:
            morse_phrase.append(Alpha_Translate[letters])

        elif letters not in text.upper():
            morse_phrase.append(" ") #Space


    return ' '.join(morse_phrase)


text = input("Please enter requested phrase to translate: ")
morse_text = Translator(text)
print(f"'{text}' translates to: \n {morse_text}")