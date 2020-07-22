# -*- coding: utf-8 -*-
from shuup_workbench.settings.utils import get_disabled_migrations
from shuup_workbench.test_settings import *  # noqa

INSTALLED_APPS = list(locals().get('INSTALLED_APPS', [])) + [
    "shuup_rest_api",
    "rest_framework.authtoken"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db.sqlite3'
    }
}

MIGRATION_MODULES = get_disabled_migrations()
MIGRATION_MODULES.update({
    app: None
    for app in INSTALLED_APPS
})

ROOT_URLCONF = 'shuup_rest_api_tests.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'shuup_api.authentication.ExpiringTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'shuup_api.permissions.ShuupAPIPermission',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}

SHUUP_ENABLE_MULTIPLE_SHOPS = True
SHUUP_BASKET_ORDER_CREATOR_SPEC = "shuup.core.basket.order_creator:BasketOrderCreator"
SHUUP_BASKET_STORAGE_CLASS_SPEC = "shuup.core.basket.storage:DatabaseBasketStorage"
SHUUP_BASKET_CLASS_SPEC = "shuup.core.basket.objects:Basket"
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'shuup.xtheme.middleware.XthemeMiddleware',
]
