
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

# <sort of PEP8 Compliant, lines are not always 79 chars long>

# We need to import some modules from Blender to actually make an adodn. 

import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty

# for more info on the bl_info structure see
# https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo#Script_Meta_Info

bl_info = {
    "name": "Blender Addon Starter",
    "author": "www.crowd-render.com",
    "version": (0, 0, 0),
    "blender": (2, 80, 0),
    "location": "Object Data",
    "description": "A simple example of a Blender addon",
    "wiki_url": "www.crowd-render.com",
    "category": "Render",
    "support": "COMMUNITY"
}

# Suppose we better support some kind of preferences?
# more on this here -> https://docs.blender.org/api/current/bpy.types.AddonPreferences.html?highlight=bl_info

#imports from this director
from src import bl_ui
from src import bl_properties
from src import main

class ExampleAddonPreferences(AddonPreferences):
    # this must match the add-on name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    #let's have a path where we can store things, like grunge maps
    filepath: StringProperty(
        name="Example File Path",
        subtype='FILE_PATH',
    )

    def draw(self, context: bpy.context) -> None:
        layout = self.layout
        layout.label(text="This is a preferences view for our add-on")
        layout.prop(self, "filepath")

def register():
    bpy.utils.register_class(ExampleAddonPreferences)
    bl_properties.register()
    bl_ui.register()
    main.register()


def unregister():
    bpy.utils.register_class(ExampleAddonPreferences)
    bl_ui.unregister()
    main.unregister()