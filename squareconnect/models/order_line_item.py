# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class OrderLineItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, quantity=None, note=None, catalog_object_id=None, variation_name=None, modifiers=None, taxes=None, discounts=None, base_price_money=None, gross_sales_money=None, total_tax_money=None, total_discount_money=None, total_money=None):
        """
        OrderLineItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'quantity': 'str',
            'note': 'str',
            'catalog_object_id': 'str',
            'variation_name': 'str',
            'modifiers': 'list[OrderLineItemModifier]',
            'taxes': 'list[OrderLineItemTax]',
            'discounts': 'list[OrderLineItemDiscount]',
            'base_price_money': 'Money',
            'gross_sales_money': 'Money',
            'total_tax_money': 'Money',
            'total_discount_money': 'Money',
            'total_money': 'Money'
        }

        self.attribute_map = {
            'name': 'name',
            'quantity': 'quantity',
            'note': 'note',
            'catalog_object_id': 'catalog_object_id',
            'variation_name': 'variation_name',
            'modifiers': 'modifiers',
            'taxes': 'taxes',
            'discounts': 'discounts',
            'base_price_money': 'base_price_money',
            'gross_sales_money': 'gross_sales_money',
            'total_tax_money': 'total_tax_money',
            'total_discount_money': 'total_discount_money',
            'total_money': 'total_money'
        }

        self._name = name
        self._quantity = quantity
        self._note = note
        self._catalog_object_id = catalog_object_id
        self._variation_name = variation_name
        self._modifiers = modifiers
        self._taxes = taxes
        self._discounts = discounts
        self._base_price_money = base_price_money
        self._gross_sales_money = gross_sales_money
        self._total_tax_money = total_tax_money
        self._total_discount_money = total_discount_money
        self._total_money = total_money

    @property
    def name(self):
        """
        Gets the name of this OrderLineItem.
        The name of the line item.

        :return: The name of this OrderLineItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrderLineItem.
        The name of the line item.

        :param name: The name of this OrderLineItem.
        :type: str
        """

        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if len(name) > 500:
            raise ValueError("Invalid value for `name`, length must be less than `500`")

        self._name = name

    @property
    def quantity(self):
        """
        Gets the quantity of this OrderLineItem.
        The quantity purchased, as a string representation of a number.

        :return: The quantity of this OrderLineItem.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this OrderLineItem.
        The quantity purchased, as a string representation of a number.

        :param quantity: The quantity of this OrderLineItem.
        :type: str
        """

        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")
        if len(quantity) > 5:
            raise ValueError("Invalid value for `quantity`, length must be less than `5`")
        if len(quantity) < 1:
            raise ValueError("Invalid value for `quantity`, length must be greater than or equal to `1`")

        self._quantity = quantity

    @property
    def note(self):
        """
        Gets the note of this OrderLineItem.
        The note of the line item.

        :return: The note of this OrderLineItem.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this OrderLineItem.
        The note of the line item.

        :param note: The note of this OrderLineItem.
        :type: str
        """

        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")
        if len(note) > 50:
            raise ValueError("Invalid value for `note`, length must be less than `50`")

        self._note = note

    @property
    def catalog_object_id(self):
        """
        Gets the catalog_object_id of this OrderLineItem.
        The [CatalogItemVariation](#type-catalogitemvariation) id applied to this line item.

        :return: The catalog_object_id of this OrderLineItem.
        :rtype: str
        """
        return self._catalog_object_id

    @catalog_object_id.setter
    def catalog_object_id(self, catalog_object_id):
        """
        Sets the catalog_object_id of this OrderLineItem.
        The [CatalogItemVariation](#type-catalogitemvariation) id applied to this line item.

        :param catalog_object_id: The catalog_object_id of this OrderLineItem.
        :type: str
        """

        if catalog_object_id is None:
            raise ValueError("Invalid value for `catalog_object_id`, must not be `None`")
        if len(catalog_object_id) > 192:
            raise ValueError("Invalid value for `catalog_object_id`, length must be less than `192`")

        self._catalog_object_id = catalog_object_id

    @property
    def variation_name(self):
        """
        Gets the variation_name of this OrderLineItem.
        The name of the variation applied to this line item.

        :return: The variation_name of this OrderLineItem.
        :rtype: str
        """
        return self._variation_name

    @variation_name.setter
    def variation_name(self, variation_name):
        """
        Sets the variation_name of this OrderLineItem.
        The name of the variation applied to this line item.

        :param variation_name: The variation_name of this OrderLineItem.
        :type: str
        """

        if variation_name is None:
            raise ValueError("Invalid value for `variation_name`, must not be `None`")
        if len(variation_name) > 255:
            raise ValueError("Invalid value for `variation_name`, length must be less than `255`")

        self._variation_name = variation_name

    @property
    def modifiers(self):
        """
        Gets the modifiers of this OrderLineItem.
        The [CatalogModifier](#type-catalogmodifier)s applied to this line item.

        :return: The modifiers of this OrderLineItem.
        :rtype: list[OrderLineItemModifier]
        """
        return self._modifiers

    @modifiers.setter
    def modifiers(self, modifiers):
        """
        Sets the modifiers of this OrderLineItem.
        The [CatalogModifier](#type-catalogmodifier)s applied to this line item.

        :param modifiers: The modifiers of this OrderLineItem.
        :type: list[OrderLineItemModifier]
        """

        self._modifiers = modifiers

    @property
    def taxes(self):
        """
        Gets the taxes of this OrderLineItem.
        The taxes applied to this line item.

        :return: The taxes of this OrderLineItem.
        :rtype: list[OrderLineItemTax]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """
        Sets the taxes of this OrderLineItem.
        The taxes applied to this line item.

        :param taxes: The taxes of this OrderLineItem.
        :type: list[OrderLineItemTax]
        """

        self._taxes = taxes

    @property
    def discounts(self):
        """
        Gets the discounts of this OrderLineItem.
        The discounts applied to this line item.

        :return: The discounts of this OrderLineItem.
        :rtype: list[OrderLineItemDiscount]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """
        Sets the discounts of this OrderLineItem.
        The discounts applied to this line item.

        :param discounts: The discounts of this OrderLineItem.
        :type: list[OrderLineItemDiscount]
        """

        self._discounts = discounts

    @property
    def base_price_money(self):
        """
        Gets the base_price_money of this OrderLineItem.
        The base price for a single unit of the line item.

        :return: The base_price_money of this OrderLineItem.
        :rtype: Money
        """
        return self._base_price_money

    @base_price_money.setter
    def base_price_money(self, base_price_money):
        """
        Sets the base_price_money of this OrderLineItem.
        The base price for a single unit of the line item.

        :param base_price_money: The base_price_money of this OrderLineItem.
        :type: Money
        """

        self._base_price_money = base_price_money

    @property
    def gross_sales_money(self):
        """
        Gets the gross_sales_money of this OrderLineItem.
        The gross sales amount of money calculated as (item base price + modifiers price) * quantity.

        :return: The gross_sales_money of this OrderLineItem.
        :rtype: Money
        """
        return self._gross_sales_money

    @gross_sales_money.setter
    def gross_sales_money(self, gross_sales_money):
        """
        Sets the gross_sales_money of this OrderLineItem.
        The gross sales amount of money calculated as (item base price + modifiers price) * quantity.

        :param gross_sales_money: The gross_sales_money of this OrderLineItem.
        :type: Money
        """

        self._gross_sales_money = gross_sales_money

    @property
    def total_tax_money(self):
        """
        Gets the total_tax_money of this OrderLineItem.
        The total tax amount of money to collect for the line item.

        :return: The total_tax_money of this OrderLineItem.
        :rtype: Money
        """
        return self._total_tax_money

    @total_tax_money.setter
    def total_tax_money(self, total_tax_money):
        """
        Sets the total_tax_money of this OrderLineItem.
        The total tax amount of money to collect for the line item.

        :param total_tax_money: The total_tax_money of this OrderLineItem.
        :type: Money
        """

        self._total_tax_money = total_tax_money

    @property
    def total_discount_money(self):
        """
        Gets the total_discount_money of this OrderLineItem.
        The total discount amount of money to collect for the line item.

        :return: The total_discount_money of this OrderLineItem.
        :rtype: Money
        """
        return self._total_discount_money

    @total_discount_money.setter
    def total_discount_money(self, total_discount_money):
        """
        Sets the total_discount_money of this OrderLineItem.
        The total discount amount of money to collect for the line item.

        :param total_discount_money: The total_discount_money of this OrderLineItem.
        :type: Money
        """

        self._total_discount_money = total_discount_money

    @property
    def total_money(self):
        """
        Gets the total_money of this OrderLineItem.
        The total amount of money to collect for this line item.

        :return: The total_money of this OrderLineItem.
        :rtype: Money
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money):
        """
        Sets the total_money of this OrderLineItem.
        The total amount of money to collect for this line item.

        :param total_money: The total_money of this OrderLineItem.
        :type: Money
        """

        self._total_money = total_money

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
