import bpy
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

print(argv)
frame = int(argv[0])
input_path = argv[1]
output_path = argv[2]


bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.fbx( filepath = input_path )
bpy.context.scene.frame_set(frame)
bpy.ops.export_mesh.stl( filepath = output_path)