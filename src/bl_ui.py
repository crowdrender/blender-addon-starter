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
from bpy.types import Panel

class ButtonsPanel:
    # This addon shows a panel in the 'data' tab of Blender's 'properties' window 
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        engine = context.engine
        return context.object and (engine in cls.COMPAT_ENGINES)


class DATA_PT_Addon_Starter(ButtonsPanel, Panel):
    bl_label = "Blender Addon Starter Panel"
    
    # Specify with which render engines this addon works
    COMPAT_ENGINES = {'CYCLES', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        cam = context.camera
        # use layout.prop to 'draw' a ui element for the property
        layout.prop(cam, 'blender_starter_addon_use')
        layout.prop(cam, 'blender_starter_addon_amount')

def register():
    bpy.utils.register_class(DATA_PT_Addon_Starter)

def unregister():
    bpy.utils.unregister_class(DATA_PT_Addon_Starter)