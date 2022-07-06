from pyecharts.charts import Line
from pyecharts.charts import Bar
from pyecharts import options as opts

class Returns(object):
    @classmethod
    def returns(cls, returns, name, width='1600px', height = '900px'):
        plotcon = cls.returns_line(returns['con'], '累计收益', '#9370DB', name, True)
        plot1m = cls.returns_line(returns['1m'], '最近一月', '#FFB6C1',name)
        plot1w = cls.returns_line(returns['1w'], '最近一周', '#DA70D6',name)
        plot1q = cls.returns_line(returns['1q'], '最近一季度', '#8B4513', name)
        return plotcon.overlap(plot1q).overlap(plot1m).overlap(plot1w)

    @classmethod
    def returns_line(cls, returns_data, name, color, block_name=None, init=False):
        trade_date_list =  [dt.date() for dt in returns_data.index.tolist()]
        line_plot = Line()
        line_plot.add_xaxis(trade_date_list)
        result_format = [float(str(result * 100)[0:5]) for result in returns_data['returns'].values.tolist()]
        line_plot.add_yaxis(name, result_format,linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
                           is_smooth=True,
                           is_connect_nones=True,
                           is_symbol_show=True,
                           itemstyle_opts=opts.ItemStyleOpts(color=color),
                           label_opts=opts.LabelOpts(is_show=False))
        
        line_plot.set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True,
                                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                                axistick_opts=opts.AxisTickOpts(is_show=False),
                                splitline_opts=opts.SplitLineOpts(is_show=False),
                                axislabel_opts=opts.LabelOpts(is_show=False)),
            yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis",
                    axis_pointer_type="cross",
                    background_color="rgba(245, 245, 245, 0.8)",
                    border_width=1,
                    border_color="#ccc",
                    textstyle_opts=opts.TextStyleOpts(color="#000"),
                ),
                visualmap_opts=opts.VisualMapOpts(
                    is_show=False,
                    dimension=2,
                    series_index=[0],
                    is_piecewise=True,
                    pieces=[
                        {"value": 1, "color": "#ec0000"},
                        {"value": -1, "color": "#00da3c"},
                    ],
                ),
            datazoom_opts=opts.DataZoomOpts(is_show=True,
                        type_="slider",
                        pos_top="90%",
                        range_start=0,
                        range_end=100,),
            title_opts=opts.TitleOpts(title=block_name + '-收益图')
        )
        
        return line_plot