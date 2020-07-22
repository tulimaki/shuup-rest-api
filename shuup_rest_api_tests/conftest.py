# -*- coding: utf-8 -*-
# This file is part of Shuup REST API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from shuup.testing.factories import get_default_shop
from shuup.xtheme.testing import override_current_theme_class

# ORIGINAL_SETTINGS = []


def pytest_runtest_call(item):
    # All tests are run with a theme override `shuup.themes.classic_gray.ClassicGrayTheme`.
    # To un-override, use `with override_current_theme_class()` (no arguments to re-enable database lookup)
    from shuup.themes.classic_gray.theme import ClassicGrayTheme
    item.session._theme_overrider = override_current_theme_class(ClassicGrayTheme, get_default_shop())
    item.session._theme_overrider.__enter__()


# def pytest_runtest_setup(item):
#     global ORIGINAL_SETTINGS
#     ORIGINAL_SETTINGS = [item for item in settings.INSTALLED_APPS]
#     settings.INSTALLED_APPS = [app for app in settings.INSTALLED_APPS if "shuup.front" not in app]


# def pytest_runtest_teardown(item):
#     settings.INSTALLED_APPS = [item for item in ORIGINAL_SETTINGS]
