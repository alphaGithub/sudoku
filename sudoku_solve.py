#SUDUKO Puzzle(Using backtraking)

#display function to display suduko
def display(mat):
	for i in range(9):
		for j in range(9):
			if mat[i][j] != 0:
				print(mat[i][j], end=' ')
			else:
				print('_',end=' ')
			if (j+1)%3 == 0 :
				print('|', end=' ')
		if (i+1)%3 == 0:
			print()
			for i in range(0,12):
				print('--',end='')
		print()
	print('\n\n')

#checkRule function to check rules of suduko 
def checkRule(mat,pos,t):
	i,j=pos
	for m in range(0,9):
		if mat[m][j] == t:
			return False
	for n in range(0,9):
		if mat[i][n] == t:
			return False

	p=i//3
	q=j//3
	for m in range(0,3):
		for n in range(0,3):
			if(mat[(p*3)+m][(q*3)+n] == t):
				return False
	return True

#fill board
def placeat(mat,pos):
	i,j=pos
	k=mat[i][j]
	t=k
	while t<10:
		if checkRule(mat,pos,t):
			mat[i][j]=t
			return True
		else:
			t=t+1
	return False

#solve the suduko puzzle
def solve(mat,blist):
	display(mat)
	i=0
	l = len(blist)
	while i<l:
		if placeat(mat,blist[i]):
			i=i+1
			
		else:
			m,n=blist[i]
			mat[m][n]=0
			i=i-1
			if i==0:
				p,q = blist[i]
				if mat[p][q]>=9:
					return None
			if i<0:
				i=0
	display(mat)
	return mat



def main():
	fname=input('Enter file name :')
	f=open("./puzzle/"+fname,'r')
	mat=[]
	blist=[]
	for line in f.readlines():
		mat.append([int(x) for x in line.split(' ')[0:9]])
	
	for i in range(9):
		for j in range(9):
			if mat[i][j] == 0 :
				blist.append((i,j))

	solve(mat,blist)
	

if __name__ == "__main__":
	main()