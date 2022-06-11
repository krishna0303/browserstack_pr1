from django.shortcuts import render
import os
import webbrowser
from pywinauto.application import Application  # import pywinauto

# Create your views here.


def home(request):
    return render(request, 'home.html')


def start(request):
    broweser1 = request.GET['browser']
    url1 = request.GET['url']
    print(broweser1)
    print(url1)

    if broweser1 == 'chrome':
        chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
        webbrowser.register(
            'firefox', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('firefox').open(url1, new=2)

    elif broweser1 == 'firefox':

        firefox_path = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        webbrowser.register(
            'firefox', None, webbrowser.BackgroundBrowser(firefox_path))
        webbrowser.get('firefox').open(url1)
    else:
        print('Invalid Browser!')
    return render(request, 'home.html')


def getUrl(request):
    broweser1 = request.GET['browser']
    print(broweser1)
    import webbrowser
    if broweser1 == 'chrome':

        app = Application(backend='uia')
        app.connect(title_re=".*Chrome.*")
        element_name = "Address and search bar"
        dlg = app.top_window()
        # get url from database
        url = dlg.child_window(
            title=element_name, control_type="Edit").get_value()
        print(url)

    elif broweser1 == 'firefox':

        app = Application(backend='uia')
        app.connect(title_re=".*Firefox.*")
        element_name = "Address and search bar"
        dlg = app.top_window()
        # get url from database
        url = dlg.child_window(
            title=element_name, control_type="Edit").get_value()
        print(url)

    else:
        print('Invalid Browser!')
    return render(request, 'home.html')


def stop(request):
    browser1 = request.GET['browser']
    # print(broweser1)
    if browser1 == "chrome":

        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)

    elif browser1 == "firefox":

        browserExe = "firefox.exe"
        os.system("taskkill /f /im "+browserExe)
    else:
        print("This browser isnt available")
    return render(request, 'home.html')


def cleanup(request):
    browser1 = request.GET['browser']
    # print(broweser1)
    if browser1 == "chrome":

        os.system("rm -rf ~/.cache/google-chrome/Default/Cache")
        os.system("rm -rf ~/.cache/google-chrome/Default/")
        os.system("rm -rf ~/.config/google-chrome/")
        os.system("rm -rf ~/.config/google-chrome/Default")

    elif browser1 == "firefox":

        # os.system("rm -rf ~/.cache/mozilla/")
        # os.system("rm ~/.mozilla/firefox/*default/*.sqlite")
        os.system(
            "rm ~/.mozilla/firefox/*.default*/*.sqlite ~/.mozilla/firefox/*default*/sessionstore.js")
        os.system("rm -r ~/.cache/mozilla/firefox/*.default*/*")

    else:
        print("This browser isnt available")
    return render(request, 'home.html')
