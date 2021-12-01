# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group
)


def load_arguments(self, _):

    with self.argument_context('disk-pool') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('availability_zones', nargs='+', help='Logical zone for Disk Pool resource.')

    with self.argument_context('disk-pool list-skus') as c:
        c.argument('location', required=True, arg_type=get_location_type(self.cli_ctx))

    with self.argument_context('disk-pool list-zones') as c:
        c.argument('location', required=True, arg_type=get_location_type(self.cli_ctx))
