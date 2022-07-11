# -*- coding: utf-8 -*-
#
# tw2.recaptcha2.widgets - TW2 widget for reCAPTCHA v2.0
#
# Copyright © 2017 Nils Philippsen <nils@tiptoe.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from tw2.core import Widget, Param, Variable, JSSource

from .resources import recaptcha2_js


class ReCaptcha2Widget(Widget):

    resources = [recaptcha2_js]

    template = 'tw2.recaptcha2.templates.recaptcha2'

    sitekey = Param("Google reCAPTCHA API v2.0 site key", request_local=False)

    theme = Param("Theme to use (light, dark)", default=None)

    captcha_type = Param("Type of captcha to use (image, audio)", default=None)

    size = Param("Size of Captcha (normal, compact)", default=None)

    tabindex = Param("Optional tabindex of the widget", default=None)

    callback = Param("Name of optional callback to execute when the user "
                     "submits a successful CAPTCHA response", default=None)

    expired_callback = Param("Name of optional callback to execute when "
                             "the recaptcha response expires and the user "
                             "needs to solve a new CAPTCHA", default=None)

    captcha_div_attrs = Variable()

    copyresponse_js = Variable()

    def prepare(self):
        if self.theme not in (None, 'light', 'dark'):
            raise ValueError("Theme must be 'light' or 'dark'")
        if self.captcha_type not in (None, 'image', 'audio'):
            raise ValueError("CAPTCHA type must be 'image' or 'audio'")
        if self.size is not None and not (isinstance(self.size, int) and
                                          self.size > 0):
            raise ValueError("Tabindex must be a positive integer")

        self.captcha_div_attrs = {'data-callback': 'recaptcha2_copy_response'}
        for attr in ('sitekey', 'theme', 'captcha_type', 'size', 'tabindex',
                     'expired_callback'):
            if getattr(self, attr):
                self.captcha_div_attrs['data-' + attr] = getattr(self, attr)

        if hasattr(self, 'compound_key'):
            input_name = self.compound_key
        else:
            input_name = self.compound_id

        if not self.callback:
            callback_js_source = ""
        else:
            callback_js_source = "{callback}(response);"

        self.copyresponse_js = JSSource(
            src="function recaptcha2_copy_response(response) {{"
            "  var div = document.getElementById('{id}');"
            "  var elements = document.getElementsByName('{name}');"
            "  for (var i = 0; i < elements.length; i++) {{"
            "    if (elements[i].type == 'hidden') {{"
            "      elements[i].value = response;"
            "    }}"
            "  }}"
            "  {callback_js_source}"
            "}}".format(id=self.compound_id, name=input_name,
                        callback_js_source=callback_js_source))

        super(ReCaptcha2Widget, self).prepare()
