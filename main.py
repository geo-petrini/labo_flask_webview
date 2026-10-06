import webview
from app import app


if __name__ == '__main__':
    window_config = {
        'transparent':False,
        'frameless':True,
        'easy_drag':True,
        'width':300,
        'height':200,
        'url':app
    }
    
    webview.create_window('Webview', **window_config)
    webview.start(icon=None)