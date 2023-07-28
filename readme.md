# StarRailAuto
*Editing*<br>
*Developing*<br><br>
This is a project for the game 'StarRail'<br>
In order to free the player from the boring and repetitive work of the game, this project is designed to automatically complete the work of the game.<br>
The project is still under *development*, and the current version is not yet available.<br>

## Features

- Feature 1: Launch the game and log in automatically
- Feature 2: Monthly card automatic renewal
- Feature 3: Daily tasks(developing)
- ...

## Getting Started

### Prerequisites

- Python 3.8 or above

### Installation


1. Clone the repository
    ```
    git clone https://github.com/Athsus/StarRailAuto.git
    ```
2. Install the required packages
    ```
    cd StarRailAuto
    pip install -r requirements.txt
    ```
3. Run the application
    ```
    python main.py
    ```

## Usage

1. Open Task Scheduler (you can search for "Task Scheduler" in the start menu).
2. In the Actions panel on the right, select Create Basic Task....
3. In the Create Basic Task Wizard, give the task a name (for example, "StarRailAuto Daily Task") and click Next.
4. In the 'Trigger' step, select 'Daily' and click 'Next'.
5. In the "Daily" step, set the start time of the task, and set "Every" to 1 day, and then click "Next".
6. In the Action step, select Start a program, and then click Next.
7. In the "Start Program" step, click "Browse..." and select the path to the Python interpreter. Enter main.py in "Add parameter", fill in the folder path where main.py is located in "Start in (optional)", and click "Next".
8. On the 'Finish' step, confirm your settings and click 'Finish.'

If your computer is not powered on all day, you may need to set an automatic power-on time in the BIOS settings. The specific setting steps vary depending on the motherboard of the computer. Usually, you need to press a specific key (such as F2, F10, DEL, etc.) Find the "Auto Power On" or "Scheduled Power On" settings in the Please refer to your motherboard or computer's user manual for details.

## Unfinished Features
Here's what this project doesn't intend to do
1. Recharge monthly card and big monthly card: <br>
Although the original intention is to free your hands, you still have to do it yourself for the monthly card.
2. Automatic map running, including the simu-universe: <br>
There is a project next door that is developing this content. Considering that the map running has low income, heavy workload, and it is also the result of other people's existing work, so I don't plan to do this part.

## Contributing
*Not yet sure*<br>
Auto-generated contributing guidelines
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Au Yu - argonrythm@gmail.com

Project Link: [https://github.com/Athsus/StarRailAuto](https://github.com/Athsus/StarRailAuto)

## References
隔壁做得很好的项目: <br>
https://github.com/Starry-Wind/StarRailAssistant
