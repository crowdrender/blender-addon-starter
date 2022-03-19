############################  LICENSE  #########################

# <This software package if for fun>

# Copyright (C) <2022> Crowd Render Pty Limited, Sydney Australia
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# You can contact the creator of Crowdrender at info at
# crowdrender dot com dot au

################################################################
  
import bpy
from bpy.props import (
    BoolProperty,
    FloatProperty
)

def register():
    bpy.types.Object.blender_starter_addon_use = BoolProperty(
        name = "Use Blender Starter Addon",
        description = "Demonstration of a boolean property in Blender",
        default = False,
    )

    bpy.types.Object.blender_starter_addon_amount = FloatProperty(
        name = "Amount",
        description= "Demonstration of a float property in Blender",
        default = 0.5,
        min = 0.0, 
        max = 1.0
    )
