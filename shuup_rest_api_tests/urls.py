# -*- coding: utf-8 -*-
# This file is part of Shuup REST API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('shuup_api.urls')),
    url(r'^', include('shuup.front.urls', namespace="shuup")),
]
