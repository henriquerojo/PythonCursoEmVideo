from pygame import mixer
print('\033[1m===EXERCÍCIO 023===\033[m')
mixer.init()
mixer.music.load('hinodobrasil.mp3')
mixer.music.play()
input('\033[31mCurte o som\033[m')
