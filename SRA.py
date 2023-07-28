import json
import os
import time

import pygetwindow as gw

from _utils.calculated import Calculated
from _utils.config import read_json_file

from constants import IS_INDEX, MANUAL_LOGIN, PWD
from _utils.atomic_operate.img_detector import ImageDetector
from _utils.log import log
from _utils.atomic_operate.clicks import Clicks
from daily_missions.commission import Commission
from game_logic.star_rail import StarRail


class SRA:
    """Application logic control"""

    def __init__(self):
        self.now_path = os.path.abspath(__file__)
        self.now_dir = os.path.dirname(self.now_path)

        self.calculated = None

        self.game_path = ""
        self.game = None

    def set_config(self):
        # ======config======
        try:
            with open(os.path.join(self.now_dir, "config.json"), "r", encoding="utf-8") as f:
                config = json.load(f)
            game_path = config["game_path"]
        except FileNotFoundError:
            config = {}
            log.info("config your game.exe")
            game_path = input()
            config["game_path"] = game_path
            with open(os.path.join(self.now_dir, "config.json"), "w", encoding="utf-8") as f:
                json.dump(config, f)
        except Exception:
            return
        self.game_path = game_path

    def start_game(self):
        """read config and start game"""

        # check if game exists, dont start another game.
        window = gw.getWindowsWithTitle("崩坏：星穹铁道")
        with open(os.path.join(self.now_dir, "config.json"), "r", encoding="utf-8") as f:
            config = json.load(f)
        game_path = config["game_path"]

        if len(window) != 0:
            self.game = StarRail(game_path)
            log.info("game exists.")
            return

        self.game = StarRail(game_path)
        self.game.launch_game()

    def wait_game_window(self, timeout=30):
        # 等待游戏窗口出现, 并且初始化SRA部件(条件为窗口句柄的)
        log.debug("waiting for game window")
        start_time = time.time()
        while time.time() - start_time < timeout:
            time.sleep(1)
            window = gw.getWindowsWithTitle("崩坏：星穹铁道")
            if len(window) == 0:
                continue
            window = window[0]
            # ======init======
            self.calculated = Calculated()
            time.sleep(1)
            return

        raise Exception(f"game not started in {timeout}s")

    def get_width(self):
        self.game.get_width()

    def wait_index(self):
        """
        为了节省资源，就每隔一秒点击
        :return:
        """
        is_index_png = self.calculated.read_img("is_index.png")
        while True:
            self.calculated.Click((10, 10))
            result = self.calculated.scan_screenshot(is_index_png, (90,90,100,100))
            if result["max_val"] > 0.95:
                log.info(f"Login Successfully")
                break
            else:
                log.debug(result["max_val"])

            time.sleep(4)
            # 扫描左上角区域
            pos = self.calculated.ocr_pos("输入")[1]
            if pos:
                log.info("Auto login")
                # 密码登录
                self.calculated.ocr_click("账号", points=(
                    0,
                    self.game.window_rect[1] / 2,
                    self.game.window_rect[0] / 2,
                    self.game.window_rect[1])
                    # self.game.window.left + 0,
                    # self.game.window.top + self.game.window_rect[1] / 2,
                    # self.game.window.right + self.game.window_rect[0] / 2,
                    # self.game.window.bottom + self.game.window_rect[1])
                                               )
                time.sleep(1)
                self.calculated.Click(pos)
                time.sleep(1)
                # pynput.keyboard import Controller, 输入连串数字
                for i in "13668066092":
                    self.calculated.keyboard.press(i)
                    time.sleep(0.5)
                time.sleep(1)
                self.calculated.ocr_click("密码")
                time.sleep(1)
                for i in PWD:
                    self.calculated.keyboard.press(i)
                    time.sleep(0.5)

                time.sleep(1)
                self.calculated.ocr_click("进入")
                return True

            time.sleep(4)

    def daily_mission(self, data):
        """
        日常
        :param data: daily mission
        """

        # 3. 派遣
        window = gw.getWindowsWithTitle("崩坏：星穹铁道")[0]
        commission = Commission(window)
        commission.start()
        # 4. 按照副本刷副本，按照计划150体力
        # 5. 每日任务做完
        # 6. 拿所有奖励
        # *7. 周常任务
        pass

    def to_index(self):
        """
        Try Esc to back to index page.
        :return:
        """
        # todo
        pass

    def close(self):
        if self.game:
            self.game.terminate()
