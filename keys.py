keys = (
    (0x1, 'VK_LBUTTON', None, 'Left mouse button'),
    (0x2, 'VK_RBUTTON', None, 'Right mouse button'),
    (0x3, 'VK_CANCEL', None, 'Control-break (Ctrl+Pause)'),
    (0x4, 'VK_MBUTTON', None, 'Middle mouse button'),
    (0x5, 'VK_XBUTTON1', None, 'X1 mouse button'),
    (0x6, 'VK_XBUTTON2', None, 'X2 mouse button'),
    (0x8, 'VK_BACK', 'B', 'BACKSPACE'),
    (0x9, 'VK_TAB', 'T', 'TAB'),
    (0xC, 'VK_CLEAR', None, 'CLEAR'),
    (0xD, 'VK_RETURN', 'Y', 'ENTER'),
    # (0x10, 'VK_SHIFT', 'S', 'SHIFT'),
    # (0x11, 'VK_CONTROL', 'C', 'CTRL'),
    # (0x12, 'VK_MENU', 'A', 'ALT'),
    (0x13, 'VK_PAUSE', 'G', 'PAUSE'),
    (0x14, 'VK_CAPITAL', 'K', 'CAPS LOCK'),
    (0x15, 'VK_KANA', None, 'IME Kana mode'),
    (0x15, 'VK_HANGUEL', None, 'IME Hanguel mode'),
    (0x15, 'VK_HANGUL', None, 'IME Hangul mode'),
    (0x17, 'VK_JUNJA', None, 'IME Junja mode'),
    (0x18, 'VK_FINAL', None, 'IME final mode'),
    (0x19, 'VK_HANJA', None, 'IME Hanja mode'),
    (0x19, 'VK_KANJI', None, 'IME Kanji mode'),
    (0x1B, 'VK_ESCAPE', 'Z', 'ESC'),
    (0x1C, 'VK_CONVERT', None, 'IME convert'),
    (0x1D, 'VK_NONCONVERT', None, 'IME nonconvert'),
    (0x1E, 'VK_ACCEPT', None, 'IME accept'),
    (0x1F, 'VK_MODECHANGE', None, 'IME mode change request'),
    (0x20, 'VK_SPACE', 'V', 'SPACEBAR'),
    (0x21, 'VK_PRIOR', 'P', 'PAGE UP'),
    (0x22, 'VK_NEXT', 'Q', 'PAGE DOWN'),
    (0x23, 'VK_END', 'E', 'END'),
    (0x24, 'VK_HOME', 'H', 'HOME'),
    (0x25, 'VK_LEFT', 'L', 'LEFT ARROW'),
    (0x26, 'VK_UP', 'U', 'UP ARROW'),
    (0x27, 'VK_RIGHT', 'R', 'RIGHT ARROW'),
    (0x28, 'VK_DOWN', 'D', 'DOWN ARROW'),
    (0x29, 'VK_SELECT', None, 'SELECT'),
    (0x2A, 'VK_PRINT', None, 'PRINT'),
    (0x2B, 'VK_EXECUTE', None, 'EXECUTE'),
    (0x2C, 'VK_SNAPSHOT', None, 'PRINT SCREEN'),
    (0x2D, 'VK_INSERT', 'I', 'INS'),
    (0x2E, 'VK_DELETE', 'X', 'DEL'),
    (0x2F, 'VK_HELP', None, 'HELP'),
    (0x30, None, '0', '0'),
    (0x31, None, '1', '1'),
    (0x32, None, '2', '2'),
    (0x33, None, '3', '3'),
    (0x34, None, '4', '4'),
    (0x35, None, '5', '5'),
    (0x36, None, '6', '6'),
    (0x37, None, '7', '7'),
    (0x38, None, '8', '8'),
    (0x39, None, '9', '9'),
    (0x41, None, 'a', 'A'),
    (0x42, None, 'b', 'B'),
    (0x43, None, 'c', 'C'),
    (0x44, None, 'd', 'D'),
    (0x45, None, 'e', 'E'),
    (0x46, None, 'f', 'F'),
    (0x47, None, 'g', 'G'),
    (0x48, None, 'h', 'H'),
    (0x49, None, 'i', 'I'),
    (0x4A, None, 'j', 'J'),
    (0x4B, None, 'k', 'K'),
    (0x4C, None, 'l', 'L'),
    (0x4D, None, 'm', 'M'),
    (0x4E, None, 'n', 'N'),
    (0x4F, None, 'o', 'O'),
    (0x50, None, 'p', 'P'),
    (0x51, None, 'q', 'Q'),
    (0x52, None, 'r', 'R'),
    (0x53, None, 's', 'S'),
    (0x54, None, 't', 'T'),
    (0x55, None, 'u', 'U'),
    (0x56, None, 'v', 'V'),
    (0x57, None, 'w', 'W'),
    (0x58, None, 'x', 'X'),
    (0x59, None, 'y', 'Y'),
    (0x5A, None, 'z', 'Z'),
    (0x5B, 'VK_LWIN', 'W', 'Left Windows'),
    (0x5C, 'VK_RWIN', None, 'Right Windows'),
    (0x5D, 'VK_APPS', 'M', 'Applications'),
    (0x5F, 'VK_SLEEP', None, 'Computer Sleep'),
    (0x60, 'VK_NUMPAD0', 'N0', 'Numeric keypad 0'),
    (0x61, 'VK_NUMPAD1', 'N1', 'Numeric keypad 1'),
    (0x62, 'VK_NUMPAD2', 'N2', 'Numeric keypad 2'),
    (0x63, 'VK_NUMPAD3', 'N3', 'Numeric keypad 3'),
    (0x64, 'VK_NUMPAD4', 'N4', 'Numeric keypad 4'),
    (0x65, 'VK_NUMPAD5', 'N5', 'Numeric keypad 5'),
    (0x66, 'VK_NUMPAD6', 'N6', 'Numeric keypad 6'),
    (0x67, 'VK_NUMPAD7', 'N7', 'Numeric keypad 7'),
    (0x68, 'VK_NUMPAD8', 'N8', 'Numeric keypad 8'),
    (0x69, 'VK_NUMPAD9', 'N9', 'Numeric keypad 9'),
    (0x6A, 'VK_MULTIPLY', 'N*', 'Multiply'),
    (0x6B, 'VK_ADD', 'N+', 'Add'),
    (0x6C, 'VK_SEPARATOR', None, 'Separator'),
    (0x6D, 'VK_SUBTRACT', 'N-', 'Subtract'),
    (0x6E, 'VK_DECIMAL', 'N.', 'Decimal'),
    (0x6F, 'VK_DIVIDE', 'N/', 'Divide'),
    (0x70, 'VK_F1', 'F1', 'F1'),
    (0x71, 'VK_F2', 'F2', 'F2'),
    (0x72, 'VK_F3', 'F3', 'F3'),
    (0x73, 'VK_F4', 'F4', 'F4'),
    (0x74, 'VK_F5', 'F5', 'F5'),
    (0x75, 'VK_F6', 'F6', 'F6'),
    (0x76, 'VK_F7', 'F7', 'F7'),
    (0x77, 'VK_F8', 'F8', 'F8'),
    (0x78, 'VK_F9', 'F9', 'F9'),
    (0x79, 'VK_F10', 'F10', 'F10'),
    (0x7A, 'VK_F11', 'F11', 'F11'),
    (0x7B, 'VK_F12', 'F12', 'F12'),
    (0x7C, 'VK_F13', 'F13', 'F13'),
    (0x7D, 'VK_F14', 'F14', 'F14'),
    (0x7E, 'VK_F15', 'F15', 'F15'),
    (0x7F, 'VK_F16', 'F16', 'F16'),
    (0x80, 'VK_F17', 'F17', 'F17'),
    (0x81, 'VK_F18', 'F18', 'F18'),
    (0x82, 'VK_F19', 'F19', 'F19'),
    (0x83, 'VK_F20', 'F20', 'F20'),
    (0x84, 'VK_F21', 'F21', 'F21'),
    (0x85, 'VK_F22', 'F22', 'F22'),
    (0x86, 'VK_F23', 'F23', 'F23'),
    (0x87, 'VK_F24', 'F24', 'F24'),
    (0x90, 'VK_NUMLOCK', 'O', 'NUM LOCK'),
    (0x91, 'VK_SCROLL', 'J', 'SCROLL LOCK'),
    (0xA0, 'VK_LSHIFT', None, 'Left SHIFT'),
    (0xA1, 'VK_RSHIFT', None, 'Right SHIFT'),
    (0xA2, 'VK_LCONTROL', None, 'Left CONTROL'),
    (0xA3, 'VK_RCONTROL', None, 'Right CONTROL'),
    (0xA4, 'VK_LMENU', None, 'Left MENU'),
    (0xA5, 'VK_RMENU', None, 'Right MENU'),
    (0xA6, 'VK_BROWSER_BACK', None, 'Browser Back'),
    (0xA7, 'VK_BROWSER_FORWARD', None, 'Browser Forward'),
    (0xA8, 'VK_BROWSER_REFRESH', None, 'Browser Refresh'),
    (0xA9, 'VK_BROWSER_STOP', None, 'Browser Stop'),
    (0xAA, 'VK_BROWSER_SEARCH', None, 'Browser Search'),
    (0xAB, 'VK_BROWSER_FAVORITES', None, 'Browser Favorites'),
    (0xAC, 'VK_BROWSER_HOME', None, 'Browser Start and Home'),
    (0xAD, 'VK_VOLUME_MUTE', None, 'Volume Mute'),
    (0xAE, 'VK_VOLUME_DOWN', None, 'Volume Down'),
    (0xAF, 'VK_VOLUME_UP', None, 'Volume Up'),
    (0xB0, 'VK_MEDIA_NEXT_TRACK', None, 'Next Track'),
    (0xB1, 'VK_MEDIA_PREV_TRACK', None, 'Previous Track'),
    (0xB2, 'VK_MEDIA_STOP', None, 'Stop Media'),
    (0xB3, 'VK_MEDIA_PLAY_PAUSE', None, 'Play/Pause Media'),
    (0xB4, 'VK_LAUNCH_MAIL', None, 'Start Mail'),
    (0xB5, 'VK_LAUNCH_MEDIA_SELECT', None, 'Select Media'),
    (0xB6, 'VK_LAUNCH_APP1', None, 'Start Application 1'),
    (0xB7, 'VK_LAUNCH_APP2', None, 'Start Application 2'),
    (0xBA, 'VK_OEM_1', ':', 'Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ";:"'),
    (0xBB, 'VK_OEM_PLUS', '+ or =', 'For any country/region, the "+"'),
    (0xBC, 'VK_OEM_COMMA', ', or <', 'For any country/region, the ","'),
    (0xBD, 'VK_OEM_MINUS', '- or _', 'For any country/region, the "-"'),
    (0xBE, 'VK_OEM_PERIOD', '. or >', 'For any country/region, the "."'),
    (0xBF, 'VK_OEM_2', '/ or ?', 'Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the "/?"'),
    (0xC0, 'VK_OEM_3', '` or ~', 'Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the "`~"'),
    (0xDB, 'VK_OEM_4', '[', 'Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the "[{"'),
    (0xDC, 'VK_OEM_5', '\ or |', 'Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the "\|"'),
    (0xDD, 'VK_OEM_6', ']', 'Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the "]}"'),
    (0xDE, 'VK_OEM_7', '\'', 'Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the "single-quote/double-quote"'),
    (0xDF, 'VK_OEM_8', None, 'Used for miscellaneous characters; it can vary by keyboard.'),
    (0xE2, 'VK_OEM_102', None, 'Either the angle bracket key or the backslash key on the RT 102-key keyboard'),
    (0xE5, 'VK_PROCESSKEY', None, 'IME PROCESS'),
    (0xE7, 'VK_PACKET', None, 'Used to pass Unicode characters as if they were keystrokes.'),
    (0xF6, 'VK_ATTN', None, 'Attn'),
    (0xF7, 'VK_CRSEL', None, 'CrSel'),
    (0xF8, 'VK_EXSEL', None, 'ExSel'),
    (0xF9, 'VK_EREOF', None, 'Erase EOF'),
    (0xFA, 'VK_PLAY', None, 'Play'),
    (0xFB, 'VK_ZOOM', None, 'Zoom'),
    (0xFD, 'VK_PA1', None, 'PA1'),
    (0xFE, 'VK_OEM_CLEAR', None, 'Clear')
)

class Key():
    def __init__(self, key):
        self.value = key[0]
        self.vk = key[1]
        self.qm = key[2]
        self.desc = key[3]

def get(value):
    key = next((i for i in keys if i[0] == value), None)
    if key:
        return Key(key)


