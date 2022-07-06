from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, Union, Optional, Literal
import PIL, numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
import asyncio, os
from math import ceil
from .ark_setting import *

""" 
作图
"""

ark_font_entry = fm.FontEntry(ark_font_path, 'lxgw')
fm.fontManager.ttflist.append(ark_font_entry)
plt.rcParams['font.sans-serif'] = ['lxgw']  # 汉字字体
plt.rcParams['axes.facecolor'] = img_bcolor
plt.rcParams['savefig.facecolor'] = img_bcolor

def debug_plt(img):#调试时候使用
    plt.cla()
    plt.imshow(img)
    plt.show()


def pil_font(font_size: int = 48, font_path = ark_font_path):
    return ImageFont.truetype(
        font_path, font_size, encoding="utf-8"
    )
    
def set_plt_font(font_size:int = 16, font_path:str = ark_font_path):
    return {
        "size":font_size,
        "fontproperties":fm.FontProperties(fname=font_path)
    }
    
def plt_tick_font(font_size:int = 16, font_path:str = ark_font_path):
    return fm.FontProperties(fname=font_path, size=font_size)


def hex2rgb(hex:str):
    """16进制转RGB"""
    r = int(hex[1:3],16)
    g = int(hex[3:5],16)
    b = int(hex[5:7], 16)
    return (r,g,b)

class ArkImageDrawer():
    def __init__(self, 

                 img_w:int, 
                 img_h:int,
                 img_type = "RGBA",
                 background_color:Union[str, Tuple[float, float, float]] = base_img_back_color,
                 font_size=10) -> None:
        
        try:
            self.loop = asyncio.get_event_loop()
        except RuntimeError:
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            self.loop = asyncio.get_event_loop()
        self.img_w, self.img_h = img_w, img_h
        self.img_type = img_type    
        self.background_color = background_color
        self.font = pil_font(font_size)
        #创建用于绘图的画布
        self.img = Image.new(self.img_type, 
                                (self.img_w, self.img_h), 
                                 self.background_color)
        self.draw = ImageDraw.Draw(self.img)

    async def atext(
        self,
        pos: Tuple[int, int],
        text: str,
        font_size:int = 0,
        fill:str = 'black',
    ):
        """
        说明：
            异步 在图片上添加文字
        参数：
            :param pos: 文字位置
            :param text: 文字内容
            :param fill: 文字颜色
        """
        self.font = pil_font(font_size)
        await self.loop.run_in_executor(None, self.text, pos, text, font_size, fill)

    def text(
        self,
        pos: Tuple[int, int],
        text: str,
        font_size:int = 40,
        fill:str='black',
        
    ):
        """
        说明：
            在图片上添加文字
        参数：
            :param pos: 文字位置
            :param text: 文字内容
            :param fill: 文字颜色
        """
        self.font = pil_font(font_size)
        self.draw.text(pos, text, fill=fill, font=self.font)

    async def apaste(
        self,
        img: Image,
        pos: Optional[Tuple[int, int]] = None,
        alpha: bool = False,
    ):
        """
        说明：
            异步 贴图
        参数：
            :param img: 已打开的图片文件，可以为 BuildImage 或 Image
            :param pos: 贴图位置（左上角）
            :param alpha: 图片背景是否为透明
        """
        await self.loop.run_in_executor(None, self.paste, img, pos, alpha)

    # 贴图
    def paste(self, img, pos=None, alpha=False):
        self.img.paste(img, pos)
        return self.img
   

def save_tmp_fig(fig):
    """_summary_
    将图片临时保存到内存中
    Args:
        fig (_type_): _description_

    Returns:
        _type_: _description_
    """
    ioBytes = BytesIO()
    try:#保存plt.fig
        fig.savefig(ioBytes, format = 'png', transparent = False)
    except:#保存pil.image
        fig.save(ioBytes, 'png')
    ioBytes.seek(0)
    img_in_cache = Image.open(ioBytes)
    return img_in_cache   

def round_corner(img:Image, 
                 radii:int, 
                 back_color:Union[str, Tuple[float, float, float]] = base_img_back_color):
    """_summary_
    新的开圆角思路
    Args:
        img (_type_): _description_
        radii (_type_): _description_
    Returns:
        _type_: _description_
    """
    char_drawer_w,char_drawer_h = img.size
    random_back_color = (74,240,103,255)#随机取值，防止冲突
    back_color = hex2rgb(back_color)
    back_color_a = (back_color[0], back_color[1], back_color[2], 255)
    #创建等同img大小的画布，背景色为随机色1
    corner_img = Image.new('RGBA', img.size, random_back_color)

    #创建圆角画布，背景色为backcolor
    circle = Image.new('RGBA', (radii * 2, radii * 2), back_color)
    circle_drawer = ImageDraw.Draw(circle)
    #画圆，颜色为随机色1
    circle_drawer.ellipse((0, 0, radii * 2, radii * 2), fill=random_back_color)
    #贴圆
    corner_img.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
    corner_img.paste(circle.crop((radii, 0, radii * 2, radii)), (char_drawer_w - radii, 0))  # 右上角
    corner_img.paste(circle.crop((radii, radii, radii * 2, radii * 2)), (char_drawer_w - radii, char_drawer_h - radii))  # 右下角
    corner_img.paste(circle.crop((0, radii, radii, radii * 2)), (0, char_drawer_h - radii))  # 左下角
    img_array = np.array(img)
    corner_array = np.array(corner_img)
    #rcolor2是圆内的颜色， 
    img = np.where(corner_array==back_color_a, corner_array, img_array)
    return Image.fromarray(img, mode='RGBA')



class BaseImage():#作图基类，目前无内容
    def __init__(self) -> None:
        pass



    
class CharImage(BaseImage):
    def __init__(self, 
                 line_cnt:int, 
                 char_type:str='star6char', 
                 record_info:dict = {},
                 radii:int = 25,
                 background_color:Union[str, Tuple[float, float, float]] = char_drawer_p['bcolor'])-> None:
        super().__init__()
        self.line_cnt = line_cnt
        self.char_type = char_type
        self.info = record_info
        self.char_info = self.info[char_type +'_info']['chars']
        self.char_type_name = f"新获得干员（至多显示{max_char_count}个）" \
            if char_type == "newchar" \
            else f"获得六星干员（至多显示{max_char_count}个）"
        #干员星级颜色映射
        self.star_colors ={
            3:'blue',
            4:'purple',
            5:'#EEEE00',
            6:'#ffcc4d',
        }
        self.cur_line_cnt = ceil(len(self.char_info)/2)
        self.char_drawer = ArkImageDrawer(char_drawer_p['w'],
                                     char_drawer_p['h'](self.cur_line_cnt),
                                     background_color = background_color)
        
        self.radii = radii
        
 
    
    def draw_chars(self):
        self.char_drawer.text(char_title_p['pos'], 
                         self.char_type_name, 
                         char_title_p['fsize'], fill=char_title_p['color'])#标题
        for i in range(self.cur_line_cnt):
            for j in range(2):
                tmpw, tmph = indi_char_drawer_p['w'], indi_char_drawer_p['h']
                indi_drawer = ArkImageDrawer(tmpw, tmph, background_color=indi_char_drawer_p['bcolor'])
                try:char = self.char_info[2*i+j]
                except:break
                char_name = char['name']
                char_star = char['star']
                char_desc = char['desc']
                char_profile = self.generate_char_profile(char_name.split(' ')[0].strip(), char_star)
                #绘制图片和文字
                indi_drawer.paste(char_profile, char_text_p['profile_pos'])
                indi_drawer.text(char_text_p['name_pos'], char_name, char_text_p['char_name_fsize'], char_text_p['char_name_color'])
                indi_drawer.text(char_text_p['desc_pos'], char_desc, char_text_p['char_desc_fsize'], char_text_p['char_desc_color'])
                self.char_drawer.paste(indi_drawer.img, 
                                  indi_char_drawer_p[f'pos{j}'](i))
        self.char_drawer.img = round_corner(self.char_drawer.img, 
                                             self.radii)# 白色区域透明可见，黑色区域不可见
        return self.char_drawer.img
      
    def generate_char_profile(self, 
                              char_name:str, 
                              char_star:int):
        """_summary_
        生成好看的单张头像
        Args:
            char_name (str): _description_
            char_star (int): _description_

        Returns:
            _type_: _description_
        """
        char_profile_path = (operator_profile_dir + "/" + f'profile_{char_name}.png')
        try:
            char_profile0 = Image.open(char_profile_path)
        except:#没有头像没更新就用海猫
            haimao_png_path = (operator_profile_dir + "/" + "海猫.png")
            char_profile0 = Image.open(haimao_png_path)
        #重塑大小
        char_profile0 = char_profile0.resize((char_text_p['profile_w'], 
                                             char_text_p['profile_w']))
        #边框
        char_profile = Image.new('RGB', 
                                 size=(char_profile0.width+6, char_profile0.height+6), 
                                 color=self.star_colors[char_star])
        #白色背景
        profile_backgrouond = Image.new('RGBA', 
                                 size=(char_profile0.width, char_profile0.height), 
                                 color="white")
        char_profile.paste(profile_backgrouond, (3, 3), mask=profile_backgrouond)
        char_profile0 = char_profile0.convert('RGBA')
        char_profile.paste(char_profile0, (3, 3), mask=char_profile0)
        return char_profile
        
class ArkImage(BaseImage):
    def __init__(self, 
                 record_info:dict,
                 user_id:str,
                 img_param:tuple) -> None:
        super().__init__()
        img_wh = img_param[0]
        self.char_line_cnt = img_param[1]
        self.record_info = record_info
        self.user_id = user_id
        save_img_name = f"record_img_{user_id}.png"
        self.save_path = os.path.join(record_img_dir, save_img_name)
        self.aid = ArkImageDrawer(img_wh[0], img_wh[1])
        
        self.info_type_dict ={
            "star":{
                'cn_desc' : "星级分布",
                'info':self.record_info['star_info'],
                'pie_style':pie_star_p,
                'text_style':desc_star_p
            },
            "pool":{
                'cn_desc' : f"卡池分布(最多{max_pool_count}个)",
                'info':self.record_info['pool_info'],
                'text_style':desc_pool_p,
                'histo_style':histo_pool_p,
            },
            "shuiwei":{
                'cn_desc': "卡池水位情况",
                'info':self.record_info['shuiwei_info'],
                'text_style':desc_shuiwei_p,
            }
        }
   
    def text_title(self, user_name:str, pool_name:str, record_count:int):
        if pool_name == 'all':pool_name = '所有卡池'
        pool_desc = f"卡池：{pool_name}"
        count_desc = f"最近{record_count}抽"
        self.aid.text(title_p['pos'], 
                      f"{user_name}的寻访分析", 
                      title_p['fsize'],
                      fill=title_p['color'])
        self.aid.text(sub_title_p['pos'], 
                      f"{pool_desc} {count_desc}", 
                      sub_title_p['fsize'],
                      sub_title_p['color'])
     
    def draw_histo(self, query_type:str = 'pool'):
        """_summary_
        绘制直方图
        Args:
            query_type (str, optional): _description_. Defaults to 'pool'.
        """
        record_info = self.info_type_dict[query_type]['info']
        style = self.info_type_dict[query_type]['histo_style']
        fig, ax = plt.subplots()

        ylabels = record_info['desc']
        ycount = record_info['count']
        yrange = range(len(ylabels))
        ax.set_title(self.info_type_dict[query_type]['cn_desc'], 
                     fontsize = int(style['title_fsize']),
                     color = style['title_fcolor'])
        bar = ax.barh(yrange, ycount, tick_label = ylabels, height = 0.4)
        ax.set_yticklabels(ylabels, 
                           fontsize = int(style['tick_fsize']),
                           color = style['tick_fcolor'])
        ax.bar_label(bar, 
                     ycount, 
                     fontsize = int(style['tick_fsize']),
                     color = style['tick_fcolor'])
        plt.subplots_adjust(left=0.4, right=0.72, bottom=0.1,)
        #关闭x轴和刻度
        ax.set_xticks([])
        off_spines = ['bottom', 'top', 'right']
        for spine in off_spines:
            ax.spines[spine].set_visible(False)
        img_in_cache = save_tmp_fig(fig)
        img_in_cache = img_in_cache.crop((0,0,560,480))
        img_in_cache = img_in_cache.resize((style['w'], style['h']))
        img_in_cache = round_corner(img_in_cache, style['radii'])
        self.aid.paste(img_in_cache, style[f'pos'])
        plt.cla()
    
    def draw_pie(self, query_type:str = "star"):
        """_summary_
        绘制饼状图
        Args:
            query_type (str, optional): _description_. Defaults to "star".
        """
        record_info = self.info_type_dict[query_type]['info']
        style = self.info_type_dict[query_type]['pie_style']
        fig, ax = plt.subplots()
        _,l_text,p_text = ax.pie(record_info['count'], 
               labels = record_info['desc'],#todo:labels 还要修改 加上具体数值
               autopct='%0.2f%%')
        for t in l_text:#设置字体大小
            t.set_size(int(style['text_fsize']))
            t.set_color(style['text_fcolor'])
        for t in p_text:#设置字体大小
            t.set_size(int(style['percent_fsize']))
            t.set_color(style['percent_fcolor'])
        ax.set_title(self.info_type_dict[query_type]['cn_desc'], 
                     fontsize = int(style['title_fsize']),
                     color = style['title_fcolor'])
        # plt.subplots_adjust()
        img_in_cache = save_tmp_fig(fig)
        img_in_cache = img_in_cache.crop((80,0,560,480))#宽560 高480
        img_in_cache = img_in_cache.resize((style['w'], style['h']))
        img_in_cache = round_corner(img_in_cache, style['radii'])
        self.aid.paste(img_in_cache, style['pos'])
        plt.cla()

    def text_distribution(self, query_type:str = "star"):
        record_info = self.info_type_dict[query_type]['info']
        style = self.info_type_dict[query_type]['text_style']
        tmp_text_drawer = ArkImageDrawer(style['bimage']['w'], 
                                         style['bimage']['h'],
                                         background_color=style['bimage']['bcolor'])
        #标题、正文描述
        for part in style['parts']:
            part_style = style[part]
            tmp_text_drawer.text(part_style['pos'], 
                                 record_info[part],
                                 font_size=part_style['fsize'],
                                 fill=part_style['color'])
        tmp_text_drawer.img = round_corner(tmp_text_drawer.img,
                                            style['bimage']['radii'])
        self.aid.paste(tmp_text_drawer.img, style['bimage']['pos'])
   
    def draw_char_query(self, char_type:str = 'star6char') -> None:
        """
        不用plt 
        先生成数个小画板，然后合成一个大画板，最后贴图
        """        
        ci = CharImage(self.char_line_cnt, char_type, self.record_info)
        char_img = ci.draw_chars()
        self.aid.paste(char_img, char_drawer_p[f"pos_{char_type}"])
         
 
    def save(self):
        try:
            res_img = self.aid.img
            res_img.save(self.save_path)
            print('arkgacha now_save')
            return True, self.save_path
        except:
            return False, "保存结果图像失败"



        