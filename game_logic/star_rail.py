import ctypes
import subprocess
import time
import os

import psutil
from _utils.log import log
import pygetwindow as gw
from PIL import ImageGrab

from _utils.config import init_config_file, modify_json_file, normalize_file_path, CONFIG_FILE_NAME


class StarRail:
    """Game process"""
    def __init__(self, game_path):
        self.game_path = game_path
        try:
            # 获取title的process
            self.process = [p for p in psutil.process_iter() if p.name() == "StarRail.exe"][0]
        except IndexError:
            self.process = None
        self.is_focused = False

        self.window_rect = None
        self.window = None

    def get_width(self, title="崩坏：星穹铁道"):
        """Get the width of the game window"""
        log.debug("Getting window...")
        while True:
            try:
                window = gw.getWindowsWithTitle(title)[0]
                self.window = window
                break
            except IndexError:
                time.sleep(0.5)

        hwnd = window._hWnd

        # 获取活动窗口的大小
        window_rect = window.width, window.height
        self.window_rect = window_rect

        user32 = ctypes.windll.user32
        desktop_width = user32.GetSystemMetrics(0)
        desktop_height = user32.GetSystemMetrics(1)

        # 单显示器屏幕宽度和高度:
        img = ImageGrab.grab()
        width, height = img.size

        scaling = round(width / desktop_width * 100) / 100
        """    
        # 获取当前显示器的缩放比例
        dc = win32gui.GetWindowDC(hwnd)
        dpi_x = win32print.GetDeviceCaps(dc, win32con.LOGPIXELSX)
        dpi_y = win32print.GetDeviceCaps(dc, win32con.LOGPIXELSY)
        win32gui.ReleaseDC(hwnd, dc)
        scale_x = dpi_x / 96
        scale_y = dpi_y / 96
        log.info(f"Real : {width} x {height} {dc} x {dc}")
        """

        # 计算出真实分辨率
        real_width = int(window_rect[0])
        real_height = int(window_rect[1])
        borderless = True if real_width * scaling == 1920 else False
        left_border = (real_width * scaling - 1920) / 2
        up_border = (real_height * scaling - 1080) - left_border
        real_width1 = 1920
        real_height1 = 1080
        if not normalize_file_path(CONFIG_FILE_NAME):
            init_config_file(real_width=real_width1, real_height=real_height1)

        log.info(f"Real resolution: {real_width} x {real_height} x {scaling} x {borderless}")

        modify_json_file(CONFIG_FILE_NAME, "real_width", real_width1)
        modify_json_file(CONFIG_FILE_NAME, "real_height", real_height1)
        modify_json_file(CONFIG_FILE_NAME, "scaling", scaling)
        modify_json_file(CONFIG_FILE_NAME, "borderless", borderless)
        modify_json_file(CONFIG_FILE_NAME, "left_border", left_border)
        modify_json_file(CONFIG_FILE_NAME, "up_border", up_border)

    def launch_game(self):
        """Launches the game launcher and starts the game."""
        subprocess.Popen(self.game_path, shell=True)

        TIMEOUT = 30
        start_time = time.time()
        while time.time() - start_time < TIMEOUT:
            for p in psutil.process_iter():
                if p.name() == "StarRail.exe":
                    try:
                        self.process = psutil.Process(p.pid)
                        log.info("Game launched.")
                        return True
                    except Exception as e:
                        log.error(e.__traceback__)
            time.sleep(1)
        return False

    def terminate(self, force_terminate=False) -> bool:
        """Terminate the game process"""
        if force_terminate:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == "StarRail.exe":
                    proc.terminate()
                    return True
            return False

        if self.process.is_running:
            self.process.terminate()
            self.process.wait()
            return True
        return False

    def is_running(self) -> bool:
        """Check if the game process"""
        return self.process.is_running

