

import os
import re
import arrow

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from hoshi.messages import TranslatableStructuredMessage

from kivy_garden.ebs.core.labels import SelfScalingLabel
from kivy_garden.ebs.clocks import SimpleDigitalClock

from ebs.linuxnode.i18n.mixin import i18nMixin
from ebs.linuxnode.gui.kivy.timetable.base import Timetable
from ebs.linuxnode.gui.kivy.timetable.base import TimetableEntry

from ebs.linuxnode.gui.kivy.timetable.base import BaseTimetableMixin
from ebs.linuxnode.gui.kivy.timetable.base import BaseTimetableGuiMixin

from ebs.linuxnode.tables.translatable import TranslatableTableSpec
from ebs.linuxnode.tables.spec import BasicColumnSpec


def render_time(ts, fmt="HH:mm"):
    return ts.format(fmt)


route_rex = re.compile(r"(?P<origin>[\S -]+[\S])\s+to\s+(?P<destination>[\S -]+?[\S])($|\s+via\s+(?P<via>[\S]+))",
                       re.IGNORECASE)


class RsrtcRoute(TranslatableStructuredMessage):
    def __init__(self, route):
        m = route_rex.match(route.strip())
        if not m:
            print("Error Parsing : {}".format(route))
            parts = {'raw': route}
        else:
            parts = self.preprocess_parts(m.groupdict())
            parts['raw'] = route
        super(RsrtcRoute, self).__init__(parts)
        self.install_template('en_IN', "[b]{origin}[/b] to [b]{destination}[/b] via [b]{via}[/b]")
        self.install_template('en_IN', "[b]{origin}[/b] to [b]{destination}[/b]")
        self.install_template('en_IN', "{raw}")
        self.install_template('hi_IN', "[b]{origin}[/b] से [b]{destination}[/b] ([b]{via}[/b] के रास्ते)")
        self.install_template('hi_IN', "[b]{origin}[/b] से [b]{destination}[/b]")
        self.install_template('hi_IN', "{raw}")

    def preprocess_parts(self, parts):
        parts = self.preprocess_part(parts, 'origin')
        parts = self.preprocess_part(parts, 'destination')
        parts = self.preprocess_part(parts, 'via')
        return parts

    def preprocess_part(self, parts, key):
        if key in parts.keys():
            if parts[key]:
                parts[key] = parts[key].upper().strip()
            else:
                parts.pop(key)
        return parts


class RsrtcTimetableEntry(TimetableEntry):
    def __init__(self, data):
        super(RsrtcTimetableEntry, self).__init__(data)

    @property
    def service_id(self):
        return self.data['bus_service_no']

    @property
    def name(self):
        return RsrtcRoute(self.data['route_name'])

    @property
    def ts_start(self):
        return arrow.get(self.data['scheduled_date'], 'YYYY-MM-DD HH:mm:ss').replace(tzinfo="+05:30")

    @property
    def departure_time(self):
        return self.ts_start

    @property
    def status(self):
        if (arrow.now() - self.ts_start).total_seconds() > 900:
            return "DEPART"
        else:
            return ""

    @property
    def ts_end(self):
        return arrow.get(self.data['scheduled_date'], 'YYYY-MM-DD HH:mm:ss').replace(tzinfo="+05:30")
    
    @property
    def route_no(self):
        return self.data['route_no']

    @property
    def bus_type(self):
        return self.data['bus_type_cd']

    @property
    def bus_no(self):
        return self.data['bus_no'] or ''

    @property
    def depot(self):
        return self.data['depot_cd']

    def __repr__(self):
        return "<{0} {1} {2}>".format(self.__class__.__name__, self.departure_time, self.name)


class RsrtcTimetable(Timetable):
    def __init__(self, node):
        self._title = None
        spec = TranslatableTableSpec(
            self,
            [
             BasicColumnSpec("Service", 'bus_type', width=120,
                             font_bold=False, dynamic_scaling=False),
             BasicColumnSpec("Departs", "departure_time", width=140,
                             dynamic_scaling=False),
             BasicColumnSpec("Bus Number", 'bus_no', width=280,
                             font_bold=False, i18n=False, dynamic_scaling=False),
             BasicColumnSpec("Route", 'name', halign='left',
                             markup=True, font_bold=False),
             BasicColumnSpec("Depot", 'depot', width=120, font_bold=False,
                             i18n=False, dynamic_scaling=False)],
            show_column_header=True, dedup_keys=['service_id'],
            row_height=90, row_spacing=10, font_size='42sp', font_bold=True,
            name='RSRTC', languages=node.i18n_supported_languages,
            **node.text_font_params,
        )
        super(RsrtcTimetable, self).__init__(node, spec)
        metadata = {
            'project': "RSRTC Infopanel",
            'version': self.node.rsrtc_version,
            'msgid_bugs_address': "shashank.chintalagiri@gmail.com",
            'language_team': "StarXMedia Signage Maintenance Team",
            'last_translator': None,
            'copyright_holder': "Propress Instrumentation & Solutions Pvt. Ltd., India",
        }
        spec.install_metadata(metadata)
        spec.install_catalog_dir(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'locale')))
        self.install()

    @property
    def prior_window(self):
        return self.node.config.rsrtc_window_prior or 30

    @property
    def post_window(self):
        return self.node.config.rsrtc_window_post or 60

    def _build_title_text(self):
        title_text = BoxLayout(
            orientation='vertical',
            size_hint=(1, 1),
            spacing=0,
        )

        l_font_params = self.spec.font_params
        l_font_params.update({
            'font_size': '42sp',
            'bold': True
        })
        org_title = Label(
            text=self.preprocess("Rajasthan State Road Transport Corporation".upper()),
            color=self.palette.cell_background,
            size_hint=(1, None), height=55, valign='middle', halign='left',
            **l_font_params
        )
        org_title.bind(size=org_title.setter('text_size'))
        title_text.add_widget(org_title)

        l_font_params = self.spec.font_params
        l_font_params.update({
            'font_size': '32sp',
            'bold': True
        })
        station_name = SelfScalingLabel(
            text=self.preprocess(self._node.config.rsrtc_stop_name),
            color=self.palette.header_cell_background,
            size_hint=(1, None), height=45, valign='middle', halign='right',
            **l_font_params
        )
        station_name.bind(size=station_name.setter('text_size'))
        title_text.add_widget(station_name)
        return title_text

    def _redraw_title(self, *_):
        _new_title_text = self._build_title_text()
        self._title.remove_widget(self._title.children[1])
        self._title.add_widget(_new_title_text, 1)

    def _build_title(self):
        if self._title:
            return self._title

        self._title = BoxLayout(
            orientation='horizontal', spacing=20, padding=[30, 10],
            size_hint=(1, None), height=120,
        )

        logo = Image(
            source=self.node.config.get_path(os.path.join('resources', 'logo.png')),
            size_hint=(None, 1), allow_stretch=True, keep_ratio=True)
        self._title.add_widget(logo)

        self._title_text = self._build_title_text()
        self._title.add_widget(self._title_text)

        # station_code = SelfScalingLabel(
        #     text=self._node.config.rsrtc_stop_id.upper(),
        #     color=self.palette.header_cell_background,
        #     size_hint=(None, 1), font_size='110sp', bold=True,
        #     valign='middle', halign='right',  # font_name=self.spec.font_name
        # )
        # station_code.bind(texture_size=station_code.setter('size'))
        # self._title.add_widget(station_code)

        l_font_params = self.spec.font_params
        l_font_params.update({
            'font_size': '110sp',
            'bold': True
        })
        clock = SimpleDigitalClock(
            color=self.palette.cell_background,
            size_hint=(None, 1), valign='middle', halign='right',
            **l_font_params
        )
        clock.bind(texture_size=clock.setter('size'))
        clock.start()
        self._title.add_widget(clock)
        return self._title


class RsrtcTimetableMixin(BaseTimetableGuiMixin, BaseTimetableMixin, i18nMixin):
    _timetable_class = RsrtcTimetable
    _timetable_entry_class = RsrtcTimetableEntry

    def __init__(self, *args, **kwargs):
        super(RsrtcTimetableMixin, self).__init__(*args, **kwargs)

    def install(self):
        super(RsrtcTimetableMixin, self).install()
        self._timetable.fallback_image = self.config.get_path('resources/rsrtc-bg-blue.png')
        self.i18n.install_object_translator(arrow.Arrow, render_time)

    def rsrtc_timetable_update(self, response):
        self.log.info("Loading Timetable Response with {n} Entries",
                      n=len(response))
        self.timetable_update(response, incremental=False)

    @property
    def rsrtc_timetable(self):
        return self.timetable_gui
