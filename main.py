import sys
import time
import traceback

import pyuac

from SRA import SRA
from _utils.log import log
from daily_missions.daily_mission_generator import DailyGenerator

if __name__ == "__main__":

    sra = SRA()
    try:
        # ======启动======
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
        else:
            sra.set_config()

            # 启动游戏
            sra.start_game()

            log.debug("start test")

            # 等待游戏窗口出现
            sra.wait_game_window()
            sra.get_width()

            # 日常数据
            daily_generator = DailyGenerator()
            daily_data = daily_generator.get_daily_mission()

            # 等待游戏进入
            sra.wait_index()
            # 执行日常
            sra.daily_mission(daily_data)


            # 哈哈哈猜猜这行谁写的嘿嘿
    except KeyboardInterrupt:
        log.error("Exit by user")
    except Exception as e:
        log.error(traceback.format_exc())
    finally:
        # sra.close()
        input()

