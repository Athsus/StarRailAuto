import time

from _utils.calculated import Calculated
from _utils.log import log


class Commission:

    def __init__(self, window):
        self.calculated = Calculated()

    def start(self, commission_count=4):
        """
        Esc
        Click commission
        =====
        COMMISSION
        =====
        Esc
        Esc
        """

        for i in range(commission_count):
            log.info("Try to commission, try {}/{}".format(i + 1, commission_count))
            self.operate_manager.keyboard.press("esc")
            time.sleep(1)
            self.operate_manager.ocr_click("委托")
            time.sleep(1)
            self.operate_manager.ocr_click("领取", overtime=100)
            time.sleep(1)
            self.operate_manager.ocr_click("再次派遣", overtime=100)
        self.operate_manager.keyboard.press("esc")
        time.sleep(1)
        self.operate_manager.keyboard.press("esc")
        return




    def rewards_commission(self):
        """
        part of
        COMMISSION


        """
