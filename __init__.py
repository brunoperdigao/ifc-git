import os
import sys
import bpy

sys.path.insert(0, "/home/bruno/src/ifc-git")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import operators
from operators import (
    AddFileToRepo,
    CommitChanges,
    CreateRepo,
    DiscardUncommitted,
    DisplayRevision,
    DisplayUncommitted,
    Merge,
    RefreshGit,
    SwitchRevision,
)
import ui
from ui import IFCGIT_PT_panel, COMMIT_UL_List
import prop
from prop import IfcGitListItem, IfcGitProperties


# import ui, prop, operator

classes = (
    operators.AddFileToRepo,
    operators.CommitChanges,
    operators.CreateRepo,
    operators.DiscardUncommitted,
    operators.DisplayRevision,
    operators.DisplayUncommitted,
    operators.Merge,
    operators.RefreshGit,
    operators.SwitchRevision,
    prop.IfcGitListItem,
    prop.IfcGitProperties,
    ui.IFCGIT_PT_panel,
    ui.COMMIT_UL_List,
)

bl_info = {
    "name": "IFC Git",
    "author": "Bruno Postle",
    "location": "Scene > IFC Git",
    "description": "Manage IFC files in Git repositories",
    "blender": (2, 80, 0),
    "category": "Import-Export",
}

#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# 2023 Bruno Postle <bruno@postle.net>


def register():
    bpy.utils.register_class(IFCGIT_PT_panel)
    bpy.utils.register_class(IfcGitListItem)
    bpy.utils.register_class(IfcGitProperties)
    bpy.utils.register_class(COMMIT_UL_List)
    bpy.utils.register_class(CreateRepo)
    bpy.utils.register_class(AddFileToRepo)
    bpy.utils.register_class(DiscardUncommitted)
    bpy.utils.register_class(CommitChanges)
    bpy.utils.register_class(RefreshGit)
    bpy.utils.register_class(DisplayRevision)
    bpy.utils.register_class(DisplayUncommitted)
    bpy.utils.register_class(SwitchRevision)
    bpy.utils.register_class(Merge)
    bpy.types.Scene.IfcGitProperties = bpy.props.PointerProperty(type=prop.IfcGitProperties)


def unregister():
    del bpy.types.Scene.ifcgit_commits
    del bpy.types.Scene.commit_index
    del bpy.types.Scene.commit_message
    del bpy.types.Scene.new_branch_name
    del bpy.types.Scene.display_branch
    del bpy.types.Scene.ifcgit_filter
    bpy.utils.unregister_class(IFCGIT_PT_panel)
    bpy.utils.unregister_class(IfcGitListItem)
    bpy.utils.unregister_class(IfcGitProperties)
    bpy.utils.unregister_class(COMMIT_UL_List)
    bpy.utils.unregister_class(CreateRepo)
    bpy.utils.unregister_class(AddFileToRepo)
    bpy.utils.unregister_class(DiscardUncommitted)
    bpy.utils.unregister_class(CommitChanges)
    bpy.utils.unregister_class(RefreshGit)
    bpy.utils.unregister_class(DisplayRevision)
    bpy.utils.unregister_class(DisplayUncommitted)
    bpy.utils.unregister_class(SwitchRevision)
    bpy.utils.unregister_class(Merge)
    del bpy.types.Scene.IfcGitProperties

if __name__ == "__main__":
    register()
