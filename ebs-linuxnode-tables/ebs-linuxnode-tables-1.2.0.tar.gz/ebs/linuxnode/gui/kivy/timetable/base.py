

import arrow
from cached_property import cached_property_with_ttl
from twisted import logger
from twisted.internet.task import deferLater
from twisted.internet.defer import CancelledError

from ebs.linuxnode.core.log import NodeLoggingMixin
from ebs.linuxnode.i18n.mixin import i18nMixin
from ebs.linuxnode.gui.kivy.core.text import FontsGuiMixin
from ebs.linuxnode.gui.kivy.core.basemixin import BaseGuiMixin

from ebs.linuxnode.tables.spec import BasicTablePalette
from ebs.linuxnode.tables.spec import BasicTableSpec
from ebs.linuxnode.tables.spec import BasicColumnSpec
from ebs.linuxnode.gui.kivy.tables.animated import AnimatedTable
from ebs.linuxnode.gui.kivy.tables.renderable import BasicRenderableTableEntry


class TimetableEntry(BasicRenderableTableEntry):
    def __init__(self, data):
        super(TimetableEntry, self).__init__(data)

    @property
    def name(self):
        raise NotImplementedError

    @property
    def ts_start(self):
        raise NotImplementedError

    @property
    def ts_end(self):
        raise NotImplementedError


class Timetable(AnimatedTable):
    _prior_window = 30
    _post_window = 60
    _period_page = 12

    def __init__(self, node, spec=None):
        self._log = None
        self._redraw_task = None
        self._current_page = 0
        if not spec:
            spec = BasicTableSpec(self, [
                BasicColumnSpec("Name", 'name'),
                BasicColumnSpec("Start Time", "ts_start"),
                BasicColumnSpec("End Time", "ts_end")],
                show_column_header=True,
                row_height=90, row_spacing=10, font_size='42sp', font_bold=False)
        super(Timetable, self).__init__(node, spec)

    @property
    def prior_window(self):
        return self._prior_window

    @property
    def post_window(self):
        return self._post_window

    @property
    def log(self):
        if not self._log:
            self._log = logger.Logger(namespace="timetable.{0}".format(self._spec.name),
                                      source=self)
        return self._log

    def build(self, entries):
        return super(Timetable, self).build(entries=entries)

    @cached_property_with_ttl(ttl=5)
    def active_entries(self):
        return [x for x in sorted(self._entries, key=lambda y: y.ts_start)
                if x.ts_start.shift(minutes=-1 * self.post_window) < arrow.now() < x.ts_end.shift(minutes=self.prior_window)]

    def start(self):
        self.log.info("Starting Timetable Redraw Task for {0}".format(self))
        self._current_page = 0
        self.step()

    def _turn_page(self):
        self._current_page = self._current_page + 1
        tp = self.total_pages
        self.log.debug("Turning to page {0} of {1}".format(self._current_page, tp))
        if self._current_page >= tp:
            self.next_language()
            self.log.debug("Switched to Next Language : {}".format(self._i18n_language))
            self._current_page = 0

    def step(self):
        self._turn_page()
        deferLater(self._node.reactor, 0.0, lambda: None)
        self.redraw_entries(entries=self.page_entities(self._current_page))
        deferLater(self._node.reactor, 0.0, lambda: None)
        duration = self._period_page
        self._redraw_task = deferLater(self._node.reactor, duration, self.step)

        def _cancel_handler(failure):
            failure.trap(CancelledError)
        self._redraw_task.addErrback(_cancel_handler)

        return self._redraw_task

    def retrigger(self):
        if self._redraw_task.active():
            self._redraw_task.cancel()
        self.step()

    def stop(self):
        self.log.info("Stopping Timetable Redraw Task for {0}".format(self))
        if self._redraw_task:
            self._redraw_task.cancel()


class BaseTimetableMixin(i18nMixin, NodeLoggingMixin):
    _timetable_class = Timetable
    _timetable_entry_class = TimetableEntry

    def __init__(self, *args, **kwargs):
        self._timetable = None
        super(BaseTimetableMixin, self).__init__(*args, **kwargs)

    def install(self):
        super(BaseTimetableMixin, self).install()
        self.log.info("Installing TimeTable {0} with {1}"
                      "".format(self._timetable_class.__name__,
                                self._timetable_entry_class.__name__))
        self._timetable = self._timetable_class(self)

    def timetable_update(self, data, incremental=False):
        self._timetable.update([self._timetable_entry_class(x) for x in data],
                               incremental)


class BaseTimetableGuiMixin(BaseTimetableMixin, FontsGuiMixin, BaseGuiMixin):
    def __init__(self, *args, **kwargs):
        self._timetable_palette = None
        self._timetable_gui = None
        self._task_timetable_redraw = None
        super(BaseTimetableGuiMixin, self).__init__(*args, **kwargs)

    @property
    def timetable_palette(self):
        if not self._timetable_palette:
            self._timetable_palette = BasicTablePalette(
                color_cell_background=self.gui_color_2,
                color_cell_foreground=self.gui_color_foreground,
                color_header_cell_background=self.gui_color_1,
                color_header_cell_foreground=self.gui_color_foreground,
                color_grid_background=self.gui_color_background,
            )
        return self._timetable_palette

    @property
    def timetable_gui(self):
        if not self._timetable_gui:
            self._timetable.palette = self.timetable_palette
            self._timetable_gui = self._timetable.build(entries=self._timetable.active_entries)
            self._timetable.start()
        return self._timetable_gui

    def _timetable_redraw(self):
        self._timetable.build(entries=self._timetable.active_entries)
