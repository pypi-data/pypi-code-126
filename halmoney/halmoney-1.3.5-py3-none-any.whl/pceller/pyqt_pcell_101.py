# -*- coding: utf-8 -*-
from halmoney import pcell, youtil, scolor, pynal, anydb, jfinder, mygrid
from PyQt5.QtWidgets import *
import sys
import subprocess
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.excel = pcell.pcell()
        self.yt = youtil.youtil()
        self.color = scolor.scolor()
        self.jf = jfinder.jfinder()
        self.nal = pynal.pynal()
        self.ab = anydb.anydb()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon('halmoney_logo.jpg'))
        self.resize(600, 700)
        self.setWindowTitle("Python 엑셀 Macro - pceller")

        self.params = self.yt.read_object_method_argument_from_object(self.excel)
        self.module_manual = self.yt.read_object_methodname_help(self.excel)

        self.new_menu = []
        self.p1_txt1 = ""
        self.p2_txt1 = ""
        self.p3_txt1 = ""
        self.var = {}
        self.menu3_dic = ""
        self.menu2_dic = ""
        self.menu1_dic = ""
        self.menu = {}
        self.make_menu_dic()
        self.btn_name_list = ["btn_c_1", "btn_c_2", "btn_c_3", "btn_c_4", "btn_c_5", "btn_c_6", "btn_c_7"]
        self.create_menubar()
        self.check_user_folder()
        self.check_volunteer_folder()

        tabs = QTabWidget()
        tabs.addTab(self.tab_page_1(), '내부 실행용')
        tabs.addTab(self.tab_page_2(), '외부 화일 실행용')
        tabs.addTab(self.tab_page_3(), '추천 화일')
        self.setCentralWidget(tabs)
        self.show()

    def check_user_folder(self):
        #user_folder가 있는지 확인
        file_namesss = self.yt.read_filename_in_folder_all(".")
        if "user_code" in file_namesss:
            pass
        else:
            self.yt.make_folder("user_code")

    def check_volunteer_folder(self):
        #user_folder가 있는지 확인
        file_namesss = self.yt.read_filename_in_folder_all(".")
        if "volunteer_code" in file_namesss:
            pass
        else:
            self.yt.make_folder("volunteer_code")

    def show_manual_1(self):
        #내부실행용 사용법
        message = """총 3단계로 이루어진부분입니다
        - 1단계 : 대분류
        - 2단계 : 중분류
        - 3단계 : 소분류 (2단계로 끝나는 없는 경우는 '없음'으로 나타난다)
        - 입력폼에 변수값들을 입력한다
        - 실행 버튼을 누른다
        
        오른쪽 아랫부분의 입력폼은 변수들을 넣는 부분으로
        입력필요하고 된 부분은 꼭 입력을 해야 실행이 되는 부분입니다
        다, 입력후 '실행'버튼을 누르면 실행이 됩니다
        - 기본값 : 입력변수의 기본 설정 값으로 들어가는 것
        - sheet_name의 기본값 : 현재 활성화된 시트
        
        """
        self.p1_txt1.setPlainText(message.replace("        ", ""))

    def show_manual_2(self):
        # 외부화일 실행용 사용법
        message = """본인이 직접 만든 Python화일을 실행시키는 부분입니다
        - 이 실행화일이 있는 폴더의 'user_code'폴더안에 저장하면 나타납니다
        - 선택한후 '실행'버튼을 누르면 실행이 됩니다
        """
        self.p2_txt1.setPlainText(message.replace("        ", ""))

    def show_manual_3(self):
        # 외부화일 실행용 사용법
        message = """본인이 직접 만든 Python화일을 실행시키는 부분입니다
        - 이 실행화일이 있는 폴더의 'user_code'폴더안에 저장하면 나타납니다
        - 선택한후 '실행'버튼을 누르면 실행이 됩니다
        """
        self.p3_txt1.setPlainText(message.replace("        ", ""))

    def show_manual_5(self):
        # logo의 의미
        #snbs(생노병사), losd(life, old, sick, die)
        message = """로고는 생노병사를 나름대로 해석을 해서 만든것이다
        - 없음과 새로움의 시작을 원으로 표현을 하였으며
        - 이마의 주름으로 나이들어가는 것을 표현하였고
        - 병들면 무엇인가 검정으로 변하는 많은 세포들을 으미하고
        - 죽은은 옆으로 누워있는 모습으로 나타냈고
        - 위아래의 대각선은 오른쪽에서 아래로 변경한다는뜻으로 화살표를 넣은것이다
        """
        self.p1_txt1.setPlainText(message.replace("        ", ""))

    def show_manual_4(self):
        # 누가 만들었나요?
        message = """
        작성자 : 박상진
        www.halmoney.com
        Date : 2022-04-11
        Version : 1.00
        """
        self.p1_txt1.setPlainText(message.replace("        ", ""))

    def create_menubar(self):

        menubar = self.menuBar()

        menu_1 = menubar.addMenu("사용법")

        menu_1_1 = QAction('내부실행용', self)
        menu_1_1.triggered.connect(self.show_manual_1)
        menu_1.addAction(menu_1_1)

        menu_1_2 = QAction('외부화일 실행용', self)
        menu_1_2.triggered.connect(self.show_manual_2)
        menu_1.addAction(menu_1_2)

        menu_1_3 = QAction(QIcon("save.png"),'참고사이트', self)
        menu_1_3.triggered.connect(qApp.quit)
        menu_1.addAction(menu_1_3)

        menu_2 = menubar.addMenu("Made by")

        menu_2_1 = QAction('누가 만들었나요?', self)
        menu_2_1.triggered.connect(self.show_manual_4)
        menu_2.addAction(menu_2_1)

        menu_2_2 = QAction('Logo의 의미', self)
        menu_2_2.triggered.connect(self.show_manual_5)
        menu_2.addAction(menu_2_2)

        menu_3 = menubar.addMenu("끝내기")

        menu_3_1 = QAction(QIcon('exit.png'),'Exit', self)
        menu_3_1.triggered.connect(qApp.quit)
        menu_3.addAction(menu_3_1)

    def make_menu_dic(self):
        # 모든 메소드를 다 언급하여 놓고 가능한 것만 두번째에 '필요'라고 써넣으면 된다
        # 사용하다보니, 모든 모듈을 자동으로 하도록 해볼려고 했으나 그것보다는 별도로 다른 의미로 쓸수도 잇도록 만드는게 좋을것 같아서 만듦

        self.basic_data = [
            ['add_macro_button', ['x'], ['추가', 'macro', 'button'], ['add', 'macro', 'button']],
            ['add_picture', ['x'], ['추가', 'picture', ''], ['add', 'picture', '']],
            ['add_picture_pixcel', ['x'], ['추가', 'picture', 'pixcel'], ['add', 'picture', 'pixcel']],
            ['add_range_text_bystep', ['필요'], ['추가-글자', '범위', '몇번째마다-번호'],
             ['add', 'range', 'text_bystep']],
            ['add_range_text_left', ['필요'], ['추가-글자', '범위', '왼쪽에추가'], ['add', 'range', 'text_left']],
            ['add_range_text_right', ['필요'], ['추가-글자', '범위', '오른쪽에추가'], ['add', 'range', 'text_right']],
            ['change_address_all', ['x'], ['변경하기', 'address', 'all'], ['change', 'address', 'all']],
            ['change_address_xyxy', ['x'], ['변경하기', 'address', 'xyxy'], ['change', 'address', 'xyxy']],
            ['change_char_num', ['x'], ['변경하기', 'char', 'num'], ['change', 'char', 'num']],
            ['change_list_1d_to2d', ['x'], ['변경하기', 'list', '1d_to2d'], ['change', 'list', '1d_to2d']],
            ['change_list_list2d', ['x'], ['변경하기', 'list', 'list2d'], ['change', 'list', 'list2d']],
            ['change_list_samelen', ['x'], ['변경하기', 'list', 'samelen'], ['change', 'list', 'samelen']],
            ['change_num_char', ['x'], ['변경하기', 'num', 'char'], ['change', 'num', 'char']],
            ['change_range_capital', ['필요'], ['변경-셀값', '영역', '첫글자만 대문자'], ['change', 'range', 'capital']],
            ['change_range_lower', ['필요'], ['변경-셀값', '영역', '소문자'], ['change', 'range', 'lower']],
            ['change_range_swapcase', ['필요'], ['변경-셀값', '영역', '대소문자 변경'],
             ['change', 'range', 'swapcase']],
            ['change_range_upper', ['필요'], ['변경-셀값', '영역', '대문자'], ['change', 'range', 'upper']],
            ['change_sheet_name', ['x'], ['변경-시트이름', 'sheet', 'name'], ['change', 'sheet', 'name']],
            ['change_xyxy_r1r1', ['x'], ['변경하기', 'xyxy', 'r1r1'], ['change', 'xyxy', 'r1r1']],
            ['check_address_value', ['x'], ['check', 'address', 'value'], ['check', 'address', 'value']],
            ['check_basic', ['x'], ['check', 'basic', ''], ['check', 'basic', '']],
            ['check_cell_type', ['x'], ['check', 'cell', 'type'], ['check', 'cell', 'type']],
            ['check_color', ['x'], ['check', 'color', ''], ['check', 'color', '']],
            ['check_color_style', ['x'], ['check', 'color', 'style'], ['check', 'color', 'style']],
            ['check_data_type', ['x'], ['check', 'data', 'type'], ['check', 'data', 'type']],
            ['check_list_address', ['x'], ['check', 'list', 'address'], ['check', 'list', 'address']],
            ['check_range_xx', ['x'], ['check', 'range', 'xx'], ['check', 'range', 'xx']],
            ['check_range_yy', ['x'], ['check', 'range', 'yy'], ['check', 'range', 'yy']],
            ['check_sheet_name', ['x'], ['check', 'sheet', 'name'], ['check', 'sheet', 'name']],
            ['check_string_address', ['x'], ['check', 'string', 'address'], ['check', 'string', 'address']],
            ['check_xline_empty', ['x'], ['check', 'xline', 'empty'], ['check', 'xline', 'empty']],
            ['check_xx_address', ['x'], ['check', 'xx', 'address'], ['check', 'xx', 'address']],
            ['check_xy_address', ['x'], ['check', 'xy', 'address'], ['check', 'xy', 'address']],
            ['check_yline_empty', ['x'], ['check', 'yline', 'empty'], ['check', 'yline', 'empty']],
            ['check_yy_address', ['x'], ['check', 'yy', 'address'], ['check', 'yy', 'address']],
            ['copy_range', ['x'], ['copy', 'range', ''], ['copy', 'range', '']],
            ['copy_xline', ['x'], ['copy', 'xline', ''], ['copy', 'xline', '']],
            ['copy_xxline_another_sheet', ['x'], ['copy', 'xxline', 'another_sheet'], ['copy', 'xxline',
                                                                                       'another_sheet']],
            ['copy_yline', ['x'], ['copy', 'yline', ''], ['copy', 'yline', '']],
            ['count_range_empty_cell', ['x'], ['count', 'range', 'empty_cell'],
             ['count', 'range', 'empty_cell']],
            ['count_sheet_shape', ['x'], ['count', 'sheet', 'shape'], ['count', 'sheet', 'shape']],
            ['delete_cell_value', ['x'], ['삭제', '셀의', '값'], ['delete', 'cell', 'value']],
            ['delete_from_n_words_01', ['필요'], ['셀값-일부삭제', '영역', '몇번째부터'],
             ['delete', 'from', 'n_words_01']],
            ['delete_range_bystep', ['필요'], ['삭제', '선택영역', '몇번째마다-번호'], ['delete', 'range', 'bystep']],
            ['delete_range_color', ['필요'], ['삭제', '선택영역', '색'], ['delete', 'range', 'color']],
            ['delete_range_empty_x', ['필요'], ['삭제', '선택영역', '빈-x열'], ['delete', 'range', 'empty_x']],
            ['delete_range_empty_y', ['필요'], ['삭제', '선택영역', '빈-y열'], ['delete', 'range', 'empty_y']],
            ['delete_range_line', ['필요'], ['삭제', '선택영역', '테두리선'], ['delete', 'range', 'line']],
            ['delete_range_linecolor', ['필요'], ['선색-삭제', '선택영역', '색-선'],
             ['delete', 'range', 'linecolor']],
            ['delete_range_link', ['필요'], ['삭제', '선택영역', 'link'], ['delete', 'range', 'link']],
            ['delete_range_ltrim', ['필요'], ['삭제', '선택영역', '왼쪽공백'], ['delete', 'range', 'ltrim']],
            ['delete_range_memo', ['필요'], ['삭제', '선택영역', '메모'], ['delete', 'range', 'memo']],
            ['delete_range_rtrim', ['필요'], ['삭제', '선택영역', '왼쪽공백'], ['delete', 'range', 'rtrim']],
            ['delete_range_samevalue', ['필요'], ['삭제', '선택영역', '같은값'],
             ['delete', 'range', 'samevalue']],
            ['delete_range_samevalue_continious', ['필요'], ['삭제', '선택영역', '같은값-연속된것'],
             ['delete', 'range', 'samevalue_continious']],
            ['delete_range_samevalue_unique', ['필요'], ['삭제', '선택영역', '고유한것만 남기기'],
             ['delete', 'range',
              'samevalue_unique']],
            ['delete_range_trim', ['필요'], ['삭제', '선택영역', '좌우공백'], ['delete', 'range', 'trim']],
            ['delete_range_value', ['필요'], ['삭제', '선택영역', '값'], ['delete', 'range', 'value']],
            ['delete_range_value_byno', ['필요'], ['삭제', '선택영역', '몇번째마다-번호'],
             ['delete', 'range', 'value_byno']],
            ['delete_range_xline_bystep', ['필요'], ['삭제', '선택영역', 'x열 반복삭제-번호'], ['delete', 'range',
                                                                                 'xline_bystep']],
            ['delete_range_yline_bystep', ['필요'], ['삭제', '선택영역', 'y열 반복삭제-번호'], ['delete', 'range',
                                                                                 'yline_bystep']],
            ['delete_rangename', ['필요'], ['삭제', '영역-이름', '없음'], ['delete', 'rangename', '']],
            ['delete_shape', ['필요'], ['삭제', '도형', '없음'], ['delete', 'shape', '']],
            ['delete_shape_all', ['필요'], ['삭제', '도형', '모든객체'], ['delete', 'shape', 'all']],
            ['delete_sheet', ['필요'], ['삭제', 'sheet', '없음'], ['delete', 'sheet', '']],
            ['delete_sheet_value_all', ['필요'], ['삭제', 'sheet', '모든값'],
             ['delete', 'sheet', 'value_all']],
            ['delete_usedrange_value', ['필요'], ['삭제', '영역-사용자', '값'],
             ['delete', 'usedrange', 'value']],
            ['delete_values_between_specific_letter', ['필요'], ['삭제', '찾은값', '특수문자사이'],
             [
                 'delete', 'values', 'between_specific_letter']],
            ['delete_xxline', ['필요'], ['삭제', 'xxline', '없음'], ['delete', 'xxline', '']],
            ['delete_xxline_value', ['필요'], ['삭제', 'xxline', '값'], ['delete', 'xxline', 'value']],
            ['delete_yyline', ['필요'], ['삭제', 'yyline', '없음'], ['delete', 'yyline', '']],
            ['delete_yyline_value', ['필요'], ['삭제', 'yyline', '값'], ['delete', 'yyline', 'value']],
            ['df_write_to_excel', ['x'], ['df', 'write', 'to_excel'], ['df', 'write', 'to_excel']],
            ['draw_cell_color', ['필요'], ['색칠하기', 'cell', 'color'], ['draw', 'cell', 'color']],
            ['draw_cell_fontcolor', ['필요'], ['색칠하기', 'cell', '폰트색'], ['draw', 'cell', 'fontcolor']],
            ['draw_cell_rgb', ['필요'], ['색칠하기', 'cell', 'rgb'], ['draw', 'cell', 'rgb']],
            ['draw_cell_rgbcolor', ['필요'], ['색칠하기', 'cell', 'rgbcolor'], ['draw', 'cell', 'rgbcolor']],
            ['draw_range_color', ['필요'], ['색칠하기', '선택영역', 'color'], ['draw', 'range', 'color']],
            ['draw_range_color_bywords', ['필요'], ['색칠하기', '선택영역', '단어가들어간것'], ['draw', 'range',
                                                                               'color_bywords']],
            ['draw_range_fontcolor', ['필요'], ['색칠하기', '선택영역', 'fontcolor'], ['draw', 'range', 'fontcolor']],
            ['draw_range_line', ['필요'], ['색칠하기', '선택영역', 'line'], ['draw', 'range', 'line']],
            ['draw_range_max_num_1', ['필요'], ['색칠하기', '선택영역', '최대숫자'], ['draw', 'range', 'max_num_1']],
            ['draw_range_mystyle', ['필요'], ['색칠하기', '선택영역', 'mystyle'], ['draw', 'range', 'mystyle']],
            ['draw_range_rgbcolor', ['필요'], ['색칠하기', '선택영역', 'rgbcolor'], ['draw', 'range', 'rgbcolor']],
            ['draw_range_samevalue_rgbcolor', ['필요'], ['색칠하기', 'range', 'samevalue_rgbcolor'],
             ['draw', 'range',
              'samevalue_rgbcolor']],
            ['draw_range_specific_text', ['필요'], ['색칠하기', '선택영역', '특수문자'], ['draw', 'range',
                                                                            'specific_text']],
            ['draw_spacecell_color', ['필요'], ['색칠하기', '공백', 'color'], ['draw', 'spacecell', 'color']],
            ['draw_xline_minvalue', ['필요'], ['색칠하기', 'x-열', '최소값'], ['draw', 'xline', 'minvalue']],
            ['dump_range_value', ['x'], ['dump', 'range', 'value'], ['dump', 'range', 'value']],
            ['excel_fun_trim', ['x'], ['excel', 'fun', 'trim'], ['excel', 'fun', 'trim']],
            ['fill_emptycell_uppercell', ['필요'], ['채워넣기', '빈셀', '위의것으로 채워넣기'], ['fill', 'emptycell',
                                                                                'uppercell']],
            ['fun_ltrim', ['x'], ['fun', 'ltrim', ''], ['fun', 'ltrim', '']],
            ['insert_sheet_new', ['x'], ['삽입', 'sheet', 'new'], ['insert', 'sheet', 'new']],
            ['insert_x_bystep', ['필요'], ['삽입', 'x-열', 'bystep'], ['insert', 'x', 'bystep']],
            ['insert_xx', ['필요'], ['삽입', 'xx-열', '없음'], ['insert', 'xx', '']],
            ['insert_y_bystep', ['필요'], ['삽입', 'y-열', 'bystep'], ['insert', 'y', 'bystep']],
            ['insert_yy', ['필요'], ['삽입', 'yy-열', '없음'], ['insert', 'yy', '']],
            ['intersect_range1_range2', ['x'], ['intersect', 'range1', 'range2'],
             ['intersect', 'range1', 'range2']],
            ['move_degree_distance', ['x'], ['move', 'degree', 'distance'], ['move', 'degree', 'distance']],
            ['move_range_bottom', ['x'], ['move', 'range', 'bottom'], ['move', 'range', 'bottom']],
            ['move_range_leftend', ['x'], ['move', 'range', 'leftend'], ['move', 'range', 'leftend']],
            ['move_range_rightend', ['x'], ['move', 'range', 'rightend'], ['move', 'range', 'rightend']],
            ['move_range_top', ['x'], ['move', 'range', 'top'], ['move', 'range', 'top']],
            ['move_range_ystep', ['x'], ['move', 'range', 'ystep'], ['move', 'range', 'ystep']],
            ['move_rangevalue_linevalue', ['x'], ['move', 'rangevalue', 'linevalue'], ['move', 'rangevalue',
                                                                                       'linevalue']],
            ['move_value_without_empty_cell_01', ['x'], ['move', 'value', 'without_empty_cell_01'], ['move',
                                                                                                     'value',
                                                                                                     'without_empty_cell_01']],
            ['move_x', ['x'], ['move', 'x', ''], ['move', 'x', '']],
            ['move_y', ['x'], ['move', 'y', ''], ['move', 'y', '']],
            ['print_preview', ['x'], ['print', 'preview', ''], ['print', 'preview', '']],
            ['read_cell_color', ['x'], ['read', 'cell', 'color'], ['read', 'cell', 'color']],
            ['read_cell_coord', ['X'], ['read', 'cell', 'coord'], ['read', 'cell', 'coord']],
            ['read_cell_memo', ['X'], ['read', 'cell', 'memo'], ['read', 'cell', 'memo']],
            ['read_cell_value', ['X'], ['read', 'cell', 'value'], ['read', 'cell', 'value']],
            ['read_continousrange_value', ['X'], ['read', 'continousrange', 'value'],
             ['read', 'continousrange',
              'value']],
            ['read_currentregion_address', ['X'], ['read', 'currentregion', 'address'],
             ['read', 'currentregion',
              'address']],
            ['read_inputbox_value', ['X'], ['read', 'inputbox', 'value'], ['read', 'inputbox', 'value']],
            ['read_range_value', ['X'], ['read', 'range', 'value'], ['read', 'range', 'value']],
            ['read_rangename_address', ['X'], ['read', 'rangename', 'address'],
             ['read', 'rangename', 'address']],
            ['read_selection_value', ['X'], ['read', 'selection', 'value'], ['read', 'selection', 'value']],
            ['read_shape_name', ['X'], ['read', 'shape', 'name'], ['read', 'shape', 'name']],
            ['read_usedrange_address', ['X'], ['read', 'usedrange', 'address'],
             ['read', 'usedrange', 'address']],
            ['read_xx_value', ['X'], ['read', 'xx', 'value'], ['read', 'xx', 'value']],
            ['read_yy_value', ['X'], ['read', 'yy', 'value'], ['read', 'yy', 'value']],
            ['replace_range_word_many', ['필요'], ['바꾸기', '선택영역', '한번에 많이 변경'],
             ['replace', 'range', 'word_many']],
            ['select_cell', ['x'], ['select', 'cell', ''], ['select', 'cell', '']],
            ['select_range', ['x'], ['select', 'range', ''], ['select', 'range', '']],
            ['select_sheet', ['x'], ['select', 'sheet', ''], ['select', 'sheet', '']],
            ['set_cell_bold', ['x'], ['set', 'cell', 'bold'], ['set', 'cell', 'bold']],
            ['set_cell_font_rgb', ['x'], ['set', 'cell', 'font_rgb'], ['set', 'cell', 'font_rgb']],
            ['set_cell_numberformat', ['x'], ['set', 'cell', 'numberformat'],
             ['set', 'cell', 'numberformat']],
            ['set_column_numberproperty', ['x'], ['set', 'column', 'numberproperty'], ['set', 'column',
                                                                                       'numberproperty']],
            ['set_formula', ['x'], ['set', 'formula', ''], ['set', 'formula', '']],
            ['set_fullscreen', ['x'], ['set', 'fullscreen', ''], ['set', 'fullscreen', '']],
            ['set_range_autofilter', ['x'], ['set', 'range', 'autofilter'], ['set', 'range', 'autofilter']],
            ['set_range_autofit', ['x'], ['set', 'range', 'autofit'], ['set', 'range', 'autofit']],
            ['set_range_bold', ['x'], ['set', 'range', 'bold'], ['set', 'range', 'bold']],
            ['set_range_font', ['x'], ['set', 'range', 'font'], ['set', 'range', 'font']],
            ['set_range_fontsize', ['x'], ['set', 'range', 'fontsize'], ['set', 'range', 'fontsize']],
            ['set_range_formula', ['x'], ['set', 'range', 'formula'], ['set', 'range', 'formula']],
            ['set_range_merge', ['x'], ['set', 'range', 'merge'], ['set', 'range', 'merge']],
            ['set_range_name', ['x'], ['set', 'range', 'name'], ['set', 'range', 'name']],
            ['set_range_numberformat', ['x'], ['set', 'range', 'numberformat'],
             ['set', 'range', 'numberformat']],
            ['set_range_unmerge', ['x'], ['set', 'range', 'unmerge'], ['set', 'range', 'unmerge']],
            ['set_range_xx', ['x'], ['set', 'range', 'xx'], ['set', 'range', 'xx']],
            ['set_range_yy', ['x'], ['set', 'range', 'yy'], ['set', 'range', 'yy']],
            ['set_sheet_lock', ['x'], ['set', 'sheet', 'lock'], ['set', 'sheet', 'lock']],
            ['set_sheet_unlock', ['x'], ['set', 'sheet', 'unlock'], ['set', 'sheet', 'unlock']],
            ['set_visible', ['x'], ['set', 'visible', ''], ['set', 'visible', '']],
            ['set_xx_height', ['x'], ['set', 'xx', 'height'], ['set', 'xx', 'height']],
            ['set_xx_numberproperty', ['x'], ['set', 'xx', 'numberproperty'],
             ['set', 'xx', 'numberproperty']],
            ['set_yy_width', ['x'], ['set', 'yy', 'width'], ['set', 'yy', 'width']],
            ['show_inputbox', ['x'], ['show', 'inputbox', ''], ['show', 'inputbox', '']],
            ['show_messagebox', ['x'], ['show', 'messagebox', ''], ['show', 'messagebox', '']],
            ['split_as_special_string', ['필요'], ['분리하기', '특정글자로', '특정글자'],
             ['split', 'as', 'special_string']],
            ['trans_list', ['x'], ['trans', 'list', '없음'], ['trans', 'list', '']],
            ['trans_range_value', ['필요'], ['xy바꾸기', '선택영역', '값'], ['trans', 'range', 'value']],
            ['unique_range_value', ['필요'], ['고유한것', '선택영역', '값'], ['unique', 'range', 'value']],
            ['write_activecell_value', ['필요'], ['쓰기', 'activecell', '값'],
             ['write', 'activecell', 'value']],
            ['write_activerange_value', ['필요'], ['쓰기', 'activerange', 'value'],
             ['write', 'activerange', 'value']],
            ['write_cell_memo', ['필요'], ['쓰기', '셀에', '매모'], ['write', 'cell', 'memo']],
            ['write_cell_value', ['필요'], ['쓰기', '셀에', '값'], ['write', 'cell', 'value']],
            ['write_emptycell_uppercell', ['필요'], ['쓰기', '빈셀', '위의셀값으로'], ['write', 'emptycell',
                                                                           'uppercell']],
            ['write_range_nansu', ['필요'], ['쓰기', '선택영역', '난수'], ['write', 'range', 'nansu']],
            ['write_range_value', ['필요'], ['쓰기', '선택영역', '값'], ['write', 'range', 'value']],
            ['write_range_value_linebase', ['필요'], ['쓰기', '선택영역', 'value_linebase'], ['write', 'range',
                                                                                      'value_linebase']],
            ['write_range_value_trans', ['필요'], ['쓰기', '선택영역', 'xy바꾸기'],
             ['write', 'range', 'value_trans']],
            ['write_range_value_ydirection_only', ['필요'], ['쓰기', '선택영역', '세로1줄로쓰기'],
             ['write', 'range', 'value_ydirection_only']], ]

        #메뉴를 만들기위해 저장한것
        for one in self.basic_data:
            #print(one)
            if one[1][0] == "필요":
                if one[2][0] in list(self.menu.keys()):
                    pass
                else:
                    self.menu[one[2][0]] = {one[3][0]: {}}

                if one[2][1] in list(self.menu[one[2][0]][one[3][0]]):
                    pass
                else:
                    self.menu[one[2][0]][one[3][0]][one[2][1]] = {one[3][1]: {}}

                if one[2][2] in list(self.menu[one[2][0]][one[3][0]][one[2][1]][one[3][1]]):
                    pass
                else:
                    self.menu[one[2][0]][one[3][0]][one[2][1]][one[3][1]][one[2][2]] = one[3][2]
            else:
                pass

    def tab_page_1(self):
        Main.keyPressEvent = self.keyPressEvent

        self.p1_table1 = mygrid.CreateTable(30, 3)
        self.p1_table1.setFont(QFont('Malgun Gothic', 10))
        self.p1_table1.setColumnWidth(2, 150)
        p1_menu1_list = list(self.menu.keys())
        p1_menu1_list.sort()

        # 기본 메뉴를 테이블에 만든다
        # [버튼위치], [누르면 실행될 코드], [버튼에나타나는 문구]
        for no in range(len(p1_menu1_list)):
            self.p1_table1.write_cell_button([no, 0], self.click_button_1st_menu, p1_menu1_list[no])

        # 버튼과 텍스트를 만드는것
        layout_top_3 = QVBoxLayout()
        layout_top_4 = QVBoxLayout()
        for one in range(1, 12):
            exec("self.btn_c_{} = QPushButton('')".format(one))
            exec("layout_top_3.addWidget(self.btn_c_{})".format(one))
            exec("self.text_d_{} = QLineEdit('')".format(one))
            exec("layout_top_4.addWidget(self.text_d_{})".format(one))

        # 실행버튼 : 버튼을 누르면 각 메소드가 실행되는 것
        p1_btn_run = QPushButton('실행')
        p1_btn_run.setMaximumHeight(200)
        p1_btn_run.setMaximumWidth(200)
        p1_btn_run.setFont(QFont('Malgun Gothic', 15))
        my_rgb_color = self.color.change_scolor_rgb("red85")
        my_hex_color = self.color.change_rgb_hex(my_rgb_color)
        p1_btn_run.setStyleSheet("background-color: {}".format(my_hex_color))
        p1_btn_run.clicked.connect(self.action_p1_run_button)

        # 메소의 설명이 나타나는 텍스트
        self.p1_txt1 = QPlainTextEdit()
        self.p1_txt1.setStyleSheet('color:black;font-size:12px;') #font-weight: bold

        message = """총 3단계로 이루어진부분입니다
        - 1단계 선택: 대분류 (액션의 분류)
        - 2단계 선택: 중분류 (보통 영역이나 대상물이다)
        - 3단계 선택: 소분류 (2단계로 끝나는 없는 경우는 '없음'으로 나타난다)
        - 입력폼에 변수값들을 입력한다
        - 실행 버튼을 누른다

        오른쪽 아랫부분의 입력폼은 변수들을 넣는 부분으로
        입력필요하고 된 부분은 꼭 입력을 해야 실행이 되는 부분입니다
        다, 입력후 '실행'버튼을 누르면 실행이 됩니다
        - 기본값 : 입력변수의 기본 설정 값으로 들어가는 것
        - sheet_name의 기본값 : 현재 활성화된 시트
        """
        self.p1_txt1.setPlainText(message.replace("        ", ""))
        layout_right_bottom = QHBoxLayout()
        layout_right_bottom.addLayout(layout_top_3, 3)
        layout_right_bottom.addLayout(layout_top_4, 7)


        layout_left = QHBoxLayout()
        layout_left.addWidget(self.p1_table1, 9)
        layout_left.addLayout(layout_right_bottom, 5)

        layout_main = QHBoxLayout()
        layout_main.addWidget(self.p1_txt1, 5)
        layout_main.addWidget(p1_btn_run, 1)

        layout_right = QVBoxLayout()
        layout_right.addLayout(layout_left, 5)
        layout_right.addLayout(layout_main, 2)

        wdg_1 = QWidget()
        wdg_1.setLayout(layout_right)
        return wdg_1

    def tab_page_2(self):
        Main.keyPressEvent = self.keyPressEvent

        self.p2_table1 = mygrid.CreateTable(30, 2)
        self.p2_table1.setFont(QFont('Malgun Gothic', 10))
        self.p2_table1.setColumnWidth(0, 250)
        self.p2_table1.setColumnWidth(1, 250)
        #두번째 탭은 사용자가 만든 코드를 한번 저장해 놓으면 사용가능하도록 하는 것이다
        user_filesss = self.yt.read_filename_in_folder_all("../pceller/user_code")
        for one_file in user_filesss:
            if one_file.endswith(".py"):
                self.new_menu.append(one_file)

        # 기본 메뉴를 테이블에 만든다
        # [버튼위치], [누르면 실행될 코드], [버튼에나타나는 문구]
        for no in range(len(self.new_menu)):
            x,y = divmod(no,2)
            self.p2_table1.write_cell_button([x, y], self.click_page2_run_button, self.new_menu[no])

        # 실행버튼 : 버튼을 누르면 각 메소드가 실행되는 것
        p2_btn_run = QPushButton('실행')
        p2_btn_run.setMaximumHeight(200)
        p2_btn_run.setMaximumWidth(200)
        p2_btn_run.setFont(QFont('Malgun Gothic', 15))
        my_rgb_color = self.color.change_scolor_rgb("blu85")
        my_hex_color = self.color.change_rgb_hex(my_rgb_color)
        p2_btn_run.setStyleSheet("background-color: {}".format(my_hex_color))
        p2_btn_run.clicked.connect(self.action_p2_run_button)

        # 메소의 설명이 나타나는 텍스트
        self.p2_txt1 = QPlainTextEdit()
        self.p2_txt1.setPlainText("이 실행화일이 있는 폴더안의 \nuser_folder안의 파이썬 화일을 실행 시키는 것이다\n입력받으면서 실행될 부분은 별도로 처리하여야 합니다. 단 외부 코드를 실행시키기 위해서는 \n - python 3.8이후 버전설치\n - pywin32설치\n - halmoney모듈의 살치")

        layout_left = QHBoxLayout()
        layout_left.addWidget(self.p2_table1)

        layout_right = QHBoxLayout()
        layout_right.addWidget(self.p2_txt1, 5)
        layout_right.addWidget(p2_btn_run, 2)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_left, 5)
        layout_main.addLayout(layout_right, 2)

        wdg_1 = QWidget()
        wdg_1.setLayout(layout_main)
        return wdg_1

    def tab_page_3(self):
        Main.keyPressEvent = self.keyPressEvent

        self.new_menu_3 = []
        self.p3_table1 = mygrid.CreateTable(30, 2)
        self.p3_table1.setFont(QFont('Malgun Gothic', 10))
        self.p3_table1.setColumnWidth(0, 250)
        self.p3_table1.setColumnWidth(1, 250)
        #두번째 탭은 사용자가 만든 코드를 한번 저장해 놓으면 사용가능하도록 하는 것이다
        user_filesss = self.yt.read_filename_in_folder_all("../pceller/volunteer_code")
        for one_file in user_filesss:
            if one_file.endswith(".py"):
                self.new_menu_3.append(one_file)

        # 기본 메뉴를 테이블에 만든다
        # [버튼위치], [누르면 실행될 코드], [버튼에나타나는 문구]
        for no in range(len(self.new_menu_3)):
            x,y = divmod(no,2)
            self.p3_table1.write_cell_button([x, y], self.click_page3_run_button, self.new_menu_3[no])

        # 실행버튼 : 버튼을 누르면 각 메소드가 실행되는 것
        p3_btn_run = QPushButton('실행')
        p3_btn_run.setMaximumHeight(200)
        p3_btn_run.setMaximumWidth(200)
        p3_btn_run.setFont(QFont('Malgun Gothic', 15))
        my_rgb_color = self.color.change_scolor_rgb("gre85")
        my_hex_color = self.color.change_rgb_hex(my_rgb_color)
        p3_btn_run.setStyleSheet("background-color: {}".format(my_hex_color))
        p3_btn_run.clicked.connect(self.action_p3_run_button)

        # 메소의 설명이 나타나는 텍스트
        self.p3_txt1 = QPlainTextEdit()
        self.p3_txt1.setPlainText("이것은 작성자가 추천하는 파이썬 화일을 \nvolunteer_code안에 넣어서 실행 시킬수 있도록 만는 것이다")

        layout_left = QHBoxLayout()
        layout_left.addWidget(self.p3_table1)

        layout_right = QHBoxLayout()
        layout_right.addWidget(self.p3_txt1, 5)
        layout_right.addWidget(p3_btn_run, 2)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_left, 5)
        layout_main.addLayout(layout_right, 2)

        wdg_1 = QWidget()
        wdg_1.setLayout(layout_main)

        return wdg_1

    def click_page3_run_button(self):
        for no in range(len(self.new_menu_3)):
            x,y = divmod(no,2)
            self.p3_table1.cellWidget(x, y).setStyleSheet("background-color: light gray")

        btn = self.sender()
        title = btn.text()
        btn.setStyleSheet("background-color: #A1EBFA")
        self.p3_txt1.setPlainText(title)

    def click_page2_run_button(self):
        for no in range(len(self.new_menu)):
            x,y = divmod(no,2)
            self.p2_table1.cellWidget(x, y).setStyleSheet("background-color: light gray")

        btn = self.sender()
        title = btn.text()
        btn.setStyleSheet("background-color: #A1EBFA")
        self.p2_txt1.setPlainText(title)

    def click_button_1st_menu(self):
        # 1번째 버튼을 누르면 실행되는 것이다
        # 기본 상태로 만든후 버튼 누른것을 실행한다
        for no in range(30):
            self.p1_table1.delete_cell_attribute([no, 1])
            self.p1_table1.delete_cell_attribute([no, 2])
        self.var["menu2_no"] = len(list(self.menu.keys()))
        for no in range(self.var["menu2_no"]):
            self.p1_table1.cellWidget(no, 0).setStyleSheet("background-color: light gray")

        btn = self.sender()
        btn.setStyleSheet("background-color: #A1EBFA")
        title = btn.text()
        self.p1_txt1.setPlainText("")

        #첫번째 선택한 1열의 설명과 이름을 갖고온다
        self.menu1_dic = self.menu[title]
        menu1_name = list(self.menu1_dic.keys())[0]
        self.var["menu1_name"] = menu1_name

        # 1번메뉴에 따라 선택한것을 이용해서, 2번째 메뉴를 만든다
        self.menu2_dic = self.menu1_dic[menu1_name]
        menu2_list = list(self.menu2_dic.keys())
        self.var["menu2_no"] = len(menu2_list)

        #2번째 라인에 버튼을 만든다
        for no in range(len(menu2_list)):
            self.p1_table1.write_cell_button([no, 1], self.click_button_2nd_menu, menu2_list[no])

    def click_button_2nd_menu(self):
        # 3번째 버튼을 삭제한다
        # 기본 상태로 만드는 것
        for no in range(self.var["menu2_no"]):
            self.p1_table1.cellWidget(no, 1).setStyleSheet("background-color: light gray")
        for no in range(15):
            self.p1_table1.delete_cell_attribute([no, 2])

        btn = self.sender()
        btn.setStyleSheet("background-color: #FFCCFF")
        title = btn.text()
        self.p2_txt1.setPlainText(title)

        self.menu3_dic = self.menu2_dic[title]
        menu2_name = list(self.menu3_dic.keys())[0]
        self.var["menu2_name"] = menu2_name

        self.menu3_dic = self.menu3_dic[menu2_name]
        menu3_list = list(self.menu3_dic.keys())
        self.var["menu3_no"] = len(menu3_list)

        #3번째 라인에 버튼을 만든다
        for no in range(len(menu3_list)):
            self.p1_table1.write_cell_button([no, 2], self.click_button_3rd_menu, menu3_list[no])

    def click_button_3rd_menu(self):
        #기본의 선택된 버튼의 색을 원래대로 만드는 것
        for no in range(self.var["menu3_no"]):
            self.p1_table1.cellWidget(no, 2).setStyleSheet("background-color: light gray")

        btn = self.sender()
        btn.setStyleSheet("background-color: #FFFFCC")
        title = btn.text()
        self.p3_txt1.setPlainText(title)

        self.menu4_name = self.menu3_dic[title]
        self.var["menu3_name"] = self.menu4_name

        #최종적으로 실행된 이름을 확인한다
        method_name = self.var["menu1_name"] + "_" + self.var["menu2_name"] + "_" + self.var["menu3_name"]
        if method_name[-1] == "_":
            method_name = method_name[:-1]
        self.var["method_name"] = method_name
        self.make_input_menu_and_textbox()

    def make_input_menu_and_textbox(self):
        """
        실시간 자료를 리스트에서 선택하면,
        가능하면 공통변수에 값을 넣도록 한다
        """
        # 버튼의 글자와 텍스트박스의 배경색을 제거한다
        self.reset_textedit_background()
        self.clear_button_text_all()

        try:
            # 선택한 메소드에 따라서 각 함수들의 parameter를 갖고온다
            list_value = self.var["method_name"]
            method_params_dic = self.params[list_value]
            self.var["method_name"] = list_value

            # 갖고온 자료를 버튼과 텍스트입력기에 써 넣는다
            num = 0
            for param_key in list(method_params_dic.keys()):
                # 버튼에 이름을 넣는 다
                exec("self.{}.setText('{}')".format(self.btn_name_list[num], param_key))
                value = method_params_dic[param_key]
                # 텍스트에 기본값을 넣는다
                if value == None or value == "":
                    value = "기본값"

                exec("self.text_d_{}.setText('{}')".format(str(num + 1), value))
                num = num + 1

            ddd = self.module_manual[list_value]
            self.p1_txt1.setPlainText(ddd[1].replace("\n\t\t", "\n"))
        except:
            pass

    def action_p2_run_button(self):
        file_path = ".\\user_code\\" + self.p2_txt1.toPlainText()
        subprocess.call(["python", file_path])

    def action_p3_run_button(self):
        file_path = ".\\volunteer_code\\" + self.p3_txt1.toPlainText()
        #print(file_path)
        subprocess.call(["python", file_path])

    def action_p1_run_button(self):
        """버튼을 누르면 pcell의 메소드를 실행 시키는것"""
        self.input_result = []
        self.reset_textedit_background()

        try:
            # 버튼과 텍스트입력기의 텍스트를 읽어온다
            for one in range(1, 8):
                exec("b{} = self.btn_c_{}.text()".format(one, one))
                exec("t{} = self.text_d_{}.text()".format(one, one))
                exec("self.input_result.append([b{}, t{}])".format(one, one))

            # 읽어온 텍스트에서 변경할것이나 오류등을 찾아낸다
            temp = ""
            for one_list in self.input_result:
                if one_list[0] == "":
                    pass
                else:
                    key = one_list[0]
                    value = one_list[1]
                    if one_list[1] == "기본값":
                        value = ""
                    elif one_list[1] == "입력필요":
                        temp = "error"
                        self.check_textedit_background()
                        break
                    temp = temp + str(key) + "='" + str(value) + "', "

            # 오류가 발견되면 에러를 나타낸다
            if temp == "error":
                print("입력이 필요한것을 입력후 재실행 시켜주세요")
                pass
            else:
                print("self.excel.{}({})".format(str(self.var["method_name"]), temp[:-2]))
                exec("self.excel.{}({})".format(str(self.var["method_name"]), temp[:-2]))
        except:
            pass


    def clear_button_text_all(self):
        """ 버튼과 텍스트의 글자를 다 지운다 """
        for one in self.btn_name_list:
            exec("self.{}.setText('')".format(one))

        for num in range(1, len(self.btn_name_list) + 1):
            exec("self.text_d_{}.setText('')".format(str(num)))

    def check_textedit_background(self):
        """ textedit의 색을 다시 원상복귀한다 """
        if self.text_d_1.text() == "입력필요": self.text_d_1.setStyleSheet("QLineEdit {background-color: red;}")
        if self.text_d_2.text() == "입력필요": self.text_d_2.setStyleSheet("QLineEdit {background-color: red;}")
        if self.text_d_3.text() == "입력필요": self.text_d_3.setStyleSheet("QLineEdit {background-color: red;}")
        if self.text_d_4.text() == "입력필요": self.text_d_4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.text_d_5.text() == "입력필요": self.text_d_5.setStyleSheet("QLineEdit {background-color: red;}")
        if self.text_d_6.text() == "입력필요": self.text_d_6.setStyleSheet("QLineEdit {background-color: red;}")
        if self.text_d_7.text() == "입력필요": self.text_d_7.setStyleSheet("QLineEdit {background-color: red;}")

    def reset_textedit_background(self):
        """ textedit의 색을 다시 원상복귀한다 """
        self.text_d_1.setStyleSheet("QLineEdit {background-color: None;}")
        self.text_d_2.setStyleSheet("QLineEdit {background-color: None;}")
        self.text_d_3.setStyleSheet("QLineEdit {background-color: None;}")
        self.text_d_4.setStyleSheet("QLineEdit {background-color: None;}")
        self.text_d_5.setStyleSheet("QLineEdit {background-color: None;}")
        self.text_d_6.setStyleSheet("QLineEdit {background-color: None;}")
        self.text_d_7.setStyleSheet("QLineEdit {background-color: None;}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())