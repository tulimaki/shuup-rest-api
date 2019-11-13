# -*- coding: utf-8 -*-
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup_rest_api"
    label = "shuup_rest_api"
    provides = {
        "api_populator": [
            "shuup_rest_api.api.populate_api"
        ]
    }
