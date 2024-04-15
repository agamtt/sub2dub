# pip install pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import sys
import os


mltfile = "ep_1.mlt"

shotcut_exe = r"C:\Program Files\Shotcut\shotcut.exe"
project_folder = r"C:\Users\girin\Desktop\이누야샤_영상\shotcut_프로젝트\자동편집_수동검수"

full_path_to_mlt = os.path.join(project_folder, mltfile)
app = Application(backend="uia").start(f'"{shotcut_exe}" "{full_path_to_mlt}"')
dig = app['Untitled - Shotcut']
dig["Export"].click()
dig["Export File"].click()

#dig.print_control_identifiers()
#input("Press Enter to exit...")
input("wait...")

