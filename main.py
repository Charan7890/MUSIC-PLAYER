import os,fnmatch
from multithreading import Thread
from time import sleep
from pygame import mixer
no_of_drives=int(input('enter number of drives you have:'))
drives=input('enter drive(C:/D:/E:/):').upper().split()

# for drive in drives:
# 	subfolders = [f.path for f in os.scandir(drive+'://') if f.is_dir() ]
# 	print(subfolders)

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
		return result
songs_list=[]
for drive in drives:
	p=find('*.mp3', drive +':\\')
	if p==[]:
		pass
	else:
		songs_list.extend(p)
for item in range(len(songs_list)):
	print(item+1,':',songs_list[item][3:])
class MusicPlayer:
	def play_music(self):
		mixer.music.play()
	def unpause_music(self):
		mixer.music.unpause()
	def pause_music(self):
		mixer.music.pause()
	def loop_song(self,val):
		loops=2
	def change_song(self):
		print(songs_list)
		song_number=int(input('enter the number which you want to play:'))
		mixer.music.load(songs_list[song_number-1])
		mixer.music.play()
def set_timer():
	timer=int(input('set timer(in minutes):'))*60
	while timer:
		sleep(timer)
		timer=0
	mixer.quit()


song=MusicPlayer()
mixer.init()
# path_of_song=input('Enter song path or folder path:')
mixer.music.load(songs_list[0])
mixer.music.play()
true=True
try:
	while true:
		op=int(input('Enter the option you were prefer to:\n1.unpause 2.pause 3.loop_song 4.change song 5.set timer 6.exit:'))
		if op==3:
			inp=input('Do you want to loop the song:\nIf yes type "YES" or "NO":').upper()[0]
			if inp=='Y':
				inp2=int(input('enter number of times:'))
				song.loop_song(inp2)
			else:
				pass
		elif op==1:
			song.unpause_music()
		elif op==2:
			song.pause_music()
		elif op==4:
			song.change_song()
		elif op==5:
			if __name__=='__main__':
				t1=Thread(target=set_timer)
				t1.start()
				t1.join()
		elif op==6:
			true=False
		else:
			print('Invalid operator')
except ValueError:
	pass

