# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import pyperclip

class CreateTable(QTableWidget): # QTableWidget
    def __init__(self, row, col): # Index, ColumnHeaders
        super(CreateTable, self).__init__()
        self.setRowCount(row)
        self.setColumnCount(col)
        stylesheet_1 = "::section{Background-color:rgb(255,236,236)}"
        stylesheet_2 = "::section{Background-color:rgb(236,247,255)}"
        self.horizontalHeader().setStyleSheet(stylesheet_1)
        self.verticalHeader().setStyleSheet(stylesheet_2)
        self.horizontalHeader().setDefaultSectionSize(85)
        self.verticalHeader().setDefaultSectionSize(10)
        self.main_stock_no = "581980"

        self.xyxy = [0, 0, 0, 0]
        self.x = ""
        self.y = ""
        self.xy = [0, 0]
        self.xx= [0, 0]
        self.yy = [0, 0]
        self.usedrange = [0, 0]
        self.var = {} # 일반적인변수를 공통으로 사용가능하도록 만들기위해
        self.cliptext = [] # undo가가능하도록 하는것
        self.history = []
        self.old_cell = ""
        self.max_x = 1
        self.max_y = 1

        # 자동으로 실행되는 것
        self.itemChanged.connect(self.event_itemchanged)
        self.cellChanged.connect(self.event_cell_changed)
        self.itemSelectionChanged.connect(self.event_itemselectionchanged)

        # self.header().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.horizontalHeader().customContextMenuRequested.connect(self.menu_header_y)
        self.verticalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.verticalHeader().customContextMenuRequested.connect(self.menu_header_x)

    def menu_header_x(self, pos):
        global_pos = self.mapToGlobal(pos)
        menu = QMenu()
        menu.addAction("verticalHeaderMenu item")
        selectedItem = menu.exec_(global_pos)
        if selectedItem:
            print("selected: ", selectedItem)
        #column = self.verticalHeader().logicalIndexAt(pos)
        print(self.verticalHeader().selectedIndexes())
        #x1, y1, x2, y2 = self.read_range_select()[0]

    def menu_header_y(self, pos):
        global_pos = self.mapToGlobal(pos)
        menu = QMenu()
        menu.addAction("horizontalHeaderMenu item")
        selectedItem = menu.exec_(global_pos)
        if selectedItem:
            print("selected: ", selectedItem)
        print(self.horizontalHeader().selectedIndexes())
        #x1, y1, x2, y2 = self.read_range_select()[0]

    def contextMenuEvent(self, event):
        # 메뉴를 만드는 것
        #print(event.pos())
        #print(self.mapToGlobal(event.pos()))

        menu = QMenu(self)
        copy_action = menu.addAction("복사하기")
        quit_action = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_action:
            qApp.quit()
        elif action == copy_action:
            print("copy...")

    def write_cell_combo(self, xy, combo_list):
        # tablewidget은 셀에 객체의 형식으로 넣어야 들어간다
        # 즉, 값, 색깔, 위치등을 지정해 주어야 들어가는 것이다
        self.check_used_range(xy)
        combo = QComboBox()
        for one in combo_list:
            combo.addItem(str(one))

        self.setCellWidget(xy[0], xy[1], combo)

    def check_max_xy(self, x, y):
        #usedrange를 확정하기위해 사용되는것
        if x !="":
            self.max_x = max(x, self.max_x)
        if y !="":
            self.max_y = max(y, self.max_y)


    def event_cell_changed(self, x: int, y: int) -> None:
        # 이동된후의 값을 나타낸다
        self.add_history(self.old_cell)
        self.check_max_xy(x, y)

        try:
            input_text = self.item(x, y).text()

            print("입력값이 변경되었네요", (x, y), input_text)
            #셀에 입력이 "="으로 입력되었을때 적용하는것
            if input_text == "=1":
                self.write_cell_combo([2, 2], ["abc", "def", "xyz"])
            elif input_text == "=2":
                print("=2 를 입력했네요")
                self.write_cell_combo([3, 3], ["111abc", "222def", "333xyz"])
        except:
            pass

    def event_itemchanged(self, item) -> None:
        print(f"Item Changed ({item.row()}, {item.column()})")

        # 이동된후의 값을 나타낸다
        x = self.currentRow()
        y = self.currentColumn()
        self.add_history(self.old_cell)
        self.check_max_xy(x, y)
        try:
            input_text = self.item(x, y).text()

            #print(input_text)
            #셀에 입력이 "="으로 입력되었을때 적용하는것
            if input_text[0:2] == "=1":
                self.write_cell_combo(2, 2, ["abc", "def", "xyz"])
            elif input_text[0:2] == "=2":
                self.write_cell_combo(3, 3, ["111abc", "222def", "333xyz"])
        except:
            pass

    def event_itemselectionchanged(self ):

        #print("item_selection_changed")
        # 이동된후의 값을 나타낸다
        x = self.currentRow()
        y = self.currentColumn()
        cells = self.read_range_attribute([x, y])
        self.old_cell = {"type": "change", "range": [x, y], "cells": cells}
        self.check_max_xy(x, y)
        return self.old_cell


    def add_history(self, change):
        self.history.append(change)

    def keyPressEvent(self, event):
        #키보드를 누르면 실행되는 것
        super().keyPressEvent(event)
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.press_enter_key()
        elif event.key() == Qt.Key_Delete:
            self.press_delete_key()
        elif event.key() == Qt.Key_A and (event.modifiers() & Qt.ControlModifier):
            self.SelectAll()
        elif event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
            self.press_copy_key()
        elif event.key() == Qt.Key_V and (event.modifiers() & Qt.ControlModifier):
            self.press_paste_key()
        elif event.key() == Qt.Key_X and (event.modifiers() & Qt.ControlModifier):
            self.paste_cut_key(event)
        elif event.key() == Qt.Key_Z and (event.modifiers() & Qt.ControlModifier):
            self.undo()

    def undo(self):
        if len(self.history):
            action = self.history.pop()
            xyxy = action["range"]
            value_s = action["cells"]
            print("undo 실행", action["type"], xyxy, value_s)

            if action["type"] == "change" or action["type"] == "delete":
               self.write_range_attribute(action)

            elif action["type"] == "delete_rows":
                self.add_rows(xyxy)
                for row, col, attribute in value_s:
                    self.write_cell_value([row, col], attribute["value"])

            elif action["type"] == "delete_cols":
                self.add_cols(xyxy)
                for row, col, attribute in value_s:
                    self.write_cell_value([row, col], attribute["value"])

            elif action["type"] == "add_rows":
                self.del_rows(xyxy)

            elif action["type"] == "add_cols":
                self.del_cols(xyxy)
            else:
                return

    def write_range_attribute(self, action):
        action_type = action["type"]
        xyxy = action["range"]
        value_s = action["cells"]
        for one_list in value_s:
            for x, y, value in one_list:
                self.setItem(x, y, QTableWidgetItem(str(value)))

    def read_range_attribute(self, xyxy):
        # 선택한영역의 주소와 속성을 하나씩 저장하는 것이다
        # 결과물 = [[x,y,값]....]
        result = []
        if len(xyxy) == 2: xyxy = [xyxy[0], xyxy[1], xyxy[0], xyxy[1]]
        for x in range(xyxy[0], xyxy[2]):
            for y in range(xyxy[1], xyxy[3]):
                result.append([x, y, self.item(x, y).text()])
        return result

    def cell_changed(self):
        # 이동된후의 값을 나타낸다
        x = self.currentRow()
        y = self.currentColumn()
        self.add_history(self.old_cell)
        self.check_max_xy(x, y)
        print(self.max_x, self.max_y)

    def press_cut_key(self):
        self.press_copy_key()
        self.press_delete_key()

    def press_paste_key(self):
        input_text = pyperclip.paste()
        result = []
        semi_list = input_text.split("\n")
        for one_text in semi_list:
            temp = one_text.split("\t")
            result.append(temp)

        xyxy = self.read_selected_address()
        self.write_range_value(result, [xyxy[0][0], xyxy[0][1]])

    def press_copy_key(self):
        self.cliptext = []
        xyxy = self.read_selected_address()[0]
        print(xyxy)
        result = ""
        if len(xyxy)==2:
            xyxy = [xyxy[0], xyxy[1], xyxy[0], xyxy[1]]

        for x in range(xyxy[0], xyxy[2]+1):
            temp = []
            for y in range(xyxy[1], xyxy[3]+1):
                item_temp = self.item(x, y)
                if item_temp is not None:
                    value = item_temp.text()
                else:
                    value = ""
                temp.append(value)
                result = result+value +"\t"
            result = result[:-2]+"\n"
            self.cliptext.append(temp)
        print(self.cliptext)
        pyperclip.copy(result[:-2])
        return result

    def press_delete_key(self):
        print("delete")
        xyxy_s = self.read_select_address()
        cells = []
        for xyxy in xyxy_s:
            cell = self.read_range_attribute(xyxy)
            cells.append(cell)
        self.delete_range_select(xyxy_s)
        self.add_history({"type": "delete", "range": xyxy_s, "cells": cells})

    def delete_range_select(self, many_range):
        # selected ranges
        print("delete action")
        for xyxy in many_range:
            for x in range(xyxy[0], xyxy[2]+1):
                for y in range(xyxy[1], xyxy[3]+1):
                    self.setItem(x, y, QTableWidgetItem(""))

    def press_enter_key(self):
        current = self.currentIndex()
        nextIndex = current.sibling(current.row() + 1, current.column())
        self.setItem(current.row() + 1, current.column(), QTableWidgetItem(str("")))
        if nextIndex.isValid():
            self.setCurrentCell(current.row() + 1, current.column())
            self.edit(nextIndex)

    def add_cols(self, xyxy):
        xyxy = self.read_select_address()[0]
        for x in (xyxy[0], xyxy[2]):
            self.InsertCols(x)
        self.add_history({"type": "add_cols", "range": [xyxy[0], 0, xyxy[2], 0], "cells": ""})

    def add_rows(self, xyxy):
        xyxy = self.read_select_address()[0]
        for y in range(xyxy[1], xyxy[3]):
            self.insertRow(y)
        self.add_history({"type": "add_rows", "range": [0, xyxy[1], 0, xyxy[3]], "cells": ""})

    def delete_cols(self, xyxy):
        xyxy = self.read_select_address()[0]
        cells = self.read_xx_attribute(xyxy)
        for y in range(xyxy[2], xyxy[0], -1):
            self.removeColumn(y)
        self.add_history({"type": "delete_cols", "range": [xyxy[0], 0, xyxy[2], 0], "cells": cells})

    def delete_rows(self, xyxy):
        xyxy = self.read_select_address()[0]
        cells = self.read_yy_attribute(xyxy)
        for y in range(xyxy[3], xyxy[1], -1):
            self.removeRow(y)
        self.add_history({"type": "delete_rows", "range": [0, xyxy[1], 0, xyxy[3]], "cells": cells})

    def read_yy_attribute(self, xyxy):
        # 세로를 삭제하였을때 값과 속성을 하나씩 저장하는 것이다
        old_xyxy = self.read_select_address()[0]
        end_xy = self.usedrange
        xyxy = [0, old_xyxy[1], end_xy[0], old_xyxy[3]]
        result = []
        for x in range(xyxy[0], xyxy[2]):
            temp = {}
            for y in range(xyxy[1], xyxy[3]):
                # 추가로 속성을 넣을수있도록 만든것이다
                temp["x"] = x
                temp["y"] = y
                temp["value"] = self.item(x, y).text()
            result.append(temp)
        return result

    def read_xx_attribute(self, xyxy):
        # 가로를 삭제하였을때 값과 속성을 하나씩 저장하는 것이다
        old_xyxy = self.read_select_address()[0]
        end_xy = self.usedrange
        xyxy = [old_xyxy[0], 0, old_xyxy[2], end_xy[1]]
        result = []
        for x in range(xyxy[0], xyxy[2]):
            temp = {}
            for y in range(xyxy[1], xyxy[3]):
                # 추가로 속성을 넣을수있도록 만든것이다
                temp["x"] = x
                temp["y"] = y
                temp["value"] = self.item(x, y).text()
            result.append(temp)
        return result

    def check_used_range(self, xyxy):
        if len(xyxy) == 2:
            self.usedrange[0] = max(xyxy[0], self.usedrange[0])
            self.usedrange[1] = max(xyxy[0], self.usedrange[1])
        else:
            self.usedrange[0] = max(xyxy[0], self.usedrange[0], self.usedrange[2])
            self.usedrange[1] = max(xyxy[0], self.usedrange[1], self.usedrange[3])

    def write_cell_value(self, xy, input_text):
        self.setItem(xy[0], xy[1], QTableWidgetItem(str(input_text)))
        self.check_max_xy(xy[0], xy[1])

    def write_range_value(self, input_list, xy=[1,1]):
        # tablewidget은 셀에 객체의 형식으로 넣어야 들어간다
        # 즉, 값, 색깔, 위치등을 지정해 주어야 들어가는 것이다
        self.check_used_range(xy)
        if type([]) != type(input_list[0]):
            input_list = [input_list]

        for x in range(len(input_list)):
            for y in range(len(input_list[0])):
                self.setItem(xy[0]+x, xy[1]+y, QTableWidgetItem(str(input_list[x][y])))
        self.check_max_xy(xy[0]+len(input_list), xy[1]+len(input_list[0]))

    def write_range_1dvalue(self, input_list):
        for y in range(len(input_list)):
                self.setItem(1, y, QTableWidgetItem(str(input_list[y])))

    def read_selected_address(self):
        result = []
        range_s = self.selectedRanges()
        for range in range_s:
            result.append([range.topRow(), range.leftColumn(), range.bottomRow(), range.rightColumn()])
        return result

    def read_range_value(self, xyxy):
        result = []
        if len(xyxy) == 2:
            xyxy = [xyxy[0], xyxy[1], xyxy[0], xyxy[1]]
        elif len(xyxy) == 4:
            pass

        for x in range(xyxy[0], xyxy[2]):
            temp = []
            for y in range(xyxy[1], xyxy[3]):
                try:
                    value = self.item(x, y).text()
                except:
                    value = ""
                print(x, y, value)
                # if value == None: value = ""
                temp.append(value)
            result.append(temp)
        self.max_x = max(xyxy[2], self.max_x)
        self.max_y = max(xyxy[3], self.max_y)
        # print(self.max_x, self.max_y)
        return result

    def read_cell_value(self, xy):
        result = self.item(xy[0], xy[1]).text()
        return result

    def sort_by_no(self, x):
        # x 번재 자리에 column 삽입
        self.sortItems(x, Qt.DescendingOrder)

    def read_select_address(self):
        # selected ranges
        # 선택한 여러영역의 좌표를 돌려준다
        # [[1,2,3,4],[5,6,7,8],[9,10,11,12],]
        selected_range = self.selectedRanges()
        result = []
        for idx, sel in enumerate(selected_range):
            temp = [sel.topRow(), sel.leftColumn(), sel.bottomRow(), sel.rightColumn()]
            result.append(temp)
        return result

    def read_range_select(self):
        # selected ranges
        # 선택한 여러영역의 좌표를 돌려준다
        # [[1,2,3,4],[5,6,7,8],[9,10,11,12],]
        selected_range = self.selectedRanges()
        result =  []
        for idx, sel in enumerate(selected_range):
            temp = [sel.topRow(), sel.leftColumn(), sel.bottomRow(), sel.rightColumn()]
            result.append(temp)
        return result

    def write_cell_checkbox(self, xy, value = 1):
        # tablewidget은 셀에 객체의 형식으로 넣어야 들어간다
        # 즉, 값, 색깔, 위치등을 지정해 주어야 들어가는 것이다
        self.check_used_range(xy)
        cbox = QCheckBox("I have a Cat")
        cbox.setChecked(int(value))
        self.setCellWidget(xy[0], xy[1], cbox)

    def write_cell_button(self, xy, action, caption = "abc"):
        # tablewidget은 셀에 객체의 형식으로 넣어야 들어간다
        # 즉, 값, 색깔, 위치등을 지정해 주어야 들어가는 것이다
        btnRun = QPushButton(caption, self)  # 버튼 텍스트
        btnRun.clicked.connect(action)
        self.setCellWidget(xy[0], xy[1], btnRun)

    def delete_cell_attribute(self, xy):
        # tablewidget은 셀에 객체의 형식으로 넣어야 들어간다
        # 즉, 값, 색깔, 위치등을 지정해 주어야 들어가는 것이다
        self.removeCellWidget(xy[0], xy[1])

    def write_cell_progressbar(self, xy, value=50):
        # tablewidget은 셀에 객체의 형식으로 넣어야 들어간다
        # 즉, 값, 색깔, 위치등을 지정해 주어야 들어가는 것이다
        self.check_used_range(xy)

        combo = QProgressBar()
        combo.setValue(int(value))
        self.setCellWidget(xy[0], xy[1], combo)