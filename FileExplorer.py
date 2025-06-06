def imgEdit():
    print("----------")
    print("FilExArtist V1.0")
    print("Starting up...")
    data=[]
    for i in range(10):
        data.append([" "," "," "," "," "," "," "," "," "," "])
    while True:
        itr=0
        print(" 0123456789")
        for i in range(10):
            print(itr,end="")
            for j in range(len(data[i])):
                print(data[i][j],end="")
            print("")
            itr+=1
        while True:
            paintX=input("Input X value, or input X if you are finished drawing: ")
            if paintX=="X":
                print("----------")
                for i in range(10):
                    for j in range(len(data[i])):
                        print(data[i][j],end="")
                    print("")
                input("Here's your drawing! press Enter to save and quit.")
                print("----------")
                return data
            try:
                int(paintX)
            except:
                print("ERROR: please insert a number or the letter X")
                continue
            paintX=int(paintX)
            if paintX>9 or paintX<0:
                print("ERROR: out of range")
                continue
            else:
                break
        while True:
            paintY=input("Input Y value: ")
            try:
                int(paintY)
            except:
                print("ERROR: please insert a number")
                continue
            paintY=int(paintY)
            if paintY>9 or paintY<0:
                print("ERROR: out of range")
                continue
            else:
                break
        if data[paintY][paintX]==" ":
            data[paintY][paintX]="█"
        else:
            data[paintY][paintX]=" "
        print("----------------")
    return

class node:
    def __init__(self,data,children=[],parent=None):
        self.data=data
        self.children=children
        if parent!=None:
            self.parent=parent
    def newNode(self,data):
        self.children.append(node(data,children=[],parent=self))
    def details(self):
        print("File name:", self.data[1])
        if self.children!=[]:
            print("Children:")
            itr=0
            for i in self.children:
                print(itr,": ",i.data[1],sep="")
                itr+=1
        else:
            print("No children")
        if self.data[0]=="txt":
            print("Text data:")
            for i in self.data[2:]:
                print(i)
            if self.data[2]=="":
                print("[No text]")
        if self.data[0]=="img":
            print("Image data:")
            for i in self.data[2]:
                print("".join(i))
            if self.data[2]=="":
                print("[No Image]")
        print("Controls:")
        if self.children!=[]:
            print("D: view the details of a file")
        print("B: Backtrack to this file's parent directory")
        if self.data[0]=="root" or self.data[0]=="fldr":
            print("N: make a new file here.")
        else:
            print("E: edit this file.")
        choose=input("")
        if choose=="B":
            return
        elif choose=="X":
            exit()
        elif choose=="D":
            if self.children==[]:
                print("ERROR: please choose an action from the list provided.")
                print("----------")
                self.details()
                return
            while True:
                choose1=input("Input the index number of the file you'd like to view. ")
                try:
                    int(choose1)
                except:
                    print("ERROR: please choose a number within the range provided.")
                    print("---------")
                    self.details()
                choose1=int(choose1)
                if choose1>len(self.children) or choose1<0:
                    print("ERROR: please choose a number within the range provided.")
                    print("---------")
                print("----------")
                self.children[choose1].details()
                return
        elif choose=="N":
            if self.data[0]!="root" and self.data[0]!="fldr":
                print("ERROR: please choose an action from the list provided.")
                ("----------")
                self.details()
                return
            else:
                print("What type of file would you like to make?")
                print("A: Folder")
                print("B: Text document")
                print("C: Drawing")
                make=input("")
                if make=="A" or make=="B" or make=="C":
                    fileName=input("What will you name the file? ")
                    if fileName=="":
                        print("ERROR: File name too short.")
                        return
                    else:
                        if make=="A":
                            make="fldr"
                        elif make=="B":
                            make="txt"
                        elif make=="C":
                            make="img"
                        self.newNode([make,fileName,""])
                        print("file created!")
                        print("----------")
                        self.details()
                        return
        elif choose=="E":
            if self.data[0]=="root" or self.data[0]=="fldr":
                print("ERROR: please choose an action from the list provided.")
                print("----------")
                self.details()
                return
            else:
                ays=input("ARE YOU SURE YOU WANT TO EDIT THIS FILE? it will overwrite the previous data. (Y/N)")
                if ays=="Y":
                    if self.data[0]=="txt":
                        print("Write the contents of the file. 1 line only, please.")
                        replace=input("")
                        self.data[2]=replace
                        print("File edited.")
                        print("----------")
                    else:
                        self.data[2]=imgEdit()
                        print("----------")
                self.details()
                return

print("FILE EXPLORER!")
print("WARNING: when you exit the program, none of your files will be saved. Sorry :(")
root=node(["root","root","this is the root node."])
root.newNode(["txt","Text File","This is a text file!"])
while True:
    root.details()
    print("----------")
print("")
