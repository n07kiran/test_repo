class LOGIN:
    USERNAME_LOCATOR = 'div#login-form form input[name = "email"]'
    PASSWORD_LOCATOR = 'div#login-form form input[name = "password"]'
    SIGNIN_LOCATOR = 'div#login-form form button[type = "submit"]'


class SECTION:
    #LOCATOR = "div.toc-container div.accordion div.card div.collapse div.card-body"
    LOCATOR = "div.card-body"


class WEBPAGE:
    LOCATOR = "ul li a"

class VIDEO:
    PLAY_BUTTON = 'button.vjs-big-play-button'
    TRACK = 'div.vjs-text-track-display'
    VIDEO = 'video.vjs-tech'