from runml.dashboard.tabs.base_tab import Tab, Verbose
from runml.dashboard.widgets.bar_widget import BarWidget
from runml.dashboard.widgets.counter_widget import CounterWidget
from runml.dashboard.widgets.expandable_list_widget import ExpandableListWidget
from runml.dashboard.widgets.percent_widget import PercentWidget
from runml.dashboard.widgets.text_widget import TextWidget


class WidgetGalleryTab(Tab):
    widgets = [
        (BarWidget(""), Verbose.ALWAYS),
        (CounterWidget(""), Verbose.ALWAYS),
        (PercentWidget(""), Verbose.ALWAYS),
        (ExpandableListWidget("Some title"), Verbose.ALWAYS),
        (TextWidget("Some title"), Verbose.ALWAYS),
    ]
