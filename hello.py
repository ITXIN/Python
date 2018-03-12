#!/usr/bin/env python
# print 'hello world'

# try:
#     f = open('/Users/avazuholding/Desktop/Python/testPython.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with  open('/Users/avazuholding/Desktop/Python/testPython.txt','rb') as f:
#     for line in f.readlines():
#         print(line.strip())

# with open('/Users/avazuholding/Desktop/Python/testPython.txt','w') as f:
#     f.write('hello,world')
#
# with  open('/Users/avazuholding/Desktop/Python/testPython.txt','rb') as f:
#     for line in f.readlines():
#         print(line.strip())

# from io import StringIO
# f = StringIO('Hello!\n Hi! \nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())




# import os
# print(os.name)
# print(os.uname())


# import pickle
# import json

# d = dict(name='Bob',age=20,score=88)
# json_str = json.dumps(d)
#
# print(json_str)
# print(json.loads(json_str))


# with  open('/Users/avazuholding/Desktop/Python/testPython.txt','wb') as f:
#     pickle.dump(d,f)
#
# with  open('/Users/avazuholding/Desktop/Python/testPython.txt','rb') as f:
#         d = pickle.load(f)
#         print(d)

# class Student(object):
#     """docstring for Student."""
#     def __init__(self, name,age,score):
#         super(Student, self).__init__()
#         self.name = name
#         self.age = age
#         self.score = score
#
# def strudent2dict(std):
#     return{
#     'name':std.name,
#     'age':std.age,
#     'score':std.score,
#     }
# s = Student('Bil',18,100)
# json_str =  json.dumps(s,default=strudent2dict)
# print(json_str)
# print(json.dumps(s,default=lambda obj:obj.__dict__))

# def dict2student(d):
#     return Student(d['name'],d['age'],d['score'])
#
# print(json.loads(json_str,object_hook=dict2student))



# import os
# print('process(%s) start' %os.getpid())
#
# pid = os.fork()
# if pid == 0:
#     print('i am child process (%s) and my parent is %s'%(os.getpid(),os.getppid()))
# else:
#     print('I (%s) just creat a child (%s)'%(os.getpid(),pid))


from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLab = Label(self,text='hello,world')
#         self.helloLab.pack()
#         self.quitButton = Button(self,text='Quit',command=self.quit)
#         self.quitButton.pack()

app = Application()
app.master.title('hello world')
app.mainloop()
