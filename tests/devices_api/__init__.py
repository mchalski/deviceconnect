# Copyright 2021 Northern.tech AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# coding: utf-8

# flake8: noqa

"""
    Device Connect

    Device facing API for managing persistent device connections.   # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@mender.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from devices_api.api.devices_api_client import DevicesAPIClient

# import ApiClient
from devices_api.api_client import ApiClient
from devices_api.configuration import Configuration
from devices_api.exceptions import OpenApiException
from devices_api.exceptions import ApiTypeError
from devices_api.exceptions import ApiValueError
from devices_api.exceptions import ApiKeyError
from devices_api.exceptions import ApiException
# import models into sdk package
from devices_api.models.error import Error

