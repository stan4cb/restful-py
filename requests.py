import settings
import misc

from flask import send_file

def index():
    return "App is running"

def take_picture(): # take picture and return stdout
    out = misc.runProc(settings.cmd_base + settings.p_take_image)
    fileName = misc.findFileNameByExt(out,'jpg')

    if(fileName != 'None'):
        settings.update_l_picture(fileName)
        return send_file(fileName)
    else:
        return 'Camera Error'

def get_preview(): # take and return preview
    misc.runProc(settings.cmd_base + settings.p_take_preview)

    return send_file("preview.jpg")

def get_picture(): # get last taken picture -- not working right now
    return send_file("pic.jpeg")
