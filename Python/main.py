# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def textToSpeech(text, language):
    from gtts import gTTS
    import os
    sound = gTTS(text=text, lang=language, slow=False)
    # sound.save(text +".mp3")
    # os.system("start "+text+".mp3")
    sound.save("text.mp3")
    os.system("start text.mp3")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    textToSpeech('اهلا بك في خدمة المساعد الشخصي','ar')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
