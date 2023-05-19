import os
import sys

os.system("chcp 65001")

import bpy

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def main(args):
    #转换处理
    print(args)
    ply_file = args.get('--ply_file')
    target_blend_file = args.get('--target_blend_file')
    bpy.ops.import_mesh.ply(filepath=ply_file)
    
    #add geometry node
    bpy.ops.object.modifier_add(type='NODES')
    bpy.data.node_groups["Col2VertexColor"].name = "Col2VertexColor"
    
    #add mat
    vert_mat = bpy.data.materials.get("Vert")
    ob = bpy.context.view_layer.objects.active
    if ob.data.materials:
        ob.data.materials[0] = vert_mat
    else:
        ob.data.materials.append(vert_mat)
    
    # del template object
    ob.select_set(False)
    template_object = "example"
    for ob in bpy.context.scene.objects:
        # 如果对象的名称与指定的名称匹配，则将其删除
        if ob.name == template_object:
            bpy.data.objects[template_object].select_set(True)
            bpy.ops.object.delete() 
    
    #save
    bpy.ops.wm.save_as_mainfile(filepath= target_blend_file)
    
    #exit
    # bpy.ops.wm.quit_blender()

if __name__ == '__main__':
    main(getopts(sys.argv))
    print('finish')