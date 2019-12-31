from __future__ import print_function
import cv2 as cv
import argparse
import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from tkscrolledframe import ScrolledFrame
import json
import random
from tkinter import messagebox
def GUI():
	root=tk.Tk(className='Operation Research')
	root.title('台灣環島規劃')
	# Create a ScrolledFrame widget
	sf = ScrolledFrame(root, width=640, height=480)
	sf.pack(side="top", expand=1, fill="both")
	# Bind the arrow keys and scroll wheel
	sf.bind_arrow_keys(root)
	sf.bind_scroll_wheel(root)

	# Create a frame within the ScrolledFrame
	inner_frame = sf.display_widget(Frame)

	######################### add widgets here, before mainloop()
	title=tk.Label(inner_frame, text='預算 Budget',font=("Courier", 20), fg='dark red')
	title.grid(row = 0,column = 0, columnspan=4)
	title = tk.Spinbox(inner_frame, from_=1, to= 100000000, bg='light gray', fg='purple', font='Arial', wrap=True, width=20 )
	title.grid(row= 0, column= 4, columnspan=4)

	sub_title_1=tk.Label(inner_frame, text='地區',font=("Courier", 16))
	sub_title_1.grid(row = 1,column = 0)
	sub_title_1_1=tk.Label(inner_frame, text='滿意度',font=("Courier", 16))
	sub_title_1_1.grid(row = 1,column = 1)

	sub_title_2=tk.Label(inner_frame, text='地區',font=("Courier", 16))
	sub_title_2.grid(row = 1,column = 2)
	sub_title_2_1=tk.Label(inner_frame, text='滿意度',font=("Courier", 16))
	sub_title_2_1.grid(row = 1,column = 3)

	sub_title_3=tk.Label(inner_frame, text='地區',font=("Courier", 16))
	sub_title_3.grid(row = 1,column = 4)
	sub_title_3_1=tk.Label(inner_frame, text='滿意度',font=("Courier", 16))
	sub_title_3_1.grid(row = 1,column = 5)

	sub_title_4=tk.Label(inner_frame, text='地區',font=("Courier", 16))
	sub_title_4.grid(row = 1,column = 6)
	sub_title_4_1=tk.Label(inner_frame, text='滿意度',font=("Courier", 16))
	sub_title_4_1.grid(row = 1,column = 7)

	###########################################################################
	####################variable ################
	spin_width = 7
	max=10
	min=0
	thisdict = {}
	#######################################
	## 台北
	台北 =tk.Label(inner_frame, text='台北', font=("Courier", 12), fg='blue')
	台北.grid(row = 2,column = 0)
	row_no = 3
	col_no = 0
	bg_colour = 'black'
	fg_colour = 'red'
	大樓101 =tk.Label(inner_frame, text='大樓101')
	大樓101.grid(row = row_no,column = col_no)
	大樓101 = tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	大樓101.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	木柵動物園 =tk.Label(inner_frame, text='木柵動物園')
	木柵動物園.grid(row = row_no,column = col_no)
	木柵動物園 = tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	木柵動物園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	公館遊樂園 =tk.Label(inner_frame, text='公館遊樂園')
	公館遊樂園.grid(row = row_no,column = col_no)
	公館遊樂園 = tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	公館遊樂園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	兒童新樂園 =tk.Label(inner_frame, text='兒童新樂園')
	兒童新樂園.grid(row = row_no,column = col_no)
	兒童新樂園 = tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	兒童新樂園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	陽明山公園=tk.Label(inner_frame, text='陽明山公園')
	陽明山公園.grid(row = row_no,column = col_no)
	陽明山公園= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	陽明山公園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	行天宮=tk.Label(inner_frame, text='行天宮')
	行天宮.grid(row = row_no,column = col_no)
	行天宮= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	行天宮.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 新北
	新北=tk.Label(inner_frame, text='新北', font=("Courier", 12),fg='blue')
	新北.grid(row = row_no,column = 0)
	row_no= row_no+1

	九份=tk.Label(inner_frame, text='九份')
	九份.grid(row = row_no,column = col_no)
	九份= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	九份.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	平溪=tk.Label(inner_frame, text='平溪')
	平溪.grid(row = row_no,column = col_no)
	平溪= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	平溪.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	野柳女王頭=tk.Label(inner_frame, text='野柳女王頭')
	野柳女王頭.grid(row = row_no,column = col_no)
	野柳女王頭= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	野柳女王頭.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	淡水老街=tk.Label(inner_frame, text='淡水老街')
	淡水老街.grid(row = row_no,column = col_no)
	淡水老街= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	淡水老街.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	富貴角燈塔=tk.Label(inner_frame, text='富貴角燈塔')
	富貴角燈塔.grid(row = row_no,column = col_no)
	富貴角燈塔= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	富貴角燈塔.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 基隆
	基隆=tk.Label(inner_frame, text='基隆', font=("Courier", 12),fg='blue')
	基隆.grid(row = row_no,column = 0)
	row_no= row_no+1

	和平島=tk.Label(inner_frame, text='和平島')
	和平島.grid(row = row_no,column = col_no)
	和平島= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	和平島.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	基隆廟口=tk.Label(inner_frame, text='基隆廟口')
	基隆廟口.grid(row = row_no,column = col_no)
	基隆廟口= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	基隆廟口.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 桃園
	桃園=tk.Label(inner_frame, text='桃園', font=("Courier", 12),fg='blue')
	桃園.grid(row = row_no,column = 0)
	row_no= row_no+1

	大溪老街=tk.Label(inner_frame, text='大溪老街')
	大溪老街.grid(row = row_no,column = col_no)
	大溪老街= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	大溪老街.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	可口可樂世界=tk.Label(inner_frame, text='可口可樂世界')
	可口可樂世界.grid(row = row_no,column = col_no)
	可口可樂世界= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	可口可樂世界.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	八德落雨松森林=tk.Label(inner_frame, text='八德落雨松森林')
	八德落雨松森林.grid(row = row_no,column = col_no)
	八德落雨松森林= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	八德落雨松森林.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	竹圍漁港=tk.Label(inner_frame, text='竹圍漁港')
	竹圍漁港.grid(row = row_no,column = col_no)
	竹圍漁港= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	竹圍漁港.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	小木屋鬆餅=tk.Label(inner_frame, text='小木屋鬆餅')
	小木屋鬆餅.grid(row = row_no,column = col_no)
	小木屋鬆餅= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	小木屋鬆餅.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 新竹
	新竹=tk.Label(inner_frame, text='新竹', font=("Courier", 12),fg='blue')
	新竹.grid(row = row_no,column = 0)
	row_no= row_no+1

	青青草原=tk.Label(inner_frame, text='青青草原')
	青青草原.grid(row = row_no,column = col_no)
	青青草原= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	青青草原.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	六福村=tk.Label(inner_frame, text='六福村')
	六福村.grid(row = row_no,column = col_no)
	六福村= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width,)
	六福村.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	################################# END OF COLUMN 1 ###################################################
	col_no = 2
	row_no = 2
	bg_colour = 'black'
	fg_colour = 'yellow'

	## 苗栗
	苗栗=tk.Label(inner_frame, text='苗栗', font=("Courier", 12),fg='blue')
	苗栗.grid(row = 2,column = 2)
	row_no= row_no+1

	三義木雕博物館=tk.Label(inner_frame, text='三義木雕博物館')
	三義木雕博物館.grid(row = row_no,column = col_no)
	三義木雕博物館= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	三義木雕博物館.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	龍騰斷橋=tk.Label(inner_frame, text='龍騰斷橋')
	龍騰斷橋.grid(row = row_no,column = col_no)
	龍騰斷橋= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	龍騰斷橋.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	勝興車站=tk.Label(inner_frame, text='勝興車站')
	勝興車站.grid(row = row_no,column = col_no)
	勝興車站= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	勝興車站.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	客家圓樓=tk.Label(inner_frame, text='客家圓樓')
	客家圓樓.grid(row = row_no,column = col_no)
	客家圓樓= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width )
	客家圓樓.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 臺中
	臺中=tk.Label(inner_frame, text='臺中', font=("Courier", 12),fg='blue')
	臺中.grid(row = row_no,column = 2)
	row_no= row_no+1

	逢甲夜市=tk.Label(inner_frame, text='逢甲夜市')
	逢甲夜市.grid(row = row_no,column = col_no)
	逢甲夜市= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	逢甲夜市.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	審計新村=tk.Label(inner_frame, text='審計新村')
	審計新村.grid(row = row_no,column = col_no)
	審計新村= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	審計新村.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	高美濕地=tk.Label(inner_frame, text='高美濕地')
	高美濕地.grid(row = row_no,column = col_no)
	高美濕地= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	高美濕地.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	宮原眼科=tk.Label(inner_frame, text='宮原眼科')
	宮原眼科.grid(row = row_no,column = col_no)
	宮原眼科= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	宮原眼科.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 彰化
	彰化=tk.Label(inner_frame, text='彰化', font=("Courier", 12),fg='blue')
	彰化.grid(row = row_no,column = 2)
	row_no= row_no+1

	鹿港老街=tk.Label(inner_frame, text='鹿港老街')
	鹿港老街.grid(row = row_no,column = col_no)
	鹿港老街= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	鹿港老街.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	玻璃博物館=tk.Label(inner_frame, text='玻璃博物館')
	玻璃博物館.grid(row = row_no,column = col_no)
	玻璃博物館= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	玻璃博物館.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	田尾公路花園=tk.Label(inner_frame, text='田尾公路花園')
	田尾公路花園.grid(row = row_no,column = col_no)
	田尾公路花園= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	田尾公路花園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 南投
	南投=tk.Label(inner_frame, text='南投', font=("Courier", 12),fg='blue')
	南投.grid(row = row_no,column = 2)
	row_no= row_no+1

	日月潭=tk.Label(inner_frame, text='日月潭')
	日月潭.grid(row = row_no,column = col_no)
	日月潭= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	日月潭.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	集集火車站=tk.Label(inner_frame, text='集集火車站')
	集集火車站.grid(row = row_no,column = col_no)
	集集火車站= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	集集火車站.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	清境農場=tk.Label(inner_frame, text='清境農場')
	清境農場.grid(row = row_no,column = col_no)
	清境農場= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	清境農場.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	妖怪村=tk.Label(inner_frame, text='妖怪村')
	妖怪村.grid(row = row_no,column = col_no)
	妖怪村= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	妖怪村.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	溪頭=tk.Label(inner_frame, text='溪頭')
	溪頭.grid(row = row_no,column = col_no)
	溪頭= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	溪頭.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 雲林
	雲林=tk.Label(inner_frame, text='雲林', font=("Courier", 12),fg='blue')
	雲林.grid(row = row_no,column = 2)
	row_no= row_no+1

	劍湖山=tk.Label(inner_frame, text='劍湖山')
	劍湖山.grid(row = row_no,column = col_no)
	劍湖山= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	劍湖山.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	古坑=tk.Label(inner_frame, text='古坑')
	古坑.grid(row = row_no,column = col_no)
	古坑= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	古坑.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	北港朝天宮=tk.Label(inner_frame, text='北港朝天宮')
	北港朝天宮.grid(row = row_no,column = col_no)
	北港朝天宮= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	北港朝天宮.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	################################# END OF COLUMN 2 ###################################################
	col_no = 4
	row_no = 3
	bg_colour = 'black'
	fg_colour = 'light green'

	## 嘉義
	嘉義=tk.Label(inner_frame, text='嘉義', font=("Courier", 12),fg='blue')
	嘉義.grid(row = 2,column = 4)

	阿里山=tk.Label(inner_frame, text='阿里山')
	阿里山.grid(row = row_no,column = col_no)
	阿里山= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	阿里山.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	嘉義火車站=tk.Label(inner_frame, text='嘉義火車站')
	嘉義火車站.grid(row = row_no,column = col_no)
	嘉義火車站= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	嘉義火車站.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	民雄鬼屋咖啡=tk.Label(inner_frame, text='民雄鬼屋咖啡')
	民雄鬼屋咖啡.grid(row = row_no,column = col_no)
	民雄鬼屋咖啡= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	民雄鬼屋咖啡.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 臺南
	臺南=tk.Label(inner_frame, text='臺南', font=("Courier", 12),fg='blue')
	臺南.grid(row = row_no,column = 4)
	row_no= row_no+1

	赤崁樓=tk.Label(inner_frame, text='赤崁樓')
	赤崁樓.grid(row = row_no,column = col_no)
	赤崁樓= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	赤崁樓.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	六千牛肉湯=tk.Label(inner_frame, text='六千牛肉湯')
	六千牛肉湯.grid(row = row_no,column = col_no)
	六千牛肉湯= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	六千牛肉湯.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	安平觀夕平台=tk.Label(inner_frame, text='安平觀夕平台')
	安平觀夕平台.grid(row = row_no,column = col_no)
	安平觀夕平台= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	安平觀夕平台.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	國華街=tk.Label(inner_frame, text='國華街')
	國華街.grid(row = row_no,column = col_no)
	國華街= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	國華街.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	林百貨=tk.Label(inner_frame, text='林百貨')
	林百貨.grid(row = row_no,column = col_no)
	林百貨= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	林百貨.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	奇美博物館=tk.Label(inner_frame, text='奇美博物館')
	奇美博物館.grid(row = row_no,column = col_no)
	奇美博物館= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	奇美博物館.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	新化老街=tk.Label(inner_frame, text='新化老街')
	新化老街.grid(row = row_no,column = col_no)
	新化老街= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	新化老街.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	國聖燈塔=tk.Label(inner_frame, text='國聖燈塔')
	國聖燈塔.grid(row = row_no,column = col_no)
	國聖燈塔= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	國聖燈塔.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	四草公園=tk.Label(inner_frame, text='四草公園')
	四草公園.grid(row = row_no,column = col_no)
	四草公園= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	四草公園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 高雄
	高雄=tk.Label(inner_frame, text='高雄', font=("Courier", 12),fg='blue')
	高雄.grid(row = row_no,column = 4)
	row_no= row_no+1

	駁二=tk.Label(inner_frame, text='駁二')
	駁二.grid(row = row_no,column = col_no)
	駁二= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	駁二.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	中山大學=tk.Label(inner_frame, text='中山大學')
	中山大學.grid(row = row_no,column = col_no)
	中山大學= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	中山大學.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	興達港=tk.Label(inner_frame, text='興達港')
	興達港.grid(row = row_no,column = col_no)
	興達港= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	興達港.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	草衙道=tk.Label(inner_frame, text='草衙道')
	草衙道.grid(row = row_no,column = col_no)
	草衙道= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	草衙道.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	愛河=tk.Label(inner_frame, text='愛河')
	愛河.grid(row = row_no,column = col_no)
	愛河= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	愛河.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 屏東
	屏東=tk.Label(inner_frame, text='屏東', font=("Courier", 12),fg='blue')
	屏東.grid(row = row_no,column = 4)
	row_no= row_no+1

	墾丁=tk.Label(inner_frame, text='墾丁')
	墾丁.grid(row = row_no,column = col_no)
	墾丁= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	墾丁.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	萬巒豬腳=tk.Label(inner_frame, text='萬巒豬腳')
	萬巒豬腳.grid(row = row_no,column = col_no)
	萬巒豬腳= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	萬巒豬腳.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	萬丹=tk.Label(inner_frame, text='萬丹')
	萬丹.grid(row = row_no,column = col_no)
	萬丹= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	萬丹.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	鵝鑾鼻燈塔=tk.Label(inner_frame, text='鵝鑾鼻燈塔')
	鵝鑾鼻燈塔.grid(row = row_no,column = col_no)
	鵝鑾鼻燈塔= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	鵝鑾鼻燈塔.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	彩虹貨櫃市集=tk.Label(inner_frame, text='彩虹貨櫃市集')
	彩虹貨櫃市集.grid(row = row_no,column = col_no)
	彩虹貨櫃市集= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	彩虹貨櫃市集.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	# ################################# END OF COLUMN 3 ###################################################
	col_no = 6
	row_no = 3
	bg_colour = 'black'
	fg_colour = 'pink'

	## 臺東
	臺東=tk.Label(inner_frame, text='臺東', font=("Courier", 12),fg='blue')
	臺東.grid(row = 2,column = 6)

	三仙台=tk.Label(inner_frame, text='三仙台')
	三仙台.grid(row = row_no,column = col_no)
	三仙台= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	三仙台.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	台東森林公園=tk.Label(inner_frame, text='台東森林公園')
	台東森林公園.grid(row = row_no,column = col_no)
	台東森林公園= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	台東森林公園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1


	藍蜻蜓炸雞=tk.Label(inner_frame, text='藍蜻蜓炸雞')
	藍蜻蜓炸雞.grid(row = row_no,column = col_no)
	藍蜻蜓炸雞= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	藍蜻蜓炸雞.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	星星部落景觀咖啡=tk.Label(inner_frame, text='星星部落景觀咖啡')
	星星部落景觀咖啡.grid(row = row_no,column = col_no)
	星星部落景觀咖啡= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	星星部落景觀咖啡.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	金剛大道=tk.Label(inner_frame, text='金剛大道')
	金剛大道.grid(row = row_no,column = col_no)
	金剛大道= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	金剛大道.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	海濱公園=tk.Label(inner_frame, text='海濱公園')
	海濱公園.grid(row = row_no,column = col_no)
	海濱公園= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	海濱公園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	鐵花村=tk.Label(inner_frame, text='鐵花村')
	鐵花村.grid(row = row_no,column = col_no)
	鐵花村= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	鐵花村.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	原始部落山地美食=tk.Label(inner_frame, text='原始部落山地美食')
	原始部落山地美食.grid(row = row_no,column = col_no)
	原始部落山地美食= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	原始部落山地美食.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	金城武樹=tk.Label(inner_frame, text='金城武樹')
	金城武樹.grid(row = row_no,column = col_no)
	金城武樹= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	金城武樹.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 花蓮
	花蓮=tk.Label(inner_frame, text='花蓮', font=("Courier", 12),fg='blue')
	花蓮.grid(row = row_no,column = 6)
	row_no= row_no+1

	太魯閣國家公園=tk.Label(inner_frame, text='太魯閣國家公園')
	太魯閣國家公園.grid(row = row_no,column = col_no)
	太魯閣國家公園= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	太魯閣國家公園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	瑞穗牧場=tk.Label(inner_frame, text='瑞穗牧場')
	瑞穗牧場.grid(row = row_no,column = col_no)
	瑞穗牧場= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	瑞穗牧場.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	七星潭=tk.Label(inner_frame, text='七星潭')
	七星潭.grid(row = row_no,column = col_no)
	七星潭= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	七星潭.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	清水斷崖=tk.Label(inner_frame, text='清水斷崖')
	清水斷崖.grid(row = row_no,column = col_no)
	清水斷崖= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	清水斷崖.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	慕谷慕魚山=tk.Label(inner_frame, text='慕谷慕魚山')
	慕谷慕魚山.grid(row = row_no,column = col_no)
	慕谷慕魚山= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	慕谷慕魚山.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	大石鼻山步道=tk.Label(inner_frame, text='大石鼻山步道')
	大石鼻山步道.grid(row = row_no,column = col_no)
	大石鼻山步道= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	大石鼻山步道.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	親不知子海空中步道=tk.Label(inner_frame, text='親不知子海空中步道')
	親不知子海空中步道.grid(row = row_no,column = col_no)
	親不知子海空中步道= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	親不知子海空中步道.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	## 宜蘭
	宜蘭=tk.Label(inner_frame, text='宜蘭', font=("Courier", 12),fg='blue')
	宜蘭.grid(row = row_no,column = 6)
	row_no= row_no+1

	蘇澳冷泉個人湯屋=tk.Label(inner_frame, text='蘇澳冷泉個人湯屋')
	蘇澳冷泉個人湯屋.grid(row = row_no,column = col_no)
	蘇澳冷泉個人湯屋= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	蘇澳冷泉個人湯屋.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	幾米公園=tk.Label(inner_frame, text='幾米公園')
	幾米公園.grid(row = row_no,column = col_no)
	幾米公園= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	幾米公園.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	南方澳觀景臺=tk.Label(inner_frame, text='南方澳觀景臺')
	南方澳觀景臺.grid(row = row_no,column = col_no)
	南方澳觀景臺= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	南方澳觀景臺.grid(row= row_no, column=col_no+1)
	row_no= row_no+1

	羅東夜市=tk.Label(inner_frame, text='羅東夜市')
	羅東夜市.grid(row = row_no,column = col_no)
	羅東夜市= tk.Spinbox(inner_frame, from_=min, to= max, bg= bg_colour, fg=fg_colour, font='Arial', wrap=True, width=spin_width)
	羅東夜市.grid(row= row_no, column=col_no+1)
	row_no= row_no+1


	################################# END OF COLUMN 4 ###################################################

	###################################### FUNCTION ####################################################
	def get_value():
		#thisdict = {}
		thisdict["預算"]=title.get()
		thisdict["101大樓"]=大樓101.get()
		thisdict["木柵動物園"] =木柵動物園.get()
		thisdict["公館(台大)遊樂園"] =公館遊樂園.get()
		thisdict["兒童新樂園"] =兒童新樂園.get()
		thisdict["陽明山公園"] =陽明山公園.get()
		thisdict["行天宮拜拜"] =行天宮.get()
		thisdict["九份"] =九份.get()
		thisdict["平溪放天燈"] =平溪.get()
		thisdict["野柳女王頭"] =野柳女王頭.get()
		thisdict["淡水老街"] =淡水老街.get()
		thisdict["富貴角燈塔"] =富貴角燈塔.get()
		thisdict["和平島"] =和平島.get()
		thisdict["基隆廟口"] =基隆廟口.get()
		thisdict["大溪老街"] =大溪老街.get()
		thisdict["可口可樂世界"] =可口可樂世界.get()
		thisdict["八德落雨松森林"] =八德落雨松森林.get()
		thisdict["竹圍漁港"] =竹圍漁港.get()
		thisdict["小木屋鬆餅(中央店)"] =小木屋鬆餅.get()
		thisdict["青青草原"] =青青草原.get()
		thisdict["六福村"] =六福村.get()
		thisdict["三義木雕博物館"] =三義木雕博物館.get()
		thisdict["龍騰斷橋"] =龍騰斷橋.get()
		thisdict["勝興車站"] =勝興車站.get()
		thisdict["客家圓樓"] =客家圓樓.get()
		thisdict["逢甲夜市"] =逢甲夜市.get()
		thisdict["審計新村"] =審計新村.get()
		thisdict["高美濕地"] =高美濕地.get()
		thisdict["宮原眼科"] =宮原眼科.get()
		thisdict["鹿港老街"] =鹿港老街.get()
		thisdict["玻璃博物館"] =玻璃博物館.get()
		thisdict["田尾公路花園"] =田尾公路花園.get()
		thisdict["日月潭"] =日月潭.get()
		thisdict["集集火車站"] =集集火車站.get()
		thisdict["清境農場"] =清境農場.get()
		thisdict["妖怪村"] =妖怪村.get()
		thisdict["溪頭"] =溪頭.get()
		thisdict["劍湖山"] =劍湖山.get()
		thisdict["古坑"] =古坑.get()
		thisdict["北港朝天宮"] =北港朝天宮.get()
		thisdict["阿里山"] =阿里山.get()
		thisdict["嘉義火車站"] =嘉義火車站.get()
		thisdict["民雄鬼屋咖啡"] =民雄鬼屋咖啡.get()
		thisdict["赤崁樓"] =赤崁樓.get()
		thisdict["六千牛肉湯"] =六千牛肉湯.get()
		thisdict["安平觀夕平台"] =安平觀夕平台.get()
		thisdict["國華街"] =國華街.get()
		thisdict["林百貨"] =林百貨.get()
		thisdict["奇美博物館"] =奇美博物館.get()
		thisdict["新化老街"] =新化老街.get()
		thisdict["國聖燈塔"] =國聖燈塔.get()
		thisdict["四草公園"] =四草公園.get()
		thisdict["駁二"] =駁二.get()
		thisdict["中山大學看猴子"] =中山大學.get()
		thisdict["興達港"] =興達港.get()
		thisdict["草衙道"] =草衙道.get()
		thisdict["愛河"] =愛河.get()
		thisdict["墾丁"] =墾丁.get()
		thisdict["萬巒豬腳"] =萬巒豬腳.get()
		thisdict["萬丹"] =萬丹.get()
		thisdict["鵝鑾鼻燈塔"] =鵝鑾鼻燈塔.get()
		thisdict["彩虹貨櫃市集"] =彩虹貨櫃市集.get()
		thisdict["三仙台"] =三仙台.get()
		thisdict["台東森林公園"] =台東森林公園.get()
		thisdict["藍蜻蜓炸雞"] =藍蜻蜓炸雞.get()
		thisdict["星星部落景觀咖啡"] =星星部落景觀咖啡.get()
		thisdict["金剛大道"] =金剛大道.get()
		thisdict["海濱公園"] =海濱公園.get()
		thisdict["鐵花村"] =鐵花村.get()
		thisdict["原始部落山地美食"] =原始部落山地美食.get()
		thisdict["金城武樹"] =金城武樹.get()
		thisdict["太魯閣國家公園"] =太魯閣國家公園.get()
		thisdict["瑞穗牧場"] =瑞穗牧場.get()
		thisdict["七星潭"] =七星潭.get()
		thisdict["清水斷崖"] =清水斷崖.get()
		thisdict["慕谷慕魚山"] =慕谷慕魚山.get()
		thisdict["大石鼻山步道"] =大石鼻山步道.get()
		thisdict["親不知子海空中步道"] =親不知子海空中步道.get()
		thisdict["蘇澳冷泉個人湯屋"] =蘇澳冷泉個人湯屋.get()
		thisdict["幾米公園"] =幾米公園.get()
		thisdict["南方澳觀景臺"] =南方澳觀景臺.get()
		thisdict["羅東夜市"] =羅東夜市.get()
		#print(thisdict)
		with open('data.txt', 'w') as outfile:
			json.dump(thisdict, outfile)
		with open('data.txt') as json_file:
			data = json.load(json_file)
			#print(data)
		root.destroy()
	######################################### message box ###################################
	def messageWindow():
		win = tk.Toplevel()
		win.title('你滿意嗎 ? Are you satisfied ? ')
		tk.Label(win, text="預算："+str(thisdict.get("預算"))+'\n'
		"101大樓:" + str(thisdict.get("大樓101"))+'  '
		"木柵動物園:" + str(thisdict.get("木柵動物園"))+'  '
		"公館遊樂園:" + str(thisdict.get("公館遊樂園"))+'  '
		"兒童新樂園:" + str(thisdict.get("兒童新樂園"))+'  '
		"陽明山公園:" + str(thisdict.get("陽明山公園"))+'  '
		"行天宮:" + str(thisdict.get("行天宮"))+'  '
		"九份:" + str(thisdict.get("九份"))+'\n'
		"平溪:" + str(thisdict.get("平溪"))+'  '
		"野柳女王頭:" + str(thisdict.get("野柳女王頭"))+'  '
		"淡水老街:" + str(thisdict.get("淡水老街"))+'  '
		"富貴角燈塔:" + str(thisdict.get("富貴角燈塔"))+'  '
		"和平島:" + str(thisdict.get("和平島"))+'  '
		"基隆廟口:" + str(thisdict.get("基隆廟口"))+'  '
		"大溪老街:" + str(thisdict.get("大溪老街"))+'\n'
		"可口可樂世界:" + str(thisdict.get("可口可樂世界"))+'  '
		"八德落雨松森林:" + str(thisdict.get("八德落雨松森林"))+'  '
		"竹圍漁港:" + str(thisdict.get("竹圍漁港"))+'  '
		"小木屋鬆餅:" + str(thisdict.get("小木屋鬆餅"))+'  '
		"青青草原:" + str(thisdict.get("青青草原"))+'  '
		"六福村:" + str(thisdict.get("六福村"))+'  '
		"三義木雕博物館:" + str(thisdict.get("三義木雕博物館"))+'\n'
		"龍騰斷橋:" + str(thisdict.get("龍騰斷橋"))+'  '
		"勝興車站:" + str(thisdict.get("勝興車站"))+'  '
		"客家圓樓:" + str(thisdict.get("客家圓樓"))+'  '
		"逢甲夜市:" + str(thisdict.get("逢甲夜市"))+'  '
		"審計新村:" + str(thisdict.get("審計新村"))+'  '
		"高美濕地:" + str(thisdict.get("高美濕地"))+'  '
		"宮原眼科:" + str(thisdict.get("宮原眼科"))+'\n'
		"鹿港老街:" + str(thisdict.get("鹿港老街"))+'  '
		"玻璃博物館:" + str(thisdict.get("玻璃博物館"))+'  '
		"田尾公路花園:" + str(thisdict.get("田尾公路花園"))+'  '
		"日月潭:" + str(thisdict.get("日月潭"))+'  '
		"集集火車站:" + str(thisdict.get("集集火車站"))+'  '
		"清境農場:" + str(thisdict.get("清境農場"))+'  '
		"妖怪村:" + str(thisdict.get("妖怪村"))+'\n'
		"溪頭:" + str(thisdict.get("溪頭"))+'  '
		"劍湖山:" + str(thisdict.get("劍湖山"))+'  '
		"古坑:" + str(thisdict.get("古坑"))+'  '
		"北港朝天宮:" + str(thisdict.get("北港朝天宮"))+'  '
		"阿里山:" + str(thisdict.get("阿里山"))+'  '
		"嘉義火車站:" + str(thisdict.get("嘉義火車站"))+'  '
		"民雄鬼屋咖啡:" + str(thisdict.get("民雄鬼屋咖啡"))+'\n'
		"赤崁樓:" + str(thisdict.get("赤崁樓"))+'  '
		"六千牛肉湯:" + str(thisdict.get("六千牛肉湯"))+'  '
		"安平觀夕平台:" + str(thisdict.get("安平觀夕平台"))+' '
		"國華街:" + str(thisdict.get("國華街"))+'  '
		"林百貨:" + str(thisdict.get("林百貨"))+'  '
		"奇美博物館:" + str(thisdict.get("奇美博物館"))+'  '
		"新化老街:" + str(thisdict.get("新化老街"))+'\n'
		"國聖燈塔:" + str(thisdict.get("國聖燈塔"))+'  '
		"四草公園:" + str(thisdict.get("四草公園"))+'  '
		"駁二:" + str(thisdict.get("駁二"))+'  '
		"中山大學:" + str(thisdict.get("中山大學"))+'  '
		"興達港:" + str(thisdict.get("興達港"))+'  '
		"草衙道:" + str(thisdict.get("草衙道"))+'  '
		"愛河:" + str(thisdict.get("愛河"))+'\n'
		"墾丁:" + str(thisdict.get("墾丁"))+'  '
		"萬巒豬腳:" + str(thisdict.get("萬巒豬腳"))+'  '
		"萬丹:" + str(thisdict.get("萬丹"))+'  '
		"鵝鑾鼻燈塔:" + str(thisdict.get("鵝鑾鼻燈塔"))+'  '
		"彩虹貨櫃市集:" + str(thisdict.get("彩虹貨櫃市集"))+'  '
		"三仙台:" + str(thisdict.get("三仙台"))+'  '
		"台東森林公園:" + str(thisdict.get("台東森林公園"))+'\n'
		"藍蜻蜓炸雞:" + str(thisdict.get("藍蜻蜓炸雞"))+'  '
		"星星部落景觀咖啡:" + str(thisdict.get("星星部落景觀咖啡"))+'  '
		"金剛大道:" + str(thisdict.get("金剛大道"))+'  '
		"海濱公園:" + str(thisdict.get("海濱公園"))+'  '
		"鐵花村:" + str(thisdict.get("鐵花村"))+'  '
		"原始部落山地美食:" + str(thisdict.get("原始部落山地美食"))+'  '
		"金城武樹:" + str(thisdict.get("金城武樹"))+'\n'
		"太魯閣國家公園:" + str(thisdict.get("太魯閣國家公園"))+'  '
		"瑞穗牧場:" + str(thisdict.get("瑞穗牧場"))+'  '
		"七星潭':" + str(thisdict.get("七星潭'"))+'  '
		"清水斷崖:" + str(thisdict.get("清水斷崖"))+'  '
		"慕谷慕魚山:" + str(thisdict.get("慕谷慕魚山"))+'  '
		"大石鼻山步道:" + str(thisdict.get("大石鼻山步道"))+'  '
		"親不知子海空中步道:" + str(thisdict.get("親不知子海空中步道"))+'\n'
		"蘇澳冷泉個人湯屋:" + str(thisdict.get("蘇澳冷泉個人湯屋"))+'  '
		"幾米公園:" + str(thisdict.get("幾米公園"))+'  '
		"南方澳觀景臺:" + str(thisdict.get("南方澳觀景臺"))+'  '
		"羅東夜市:" + str(thisdict.get("羅東夜市"))+'  '
		).pack()
		tk.Button(win, text='Yes', command=root.destroy).pack()
		tk.Button(win, text='Retry', command=win.destroy).pack()
	########################### random ######################################################
	def random_no():
		#thisdict = {}
		thisdict["預算"]=random.randrange (1,100000000,1)
		thisdict["101大樓"]=random.randrange (0,11,1)
		thisdict["木柵動物園"] =random.randrange (0,11,1)
		thisdict["公館(台大)遊樂園"] =random.randrange (0,11,1)
		thisdict["兒童新樂園"] =random.randrange (0,11,1)
		thisdict["陽明山公園"] =random.randrange (0,11,1)
		thisdict["行天宮拜拜"] =random.randrange (0,11,1)
		thisdict["九份"] =random.randrange (0,11,1)
		thisdict["平溪放天燈"] =random.randrange (0,11,1)
		thisdict["野柳女王頭"] =random.randrange (0,11,1)
		thisdict["淡水老街"] =random.randrange (0,11,1)
		thisdict["富貴角燈塔"] =random.randrange (0,11,1)
		thisdict["和平島"] =random.randrange (0,11,1)
		thisdict["基隆廟口"] =random.randrange (0,11,1)
		thisdict["大溪老街"] =random.randrange (0,11,1)
		thisdict["可口可樂世界"] =random.randrange (0,11,1)
		thisdict["八德落雨松森林"] =random.randrange (0,11,1)
		thisdict["竹圍漁港"] =random.randrange (0,11,1)
		thisdict["小木屋鬆餅(中央店)"] =random.randrange (0,11,1)
		thisdict["青青草原"] =random.randrange (0,11,1)
		thisdict["六福村"] =random.randrange (0,11,1)
		thisdict["三義木雕博物館"] =random.randrange (0,11,1)
		thisdict["龍騰斷橋"] =random.randrange (0,11,1)
		thisdict["勝興車站"] =random.randrange (0,11,1)
		thisdict["客家圓樓"] =random.randrange (0,11,1)
		thisdict["逢甲夜市"] =random.randrange (0,11,1)
		thisdict["審計新村"] =random.randrange (0,11,1)
		thisdict["高美濕地"] =random.randrange (0,11,1)
		thisdict["宮原眼科"] =random.randrange (0,11,1)
		thisdict["鹿港老街"] =random.randrange (0,11,1)
		thisdict["玻璃博物館"] =random.randrange (0,11,1)
		thisdict["田尾公路花園"] =random.randrange (0,11,1)
		thisdict["日月潭"] =random.randrange (0,11,1)
		thisdict["集集火車站"] =random.randrange (0,11,1)
		thisdict["清境農場"] =random.randrange (0,11,1)
		thisdict["妖怪村"] =random.randrange (0,11,1)
		thisdict["溪頭"] =random.randrange (0,11,1)
		thisdict["劍湖山"] =random.randrange (0,11,1)
		thisdict["古坑"] =random.randrange (0,11,1)
		thisdict["北港朝天宮"] =random.randrange (0,11,1)
		thisdict["阿里山"] =random.randrange (0,11,1)
		thisdict["嘉義火車站"] =random.randrange (0,11,1)
		thisdict["民雄鬼屋咖啡"] =random.randrange (0,11,1)
		thisdict["赤崁樓"] =random.randrange (0,11,1)
		thisdict["六千牛肉湯"] =random.randrange (0,11,1)
		thisdict["安平觀夕平台"] =random.randrange (0,11,1)
		thisdict["國華街"] =random.randrange (0,11,1)
		thisdict["林百貨"] =random.randrange (0,11,1)
		thisdict["奇美博物館"] =random.randrange (0,11,1)
		thisdict["新化老街"] =random.randrange (0,11,1)
		thisdict["國聖燈塔"] =random.randrange (0,11,1)
		thisdict["四草公園"] =random.randrange (0,11,1)
		thisdict["駁二"] =random.randrange (0,11,1)
		thisdict["中山大學看猴子"] =random.randrange (0,11,1)
		thisdict["興達港"] =random.randrange (0,11,1)
		thisdict["草衙道"] =random.randrange (0,11,1)
		thisdict["愛河"] =random.randrange (0,11,1)
		thisdict["墾丁"] =random.randrange (0,11,1)
		thisdict["萬巒豬腳"] =random.randrange (0,11,1)
		thisdict["萬丹"] =random.randrange (0,11,1)
		thisdict["鵝鑾鼻燈塔"] =random.randrange (0,11,1)
		thisdict["彩虹貨櫃市集"] =random.randrange (0,11,1)
		thisdict["三仙台"] =random.randrange (0,11,1)
		thisdict["台東森林公園"] =random.randrange (0,11,1)
		thisdict["藍蜻蜓炸雞"] =random.randrange (0,11,1)
		thisdict["星星部落景觀咖啡"] =random.randrange (0,11,1)
		thisdict["金剛大道"] =random.randrange (0,11,1)
		thisdict["海濱公園"] =random.randrange (0,11,1)
		thisdict["鐵花村"] =random.randrange (0,11,1)
		thisdict["原始部落山地美食"] =random.randrange (0,11,1)
		thisdict["金城武樹"] =random.randrange (0,11,1)
		thisdict["太魯閣國家公園"] =random.randrange (0,11,1)
		thisdict["瑞穗牧場"] =random.randrange (0,11,1)
		thisdict["七星潭"] =random.randrange (0,11,1)
		thisdict["清水斷崖"] =random.randrange (0,11,1)
		thisdict["慕谷慕魚山"] =random.randrange (0,11,1)
		thisdict["大石鼻山步道"] =random.randrange (0,11,1)
		thisdict["親不知子海空中步道"] =random.randrange (0,11,1)
		thisdict["蘇澳冷泉個人湯屋"] =random.randrange (0,11,1)
		thisdict["幾米公園"] =random.randrange (0,11,1)
		thisdict["南方澳觀景臺"] =random.randrange (0,11,1)
		thisdict["羅東夜市"] =random.randrange (0,11,1)
		#print(thisdict)
		# for x in thisdict:
		# 	print("\""+ x +':'+ "\"" + '+str(thisdict.get("' + x + "\"" + '))')
		with open('data.txt', 'w') as outfile:
			json.dump(thisdict, outfile)
		messageWindow()

	    #root.destroy()
	#########################################################################################
	##################################### BUTTON ################################################
	done_button = tk.Button(inner_frame, text='Done', width=25, command=get_value)
	done_button.grid(row= 40, column=1,columnspan=2)
	cancel_button = tk.Button(inner_frame, text='Cancel', width=25, command=root.destroy)
	cancel_button.grid(row= 40, column=3,columnspan=2)
	random_button = tk.Button(inner_frame, text='Random', width=25, command=random_no)
	random_button.grid(row= 40, column=5,columnspan=2)

	root.mainloop()