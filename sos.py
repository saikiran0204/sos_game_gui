from tkinter import *

board = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def verticalo(i,j):
	if board[i-1][j] == 's' and board[i+1][j] == 's':
		return True
	else:
		return False
def horo(i,j):
	if board[i][j-1] == 's' and board[i][j+1] =='s':
		return True
	else:
		return False
def diago(i,j):
	if (board[i-1][j-1] == 's' and board[i+1][j+1] == 's') or (board[i-1][j+1] == 's' and board[i+1][j-1] == 's'):
		return True
	else:
		return False
def diag1(i,j):
	if board[i-2][j-2] == 's' and board[i-1][j-1] == 'o':
		return True
	else:
		return False
def diag2(i,j):
	if board[i-2][j+2] == 's' and board[i-1][j+1] == 'o':
		return True
	else:
		return False
def diag3(i,j):
	if board[i+2][j-2] == 's' and board[i+1][j-1] == 'o':
		return True
	else:
		return False
def diag4(i,j):
	if board[i+2][j+2] == 's' and board[i+1][j+1] == 'o':
		return True
	else:
		return False
def vert1(i,j):
	if board[i-2][j] == 's' and board[i-1][j] == 'o':
		return True
	else:
		return False
def vert2(i,j):
	if board[i+2][j] == 's' and board[i+1][j] == 'o':
		return True
	else:
		return False
def hor1(i,j):
	if board[i][j-2] == 's' and board[i][j-1] == 'o':
		return True
	else:
		return False
def hor2(i,j):
	if board[i][j+2] == 's' and board[i][j+1] == 'o':
		return True
	else:
		return False

def check(op,i,j):
	if op == "s":
		if i > 1 and j > 1:
			if diag1(i,j):
				return True
		if i > 1 and j < 23:
			if diag2(i,j):
				return True
		if i < 23 and j > 1:
			if diag3(i,j):
				return True
		if i < 23 and j < 23:
			if diag4(i,j):
				return True
		if j > 1:
			if hor1(i,j):
				return True
		if j< 23:
			if hor2(i,j):
				return True
		if i > 1:
			if vert1(i,j):
				return True
		if i < 23:
			if vert2(i,j):
				return True
		return False	
	else:
		if (i == 0 and j == 0) or (i == 0 and j == 24) or (i == 24 and j == 0) or (i == 24 and j == 24):
			pass
		elif i == 0 or i == 24:
			if horo(i,j):
				return True
		elif j == 0 or j == 24:
			if verticalo(i,j):
				return True
		else:
			if verticalo(i,j) or horo(i,j) or diago(i,j):
				return True
	return False

def choice(op,i,j):
	# b.destroy()
	global turn
	board[i][j] = op
	if turn == 0:
		turn = 1
		name1.set('*')
		name2.set("")
		if check(op,i,j):
			global player2
			player2 = player2 + 1
			varplayer2.set(str(player2))
	else:
		turn = 0
		name1.set("")
		name2.set('*')
		if check(op,i,j):
			global player1
			player1 = player1 + 1
			varplayer1.set(str(player1))
	#board1()
	Label(frame2,text=op).grid(row=i,column=j)

def end(frame3):
	frame2.destroy()
	frame3.destroy()
	if player1 > player2:
		Label(r,text=name11 + ' won the game').grid(row=0,column=0)
	elif player2 > player1:
		Label(r,text=name22 + " won the game").grid(row=0,column=0)
	else:
		Label(r,text=name11 + " and " + name22 + " won the game").grid(row=0,column=0)

def left(event,i,j):
	choice("s",i,j)

def right(event,i,j):
	choice("o",i,j)

def board1():
	frame1.destroy()
	frame3 = Frame(r)
	Label(frame3,text="turn").grid(row=0,column=0)
	Label(frame3,text="Player").grid(row=0, column=1)
	Label(frame3,text="score").grid(row=0,column=2)
	Button(frame3,text="end", command=lambda: end(frame3)).grid(row=0,column=5)
	Label(frame3,textvariable=name1).grid(row=1,column=0)
	player1 = Label(frame3,text=name11).grid(row=1, column=1)
	score1 = Label(frame3,textvariable=varplayer1).grid(row=1,column=2)
	Label(frame3,textvariable=name2).grid(row=2,column=0)
	player2 = Label(frame3,text=name22).grid(row=2, column=1)
	score2 = Label(frame3,textvariable=varplayer2).grid(row=2,column=2)
	frame3.grid(row=0,column=0)
	for i in range(0,25):
		for j in range(0,25):
			if board[i][j] == 0:
				#jk = Button(frame2,text="-",command=lambda i=i,j=j: click(i,j)).grid(row=i,column=j)
				jk = Button(frame2,text="-")
				jk.bind('<Button-1>',lambda e, i=i, j=j:left(e,i,j))
				jk.bind('<Button-3>',lambda e, i=i, j=j:right(e,i,j))
				jk.grid(row=i,column=j,sticky=W)
			else:
				Label(frame2,text=board[i][j]).grid(row=i,column=j)

def first1():
	player1 = Label(frame1,text="player 1").grid(row=1,column=0)
	entry1 = Entry(frame1)
	entry1.grid(row=1,column=3,sticky=W)
	player2 = Label(frame1,text="player 2").grid(row=2,column=0)
	entry2 = Entry(frame1)
	entry2.grid(row=2,column=3,sticky=W)
	Button(frame1,text="start",command=lambda entry1=entry1,entry2=entry2:get(entry1,entry2)).grid(row=3,column=2)
	Label(frame1,text="left click is o and right click is s").grid(row=4,column=0, columnspan=4)

def get(entry1,entry2):
	varplayer1.set("0")
	varplayer2.set("0")
	global name11
	global name22
	name11 = entry1.get()
	name22 = entry2.get()
	name1.set("* ")
	name2.set("")
	board1()

r =Tk()
r.title('sos game')
turn = 0
player1 = 0
player2 = 0
varplayer1 = StringVar()
varplayer2 = StringVar()
name1 = StringVar()
name2 = StringVar()
frame1 = Frame(r)
frame2 = Frame(r)
if __name__ == "__main__":
	first1()

frame1.grid(row=0,column=0)
frame2.grid(row=1,column=0)
r.mainloop()