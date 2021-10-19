#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import tkinter.messagebox as mb

#メインウインドウを作成
root = tkinter.Tk()
root.title(u"O-Idialog") #メインウィンドウのタイトルを設定
root.geometry("400x200") #メインウインドウの大きさをきめる


def SendValue(event):
    value = EditBox.get() #テキストボックスの中身を取得する
    #EditBox.delete(0,tkinter.END) #テキストボックスの中身を削除する
    mb.showinfo("output",value) #ダイアログを表示する
    

#ラベル作成
Editlabel = tkinter.Label(text="文字列を挿入してください",font=10)
Editlabel.pack()



#テキストボックス作成
EditBox = tkinter.Entry(width=50,)
EditBox.insert(tkinter.END,"表示する文字列")
EditBox.place(x=50,y=70)#場所を指定する


#ボタン作成
EditButton = tkinter.Button(text="submit",width=30,bg="#ff0000")
EditButton.bind("<Button-1>",SendValue)
EditButton.place(x=90,y=130)


#メインループを開始
root.mainloop()
