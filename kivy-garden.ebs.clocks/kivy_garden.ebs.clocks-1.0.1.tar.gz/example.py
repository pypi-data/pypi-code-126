

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.ebs.clocks import SimpleDigitalClock

# Scaling does not work with this approach. There is possibly something else in
# the original full linuxnode which makes SelfScalingLabel work. It might have
# to do with bindings to Window.size


class ClockExampleApp(App):
    def build(self):
        w = BoxLayout(size_hint=(1, 1))
        clock = SimpleDigitalClock(bold=True, font_size='120sp')
        w.add_widget(clock)
        return w


ClockExampleApp().run()
