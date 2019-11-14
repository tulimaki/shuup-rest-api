# -*- coding: utf-8 -*-
# This file is part of Shuup REST API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from shuup_rest_api.views.address import MutableAddressViewSet
from shuup_rest_api.views.attribute import AttributeViewSet
from shuup_rest_api.views.basket import BasketViewSet
from shuup_rest_api.views.category import CategoryViewSet
from shuup_rest_api.views.contact_group import ContactGroupViewSet
from shuup_rest_api.views.contact_group_price_display import (
    ContactGroupPriceDisplayViewSet
)
from shuup_rest_api.views.contacts import ContactViewSet, PersonContactViewSet
from shuup_rest_api.views.customer_group_pricing import CgpPriceViewSet
from shuup_rest_api.views.front_orders import FrontOrderViewSet
from shuup_rest_api.views.front_passwords import (
    PasswordResetViewSet, SetPasswordViewSet
)
from shuup_rest_api.views.front_products import (
    FrontProductViewSet, FrontShopProductViewSet
)
from shuup_rest_api.views.front_users import FrontUserViewSet
from shuup_rest_api.views.manufacturer import ManufacturerViewSet
from shuup_rest_api.views.orders import OrderViewSet
from shuup_rest_api.views.product_media import ProductMediaViewSet
from shuup_rest_api.views.product_variation import (
    ProductVariationVariableValueViewSet, ProductVariationVariableViewSet
)
from shuup_rest_api.views.products import (
    ProductAttributeViewSet, ProductPackageViewSet, ProductTypeViewSet,
    ProductViewSet, ShopProductViewSet
)
from shuup_rest_api.views.shipments import ShipmentViewSet
from shuup_rest_api.views.shop import ShopViewSet
from shuup_rest_api.views.suppliers import SupplierViewSet
from shuup_rest_api.views.tax import TaxViewSet
from shuup_rest_api.views.tax_class import TaxClassViewSet
from shuup_rest_api.views.units import SalesUnitViewSet
from shuup_rest_api.views.users import UserViewSet


def populate_api(router):
    """
    :param router: Router
    :type router: rest_framework.routers.DefaultRouter
    """
    router.register("shuup/address", MutableAddressViewSet)
    router.register("shuup/attribute", AttributeViewSet)
    router.register("shuup/category", CategoryViewSet)
    router.register("shuup/contact", ContactViewSet)
    router.register("shuup/contact_group", ContactGroupViewSet)
    router.register("shuup/contact_group_price_display", ContactGroupPriceDisplayViewSet)
    router.register("shuup/order", OrderViewSet)
    router.register("shuup/person_contact", PersonContactViewSet)
    router.register("shuup/product", ProductViewSet)
    router.register("shuup/product_attribute", ProductAttributeViewSet)
    router.register("shuup/product_media", ProductMediaViewSet)
    router.register("shuup/product_type", ProductTypeViewSet)
    router.register("shuup/product_package", ProductPackageViewSet)
    router.register("shuup/product_variation_variable", ProductVariationVariableViewSet)
    router.register("shuup/product_variation_variable_value", ProductVariationVariableValueViewSet)
    router.register("shuup/shipment", ShipmentViewSet)
    router.register("shuup/shop", ShopViewSet)
    router.register("shuup/shop_product", ShopProductViewSet)
    router.register("shuup/manufacturer", ManufacturerViewSet)
    router.register("shuup/supplier", SupplierViewSet)
    router.register("shuup/user", UserViewSet)
    router.register("shuup/sales_unit", SalesUnitViewSet)
    router.register("shuup/tax", TaxViewSet)
    router.register("shuup/tax_class", TaxClassViewSet)
    router.register("shuup/basket", BasketViewSet)

    router.register("shuup/front/user", FrontUserViewSet)
    router.register("shuup/front/password", SetPasswordViewSet, 'set_password')
    router.register("shuup/front/password/reset", PasswordResetViewSet, 'password_reset')
    router.register("shuup/front/orders", FrontOrderViewSet)
    router.register("shuup/front/shop_products", FrontShopProductViewSet)
    router.register("shuup/front/products", FrontProductViewSet)

    router.register("shuup/cgp_price", CgpPriceViewSet)
