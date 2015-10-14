import shelve

settings_file = 'serv_settings'

g_port = 8080

cmd_base = 'gphoto2'
p_take_image = '--auto-detect --capture-image-and-download'
p_take_preview = '--auto-detect --capture-preview --force-overwrite'

last_t_picture = ''

_key_port = 'port'
_key_last_t_picture = 'l_pic'

def load_settings():
    settings = shelve.open(settings_file,writeback=True)

    if(settings.has_key(_key_port)):
        g_port = settings[_key_port]
    else:
        settings[_key_port] = 8080


    if(settings.has_key(_key_last_t_picture)):
        last_t_picture = settings[_key_last_t_picture]

    settings.close()

def update_setting(key,val):
    settings = shelve.open(settings_file,writeback=True)

    settings[key] = val

    settings.close()

def update_l_picture(val):
    update_setting(_key_last_t_picture,val)
