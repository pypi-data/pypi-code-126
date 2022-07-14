import setuptools

setuptools.setup(
    name="xwtgzs-lz",
    version="1.0",
    author="刘贞、小於菟工作室",
    author_email="LZ.XWT@outlook.com",
    description="小於菟工作室开发的包。",
    long_description="此库中有两个模块：text_and_number（文字与数字处理库，后文简称为TAN）、common_methods_in_daily_life(日常生活中的常用方法，后文简称为CMIDL），在TAN中有6个方法：1.speak（text）text是文本或数字类型，此方法将生成一个.vbs文件在pip安装位置，默认自动读出文件。2.remove_quotation_marks（a）a是任意字符串，它将字符串去掉两个“""”(此方法对于文字也有用)，返回值为非字符串的文字或数字。3.dictionary_value_separation(a, number)a是字典，number是0或者1，它用于将字典的键和值分离，并且返回一个列表，其中有所有的值或者键，number是0是取键，1取值。4.power_calculation（a,number）此方法中，a和number均为数字，计算number的a次方，返回计算结果的数值。5.Solve_the_greatest_common_factor(x, y)求解x,y的最大因数6.Solve_the_least_common_multiple（x，y）求解x,y的最小公倍数；在CMIDL中有两个方法：1.weather(a, b, c),a是字符串格式的省份拼音，b是字符串格式的城市拼音，c是数值；当c = 0为今天，c = 1为明天，c=3为后天（其中含有天气、气温、穿衣提醒等）2.be_qr(a,b)a格式随便的内容，b是数值1或者0，如果b= 1 则展示图片，b = 0则返回图片名，可全盘查找。 ",
    long_description_content_type="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'xwtgzs-lz'}

)
