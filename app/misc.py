import ctypes


# https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw
def show_message_box_and_get_button_pressed(text):
    MessageBox = ctypes.windll.user32.MessageBoxW
    btn_pressed = MessageBox(None, text, "Teste Message Box", 3)

    buttons = {
        6: '"SIM"',
        7: '"NÃO"',
        2: '"CANCELAR"',
    }
    print(f'Você pressionou bottão {buttons[btn_pressed]}')

    MessageBox(None, f'Você pressionou bottão {buttons[btn_pressed]}', "Teste Message Box", 0)


# show_message_box_and_get_button_pressed('Ta dáaa!!!')




def pegar_username():
    handle = ctypes.WinDLL('Advapi32.dll')
    error_handle = ctypes.WinDLL('Kernel32.dll')

    username_length = 256
    lpbuffer = 256
    username = ctypes.create_unicode_buffer(username_length)
    pcbBuffer = ctypes.c_ulong(lpbuffer)

    result = handle.GetUserNameW(username, ctypes.byref(pcbBuffer))

    if result <= 0:
        error_code = error_handle.GetLastError()
        print(f'Error code: {error_code}')
        return f'Error code: {error_code}'

    print(username.value)
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, f'O unsuário dono do processo atual é: {username.value}', "Teste Pegar Nome de Usuário", 0)

    return username.value

pegar_username()