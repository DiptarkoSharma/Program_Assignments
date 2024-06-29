import os
import datetime
def read_all_data():
	text_file = open("lms.txt", "r") 	#reading file 
	lines = text_file.readlines()
	for line in lines:
		ln=line.strip('\n')
		print(ln)
	choice()

def choice():
	print('Type 1 For Entire Book Catalogue')
	print('Type 2 For Search a Book Based On Name/Author')
	print('Type 3 For Issue a Book')
	print('Type 4 For Return a Book')
	print('Type 5 For Donate a Book')
	num=int(input("Enter your choice:--"))
	if num==1:
		read_all_data()
	elif num==2:
		# print("choice 2")
		book_author=input("Enter Book or Author Name:--")
		search_book(book_author)
	elif num==3:
		book_name=input("Enter Book Name to Issue:--")
		issue_a_book(book_name)

	elif num==4:
		book_name=input("Enter Book Name to Return:--")
		return_a_book(book_name)
	elif num==5:
		donate_a_book()		

	else:
		print("invalid choice")

def search_book(book_author):
		book_author=book_author.replace(" ","")
		# print(b)
		new_list=[]
		book_available=[]
		text_file=open("lms.txt","r")
		lines=text_file.readlines()
		for line in lines:
			ln=line.strip('\n')
			# print(type(ln))
			rmv_spc=ln.replace(" ","")
			lt=rmv_spc.split(",")
			new_list.append(lt)
		for new in new_list:
			if new[1]==book_author or new[2]==book_author:
				book_available.append(1)
			else:
				book_available.append(0)
		if 1 in book_available:
			print("Book Available")
		else:
			print("Sorry Book Not Exist")
		choice()

# check_book_status(status)

def issue_a_book(book_name):
	book_name=book_name.replace(" ","")
	Current_Date = datetime.datetime.today() + datetime.timedelta(days=7)
	new_list=[]
	book_available=[]
	text_file=open("lms.txt","r")
	lines=text_file.readlines()
	for line in lines:
		ln=line.strip('\n')
		# print(type(ln))
		rmv_spc=ln.replace(" ","")
		lt=rmv_spc.split(",")
		new_list.append(lt)
	for new in new_list:
		if new[1]==book_name:
			status=new[3]
			book_available.append(1)
		else:
			book_available.append(0)
	if 1 in book_available:
		# check_book_status(status)
		if status=='In':
			# print("issue a Book")
			# os.remove("written_file.txt")
			print("The Book {} is issued to You , please return the book on or before {}".format(book_name,Current_Date))
			with open('lms.txt','w') as file_handler:
				for item in new_list:
					if item[1]==book_name:
						item[3]='Out'
						file_handler.write("{}\n".format(item))
					else:
						file_handler.write("{}\n".format(item))
						# print(item[1])
			infile="lms.txt"
			outfile="cleaned_file.txt"
			delete_list=["[","]","'"]
			fin=open(infile)
			fout=open(outfile,'w+')
			for line in fin:
				for word in delete_list:
					line=line.replace(word,"")
				fout.write(line)
			fin.close()
			fout.close()

			f=open('cleaned_file.txt')
			f1=open('lms.txt','w')
			for x in f.readlines():
				f1.write(x)
			f.close()
			f1.close()
			os.remove('cleaned_file.txt')
			

		else:
			print("Book already issued")
	else:
		print("Sorry Book Not Exist")
	choice()

def return_a_book(book_name):
	book_name=book_name.replace(" ","")
	Current_Date = datetime.datetime.today() + datetime.timedelta(days=10)
	new_list=[]
	book_available=[]
	text_file=open("lms.txt","r")
	lines=text_file.readlines()
	for line in lines:
		ln=line.strip('\n')
		# print(type(ln))
		rmv_spc=ln.replace(" ","")
		lt=rmv_spc.split(",")
		new_list.append(lt)
	for new in new_list:
		if new[1]==book_name:
			status=new[3]
			book_available.append(1)
		else:
			book_available.append(0)
	if 1 in book_available:
		if status=='Out':
			with open('lms.txt','w') as file_handler:
				for item in new_list:
					if item[1]==book_name:
						item[3]='In'
						file_handler.write("{}\n".format(item))
					else:
						file_handler.write("{}\n".format(item))
						# print(item[1])
			infile="lms.txt"
			outfile="cleaned_file.txt"
			delete_list=["[","]","'"]
			fin=open(infile)
			fout=open(outfile,'w+')
			for line in fin:
				for word in delete_list:
					line=line.replace(word,"")
				fout.write(line)
			fin.close()
			fout.close()

			f=open('cleaned_file.txt')
			f1=open('lms.txt','w')
			for x in f.readlines():
				f1.write(x)
			f.close()
			f1.close()
			os.remove('cleaned_file.txt')
			print("Thanks For Returning the Book")

		else:
			print("You are trying to return a book which is already Checked In")
	else:
		print("You are trying to return a wrong book")
	choice()


def donate_a_book():
	how_many_book=int(input("How many Book want to donate:--"))
	book_author=[]
	total_element=[]
	text_file=open("lms.txt","r")
	lines=text_file.readlines()
	for line in lines:
		total_element.append(line)
	cnt_line=len(total_element)
	for total in range(how_many_book):
		book_name=input("Enter Book Name:--")
		author_name=input("Enter Author Name:--")
		book_author.append([cnt_line+1,book_name,author_name,'In'])
		cnt_line=cnt_line+1
	with open('lms.txt','a') as f:

		for item in book_author:
			text_file=open("lms.txt","r")
			lines=text_file.readlines()
			f.write('\n {}'.format(''.join(str(item))))

	infile='lms.txt'
	outfile='new_file.txt'
	delete_list=["[","]","'"]
	fin=open(infile)
	fout=open(outfile,'w+')
	for line in fin:
		for word in delete_list:
			line=line.replace(word,"")
		fout.write(line)
	fin.close()
	fout.close()

	f=open('new_file.txt')
	f1=open('lms.txt','w')
	for x in f.readlines():
		f1.write(x)
	f.close()
	f1.close()
	os.remove('new_file.txt')
	print("Thanks for Donating a book")
	choice()

choice()