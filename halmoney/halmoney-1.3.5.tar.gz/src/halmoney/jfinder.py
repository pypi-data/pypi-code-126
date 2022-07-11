# -*- coding: utf-8 -*-
import re
from halmoney import basic_data

class jfinder:
    def __init__(self):
        basic = basic_data.basic_data()
        self.common_data = basic.basic_data()
        self.jf_sql = ""
        self.re_sql = ""
        self.re_compiled = ""

    def manual(self):
        result = """
            이것을 만든 이유는 정규표현식이 업무에 사용하기 편한것인데
            일반적인 사람들이 읽고 사용하기가 어려워
            쉽게 사용할수있도록 만들어 본것이다
            그래서 일부 형식은 기존 정규표현식을 따라간것들도 있다
            단, 너무 복잡한 표현식은 

            전반적인 설정을 할때는 괄호를 사용해서 나타내었다 ==> (대소문자무시)(여러줄)(개행문자포함)(최소찾기)
                가능한한 설정은 제일 앞부분에 나타내기를 바란다
                (최소찾기) ==> 최소단어찾기를 위한 설정
                (대소문자무시) ==> re.IGNORECASE 대소문자 무시
                (여러줄)  ==> re.MULITILINE 여러줄도 실행
                (개행문자포함)  ==> # re.DOTALL 개행문자도 포함
            or는 |로 사용
                "(010|016|019)-[숫자:3~4]-[숫자:3~4]" ==> 또는 을 사용할때는 가급적 괄호를 사용하는것을 추천한다
            갯수를 지정할때는 1~3과같이 물결무늬를 이용해서 나타내었다 ==> 숫자가 0개~3개일때 ==> [숫자:0~3] 
                대괄호를 사용하여 구분 한다, 갯수는 ~를 사용한다,
                보통사용하는 re구문을 그대로 사용하여도 적용된다. 단 너무 복잡한것은 오류가 날 가능성도 있다
                일반적인 사용법 => "[맨앞][한글:3~3][영어:0~2]"
            문자하나가 아니고 단어자체가 반복을 하는 경우를 찾아야하는경우도 있다. 이렬경우는
                단어를 반복할때는 : [단어(abc):3~4]  => (abc){3,4}
            문자의 앞뒤에 조건이 붙는 경우
                (앞에있음:문자)
            특수문자나 일반 문자를 대괄호에 그대로 사용하여도 된다
                특수문자(".^ $ *+ ? {}[] \ | ()")의 사용법 => [.$:3~4]
            일본어나 중국어등의 문자열등을 추가하고 싶을때는 위의 리스트를 변경하면 된다
            """
        return result
    def basic_re(self):
        data = ".^$ *+?{}[]\|()"
        #이것만 사용이 가능하다

    def check_string_address(self, input_text="입력필요"):
        """
        입력형태 : "$1:$8", "1", "a","a1", "a1b1", "2:3", "b:b"
        숫자와 문자로 된부분을 구분하는 것이다
        """
        result = []
        aaa = re.compile("[a-zA-Z]*|\d*")
        temp_text = aaa.findall(str(input_text))
        for one in temp_text:
            if one != "":
                result.append(one)
        print(result)
        return result

    def check_column_type(self, input_list, per = 80):
        """
        넘어오는 자료형에 대해서, 평가를 내리는것
        per를 넣은것은 몇프로이상이면 이것을 OK할것인지를 알아보는 것에대한 기준을 만드는 것이다
        """
        total_no = 0
        for one_data in input_list:
            total_no = total_no + 0


    def is_date(self, input_data):
        """
        입력값이 날짜에 대한 것인지 확인하는 것이다
        결과값 : 1(yes), 0(no)
        조건 : 숫자가 3개이상은 있어야 한다
        """
        re_basic = "[\d\-\.\/년월일시분초]{3,}"
        p = re.compile(re_basic)
        temp = p.match(input_data)
        if temp:
            result = 1
        else:
            result = 0
        return result


    def jfinder (self, input_data):
        """
        간단한 사용법은 한글로된것만 3~7개 짜리만 찾을때 ==> [한글:3~7]
        정규표현식은 resql이라 말하고,
        jfinder의 사용할때 사용하는 구문은 jfsql이라고 사용한다

        findall(패턴, 문자열, 플래그)
        findall()은 문자열 안에 패턴에 맞는 케이스를 전부 찾아서 리스트로 반환합니다.
        """
        result = input_data.replace(" ", "")

        setup_list = [
            ["(대소문자무시)", "(?!)"], #re.IGNORECASE 대소문자 무시
            ["(여러줄)", "(?m)"], # re.MULITILINE 여러줄도 실행
            ["(개행문자포함)", "(?s)"], # re.DOTALL 개행문자도 포함
            ]

        for one in setup_list:
            result = result.replace(one[0], one[1])



        basic_list = [
            [":(\d+)[~](\d*)[\]]", "]{\\1,\\2}"], # :3~4] ==> ]{3,4}
            ["[\[](\d+)[~](\d*)[\]]", "{\\1,\\2}"], # [3~4] ==> {3,4}

            ["\(뒤에있음:(.*)\)",                "(?=\\1)" ], #(뒤에있음:(abc)) => (?=abc)
            ["\(뒤에없음:(.*)\)",                "(?!\\1)" ], #(뒤에없음:(abc)) => (?!abc)
            ["\(앞에있음:(.*)\)",                "(?<=\\1)"], #(앞에있음:(abc)) => (?<=abc)
            ["\(앞에없음:(.*)\)",                "(?<!\\1)"], #(앞에없음:(abc)) => (?<!abc)

            ["([\[]?)한글[&]?([\]]?)", "\\1ㄱ-ㅎ|ㅏ-ㅣ|가-힣\\2"],
            ["([\[]?)한글자음[&]?([\]]?)",       "\\1ㄱ-ㅎ\\2"], #[ㅏ-ㅣ]
            ["([\[]?)한글모음[&]?([\]]?)",       "\\1ㅏ-ㅣ\\2"], #[ㅏ-ㅣ]
            ["([\[]?)숫자[&]?([\]]?)",          "\\1 0-9 \\2"],
            ["([\[]?)영어대문자[&]?([\]]?)",     "\\1A-Z\\2"],
            ["([\[]?)영어소문자[&]?([\]]?)",     "\\1a-z\\2"],
            ["([\[]?)영어[&]?([\]]?)",          "\\1a-zA-Z\\2"],
            ["([\[]?)일본어[&]?([\]]?)",        "\\1ぁ-ゔ|ァ-ヴー|々〆〤\\2"],
            ["([\[]?)한자[&]?([\]]?)",          "\\1一-龥\\2"],
            ["([\[]?)특수문자[&]?([\]]?)",       "\\1 @#$&-_ \\2"],
            ["([\[]?)문자[&]?([\]]?)",          "."],
            ["([\[]?)공백[&]?([\]]?)",          "\\1\\\s\\2"], #공백문자(스페이스, 탭, 줄바꿈 등)

            ["[\[]단어([(].*?[)])([\]]?)",      "\\1"],
            ["[\[]또는([(].*?[)])([\]]?)",      "\\1|"],
            ["[\(]이름<(.+?)>(.+?)[\)]",        "?P<\\1>\\2"], #[이름<abc>표현식]
            ]



        for one in basic_list:
            result = re.sub(one[0], one[1], result)
            result = result.replace(" ", "")

        simple_list = [
            ['[처음]', '^'], ['[맨앞]', '^'], ['[시작]', '^'],
            ['[맨뒤]', '$'], ['[맨끝]', '$'], ['[끝]', '$'],
            ['[또는]', '|'], ['또는', '|'],['or', '|'],
            ['not', '^'],
            ]

        for one in simple_list:
            result = result.replace(one[0], one[1])

        #이단계를 지워도 실행되는데는 문제 없으며, 실행 시키지 않았을때가 약간 더 읽기는 편하다
        #일부 기본 re모듈을 사용할수있도록 만든것이다
        #그리고 밑의 최소탐색이 가능하게 하기위한 변경하는 부분이다
        high_list = [
            ['[^a-zA-Z0-9]', '\W'],
            ['[^0-9a-zA-Z]', '\W'],
            ['[a-zA-Z0-9]', '\w'],
            ['[0-9a-zA-Z]', '\w'],
            ['[^0-9]', '\D'],
            ['[0-9]', '\d'],
            ['{0,}', '*'],
            ['{1,}', '+'],
            ]

        for one in high_list:
            result = result.replace(one[0], one[1])

        #최대탐색을 할것인지 최소탐색을 할것인지 설정하는 것이다
        if "(최소찾기)" in result:
            result = result.replace("[1,]","+")
            result = result.replace("[1,]","*")

            result = result.replace("+","+?")
            result = result.replace("*","*?")
            result = result.replace("(최소찾기)","")

        #print("re구문은 ===>", result)
        return result

    def change_jfsql_resql (self, jf_sql):
        """
        JFINDER의 형식을 정규식표현으로 바꾸는 것이다
        """
        re_sql = self.jfinder(jf_sql)
        self.re_sql = re_sql
        return re_sql

    def set_jfsql (self, jf_sql):
        """
        JFINDER의 형식을 정규식표현으로 바꾸는 것이다
        """
        re_sql = self.jfinder(jf_sql)
        self.re_sql = re_sql
        return re_sql


    def check_all_cap(self, input_data):
        """
        처음부터 끝까지 모두 알파벳 대문자인지를 파악
        입력된 자료중 모두 대문자인 것들만 돌려준다
        """
        jf_sql = "[처음][영어대문자:1~][끝]"
        re_basic = self.change_jfsql_resql(jf_sql)
        result = re.findall(re_basic, input_data)
        return result

    def check_dash_date(self, input_data):
        """
        처음부터 끝까지 -로된 날짜 인지를 확인
        2,4개숫자 - 1~2개 숫자 - 1~2개숫자
        """
        re_basic = "^\d{2,4}-\d{1,2}-\d{1,2}$"
        result = re.findall(re_basic, input_data)
        return result

    def check_email_address(self, input_data):
        """
        이메일주소를 확인
        """
        re_basic = "^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
        result = re.findall(re_basic, input_data)
        return result

    def check_eng_only(self, input_data):
        """
        처음부터 끝까지 모두 영문인지 확인
        """
        re_basic = "^[a-zA-Z]+$"
        result = re.findall(re_basic, input_data)
        return result

    def check_handphone_only(self, input_data):
        """
        처음부터 끝까지 핸드폰 번호인지 확인
        """
        jf_sql = "[처음](010|019|011)-[숫자:4~4]-[숫자:4~4]"
        re_basic = self.change_jfsql_resql(jf_sql)
        result = re.findall(re_basic, input_data)
        return result

    def check_phone_no(self, input_data):
        """
        전화번호인지 알아내는것
        """
        jf_sql = "[숫자:2~3][-:0~1][숫자:3~4][-:0~1][숫자:4~4]"
        re_basic = self.change_jfsql_resql(jf_sql)
        result = re.findall(re_basic, input_data)
        #result = re.findall(re_basic, input_data)
        #return result

    def check_ip_address(self, input_data):
        """
        IP주소 입력
        """
        re_basic = "((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))"
        result = re.findall(re_basic, input_data)
        return result

    def check_korean_only(self, input_data):
        """
        # 모두 한글인지
        """
        re_basic = "[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]"
        result = re.findall(re_basic, input_data)
        return result

    def check_special_char(self, input_data):
        """
        특수문자가들어가있는지
        영어, 숫자, 한글이외의 글자 찾기
        """
        re_basic = "^[a-zA-Z0-9ㄱ-ㅎ|ㅏ-ㅣ|가-힣]"
        result = re.findall(re_basic, input_data)
        return result

    def remain_eng_num(self, input_text):
        """
        알파벳과 숫자만 있는것을 확인하는것
        """
        re_com = re.compile("[^A-Za-z0-9]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            print(re_com.search(input_text))
            new_text = re_com.sub("", input_text)
            print(new_text)
        return new_text

    def remain_kor_eng_num(self, input_text):
        """
        # 한글, 영어, 숫자만 남기고 나머지는 모두 지우는 것이다
        """
        re_com = re.compile("[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-힣]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            print(re_com.search(input_text))
            new_text = re_com.sub("", input_text)
            print(new_text)
        return new_text

    def delete_numcomma(self, input_text):
        """
        숫자중에서 ,로 분비리된것중에서 ,만 없애는것
        1,234,567 => 1234567
        """
        re_com = re.compile("[0-9,]")
        re_com_1 = re.compile("[,]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            new_text = re_com_1.sub("", input_text)
            print(new_text)
        return new_text

    def remain_specialchar(self, input_text):
        """
        # 공백과 특수문자등을 제외하고 같으면 새로운 y열에 1을 넣는 함수
        # 리스트의 사이즈를 조정한다
        """
        re_com = re.compile("[\s!@#$%^*()\-_=+\\\|\[\]{};:'\",.<>\/?]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            new_text = re_com.sub("", input_text)
            print(new_text)
        return new_text

    def find_hangul(self, input_data):
        """
        문장속의 모든 한글을 돌려준다
        """
        jf_sql = "[한글:1~]"
        re_basic = self.change_jfsql_resql(jf_sql)
        result = re.findall(re_basic, input_data)
        return result

    def find_eng(self, input_data):
        """
        문장속의 모든 영어를 돌려준다
        """
        jf_sql = "[영어:1~]"
        re_basic = self.change_jfsql_resql(jf_sql)
        result = re.findall(re_basic, input_data)
        return result

    def between_no1_no2(self, input_text, m, n):
        """
        숫자 : m,n개사이인 것만 추출
        """
        re_basic = "^\d{" + str(m) + "," + str(n) + "}$"
        result = re.findall(re_basic, input_text)
        return result

    def between_len1_len2(self, input_text, m, n):
        """
        문자수 : m다 크고 n보다 작은 문자
        """
        re_basic = "^.{" + str(m) + "," + str(n) + "}$"
        result = re.findall(re_basic, input_text)
        return result

    def between_text1_text2(self, input_text, text_a, text_b):
        """
        두개 문자사이의 글자를 갖고오는것
        """
        replace_lists = [
            ["(", "\("],
            [")", "\)"],
        ]
        origin_a = text_a
        origin_b = text_b

        for one_list in replace_lists:
            text_a = text_a.replace(one_list[0], one_list[1])
            text_b = text_b.replace(one_list[0], one_list[1])
        re_basic = text_a + "[^" + str(origin_b) + "]*" + text_b
        result = re.findall(re_basic, input_text)
        return result

    def run_all_2nd (self, jf_sql, jfinder_result):
        """
        정규표현식이 된것을 다시한번 적용하기 위한 것이다
        한번의 실행으로 완료되지 못한 내용을 다시한번 실행하기 위해서는 jfinder로 나온 결과값을 변경하는 기능이 필요
        """

        result = []
        for one_jf in jfinder_result:
            temp_list = self.run_all(jf_sql, one_jf[0])
            if temp_list:
                for one_list in temp_list:
                    one_list[1] = one_list[1] + one_jf[1] -1
                    one_list[2] = one_list[2] + one_jf[2] -1
                    result.append(one_list)
        return result


    def run_all (self, jf_sql, input_text):
        """
        찾은것과 찾은 위치를 함께 돌려주는 것이다
        만약 그룹으로 뿍었다면, 그룹또한 돌려준다
        [[결과값, 시작순서, 끝순서, [그룹1, 그룹2...], match결과].....]
        """
        re_sql = self.jfinder(jf_sql)
        re_com = re.compile(re_sql)
        result_match = re_com.match(input_text)
        result_finditer = re_com.finditer(input_text)

        final_result = []
        num=0
        for one_iter in result_finditer:
            temp=[]
            #찾은 결과값과 시작과 끝의 번호를 넣는다
            temp.append(one_iter.group())
            temp.append(one_iter.start())
            temp.append(one_iter.end())

            #그룹으로 된것을 넣는것이다
            temp_sub = []
            if len(one_iter.group()):
                for one in one_iter.groups():
                    temp_sub.append(one)
                temp.append(temp_sub)
            else:
                temp.append(temp_sub)

            #제일 첫번째 결과값에 match랑 같은 결과인지 넣는것
            if num == 0: temp.append(result_match)
            final_result.append(temp)
            num+=1
        return final_result

    def run_total(self, input_sql, input_text ):
        """
        조건에 맞는것을 찾아서 여러개가 있을경우 리스트로 돌려주는 것이다
        [[결과값, 시작순서, 끝순서, [그룹1, 그룹2...], match결과].....]
        """
        re_com = re.compile(input_sql)
        re_results = re_com.finditer(input_text)
        result = []
        if re_results:
            for one in re_results:
                result.append([one.group(), one.start(), one.end()])
        return result

    def run_resql (self, re_sql, input_text):
        """
        re구문 자체를 실행시키는것
        """
        re_compiled = re.compile(re_sql)
        result = re_compiled.findall(input_text)
        return result

    def get_replaced_text (self, jf_sql, input_text, replace_word):
        result = self.run_replace(jf_sql, input_text, replace_word)
        return result

    def get_serched_text (self, jf_sql, input_text):
        result = self.run_search (jf_sql, input_text)
        return result

    def get_serched_text_with_all (self, jf_sql, input_text):
        result = self.run_total(jf_sql, input_text )
        return result


    def set_basic_data (self, jf_sql):
        self.re_sql = self.jfinder(jf_sql)
        self.re_compiled = re.compile(self.re_sql)


    def speed_replaced_text (self, input_text, replace_word):
        """
        set_basic_data를 이용해서 매번 jfsql을 변경하고, re_sql을 변경하는 것을 set을 이용하여 외부에서 한번에 하는 것이다
        많은 수의 반복을 할때 속도를 올릴수있다
        """
        result = self.re_compiled.sub(replace_word, str(input_text))
        return result

    def speed_serched_text (self, input_text):
        result = self.re_compiled.findall(str(input_text))
        return result


    def speed_serched_text_with_all (self, jf_sql, input_text):
        result = self.run_total(jf_sql, str(input_text) )
        return result


    def run_replace (self, jf_sql, input_text, replace_word):
        """
        조건에 맞는 것을 찾으면 원하는 것으로 바꾸는 것이다
        """
        re_sql = self.jfinder(jf_sql)
        re_compiled = re.compile(re_sql)
        result = re_compiled.sub(replace_word, str(input_text))
        return result

    def run_search (self, jf_sql, input_text):
        """
        조건에 맞는것을 찾아서 여러개가 있을경우 리수트로 돌려주는 것이다
        """
        re_sql = self.jfinder(jf_sql)
        re_compiled = re.compile(re_sql)
        #print(re_compiled)
        result = re_compiled.findall(str(input_text))
        return result

    def run_resql_for_file(self, re_sql, file_name):
        """
        텍스트화일을 읽어서 re에 맞도록 한것을 리스트로 만드는 것이다
        함수인 def를 기준으로 저장을 하며, [[공백을없앤자료, 원래자료, 시작줄번호].....]
        """
        re_com = re.compile(re_sql)
        f = open(file_name, 'r', encoding='UTF8')
        lines = f.readlines()
        num = 0
        temp = ""
        temp_original = ""
        result = []
        for one_line in lines:
            aaa = re.findall(re_com, str(one_line))
            original_line = one_line
            changed_line = one_line.replace(" ", "")
            changed_line = changed_line.replace("\n", "")

            if aaa:
                result.append([temp, temp_original, num])
                temp = changed_line
                temp_original = original_line
            # print("발견", num)
            else:
                temp = temp + changed_line
                temp_original = temp_original + one_line
        return result

    def split_double_moum(self, input_mo):
        """
        이중모음을 단모음으로 바꿔주는것
        """
        mo2_dic = {"ㅘ": ["ㅗ", "ㅏ"], "ㅙ": ["ㅗ", "ㅐ"], "ㅚ": ["ㅗ", "ㅣ"], "ㅝ": ["ㅜ", "ㅓ"], "ㅞ": ["ㅜ", "ㅔ"], "ㅟ": ["ㅜ", "ㅣ"],
                   "ㅢ": ["ㅡ", "ㅣ"], }
        result = mo2_dic[input_mo]
        return result

    def split_hangul_jamo(self, text):
        """
        한글자의 한글을 자음과 모음으로 구분해 주는것
        출력형식 : [[초성, 중성, 종성],["초성, 중성, 종성의 자릿수],
                [바이트번호를 각 자릿수에 맞도록 1자리 숫자로 만들기 위해 변경한것],[encode한 것]]
        # print("encode한 것 ==> ", one_byte_data)
        # print("바이트번호를 각 자릿수에 맞도록 1자리 숫자로 만들기 위해 변경한것 ==> ", bite_no_1)
        # print("입력한 한글 한글자는 ==> ", text)
        # print("초성, 중성, 종성의 자릿수 ==> ", step_letter)
        # print("초성, 중성, 종성의 글자 ==> ", chojoongjong)
        """

        first_letter = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ",
                        "ㅎ"]  # 19 글자
        second_letter = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ",
                         "ㅢ",
                         "ㅣ"]  # 21 글자
        third_letter = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ",
                        "ㅅ",
                        "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]  # 28 글자, 없는것 포함
        one_byte_data = text.encode("utf-8")
        no_1 = int(one_byte_data[0])
        no_2 = int(one_byte_data[1])
        no_3 = int(one_byte_data[2])

        new_no_1 = (no_1 - 234) * 64 * 64
        new_no_2 = (no_2 - 128) * 64
        new_no_3 = (no_3 - 128)

        bite_no = [no_1, no_2, no_3]  # 바이트번호인 16진수를 10진수로 나타낸것
        bite_no_1 = [new_no_1, new_no_2, new_no_3]  # 바이트번호를 각 자릿수에 맞도록 1자리 숫자로 만들기 위해 변경한것

        value_sum = new_no_1 + new_no_2 + new_no_3

        value = value_sum - 3072  # 1의자리에서부터 시작하도록 만든것
        temp_num_1 = divmod(value, 588)  # 초성이 몇번째 자리인지를 알아내는것
        temp_num_2 = divmod(temp_num_1[1], 28)  # 중성과 종성의 자릿수를 알아내는것것

        chosung = first_letter[divmod(value, 588)[0]]  # 초성
        joongsung = second_letter[divmod(temp_num_1[1], 28)[0]]  # 중성
        jongsung = third_letter[temp_num_2[1]]  # 종성

        step_letter = [temp_num_1[1], temp_num_2[0], temp_num_2[1]]  # 초성, 중성, 종성의 자릿수
        chojoongjong = [chosung, joongsung, jongsung]  # 초성, 중성, 종성의 글자

        return [chojoongjong, step_letter, bite_no, value, one_byte_data]

    def split_eng_num(self, data):
        """
        영어와 숫자를 분리해 주는 것
        많이 사용하는 것 같아서 만들어 본것입니다
        입력문자열에서 영어와 숫자만 찾아서 돌려주는것
        """
        re_compile = re.compile(r"([a-zA-Z]+)([0-9]+)")
        result = re_compile.findall(data)
        new_result = []
        for dim1_data in result:
            for dim2_data in dim1_data:
                new_result.append(dim2_data)
        return new_result