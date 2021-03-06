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

    API for managing persistent device connections. Intended for use by the web GUI   # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@mender.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from management_api.api.management_api_client import ManagementAPIClient

# import ApiClient
from management_api.api_client import ApiClient
from management_api.configuration import Configuration
from management_api.exceptions import OpenApiException
from management_api.exceptions import ApiTypeError
from management_api.exceptions import ApiValueError
from management_api.exceptions import ApiKeyError
from management_api.exceptions import ApiException
# import models into sdk package
from management_api.models.device_state import DeviceState
from management_api.models.error import Error

