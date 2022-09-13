@echo off
if [%1]==[help] goto :help
if [%1]==[--help] goto :help
if [%1]==[?] goto :help
if [%1]==[] goto :err
if [%2]==[] goto :err
if [%3]==[] goto :err
if [%4]==[] goto :err
%1 --background --python fbx_to_stl.py -- %2 %3 %4

:err
echo Some parameters are missing, check docs
exit

:help
echo -------------------------------
echo     Execute this script as
echo -------------------------------
echo      blender.bat {1} {2} {3} {4}
echo      where:
echo            {1} .... path to your blender executable, 
echo                     example: "C:\Program Files\Blender Foundation\Blender 3.2\blender.exe"
echo            {1} .... animation frame to export,
echo                     example: 35
echo            {2} .... input file path (fbx)
echo                     example: "C:\something\something.fbx"
echo            {3} .... output file path (stl)
echo                     example: "C:\something\something.stl"
echo -------------------------------
echo     PREREQUISITES:
echo        -- Blender
echo        -- Python 3
echo        -- https://pypi.org/project/bpy/