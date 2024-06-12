# Jetpack Joyride

My project is a recreation of the original “Jetpack Joyride” game by ‘Halfbrick’. The goal is to boost your jetpack and dodge obstacles for as long as you can in a map that increases in speed and difficulty as the game goes on.

## Prerequisites

### Install Python 3.10

Some earlier versions may work, but later versions will not. Follow the steps below to install Python 3.10 and add it to your PATH.

#### On Windows

```sh
1. Download Python 3.10 from the [official website](https://www.python.org/downloads/release/python-3100/).
2. Install Python 3.10 and make sure to check the option "Add Python to PATH" during installation.
3. Verify the installation by opening Command Prompt and typing:
```
   ```sh
   python --version
   ```
   or
   ```sh
   python3.10 --version
   ```
4. If `python3.10` is not recognized, find the installation path:
   ```sh
   where python
   ```
5. Add the path to the environment variables:
   - Open the Start Menu, search for "Environment Variables", and select "Edit the system environment variables".
   - In the System Properties window, click the "Environment Variables" button.
   - In the Environment Variables window, find the `Path` variable in the "System variables" section and select it.
   - Click "Edit", then "New", and add the path to the Python 3.10 directory (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python310`).
   - Click "OK" to close all windows and apply the changes.
6. Close and reopen Command Prompt and verify:
   ```sh
   python3.10 --version
   ```
   NOTE: if this does not work you may also try:
   ```sh
   python --version
   ```
   In this case you may have to use
   ```sh
   python JetpackJoyride.py
   ```
   or use the entire path:
   ```sh
   path/to/python.exe JetpackJoyride.py
   ```
   when RUNNING THE GAME.

#### On macOS and Linux

```sh
1. Download Python 3.10 from the [official website](https://www.python.org/downloads/release/python-3100/).
2. Install Python 3.10.
```
#### SKIP to RUNNING THE GAME and come back if it cannot find python3.10
3. Find the installation path:
   ```sh
   which python3.10
   ```
4. Add the path to your shell profile:
   - Open your shell profile file in a text editor (`~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`):
     ```sh
     nano ~/.bashrc  # for bash
     nano ~/.zshrc   # for zsh
     ```
   - Add the following line:
   - NOTE: replace '/usr/local/bin' with the path from 'which python3.10' command
     ```sh
     export PATH="/usr/local/bin:$PATH"
     ```
   - Save the file and reload your shell configuration:
     ```sh
     source ~/.bashrc  # for bash
     source ~/.zshrc   # for zsh
     ```
5. Verify the installation by opening a terminal and typing:
   ```sh
   python3.10 --version
   ```


## Running the Game

1. Open your terminal.
2. Clone the Repository:
   ```sh
   git clone https://github.com/PinheadPatty/Jetpack-Joyride-Remake.git
   ```
3. Navigate to the Jetpack-Joyride-Remake directory:
   ```sh
   cd Jetpack-Joyride-Remake
   ```
4. Run the python script:
   ```sh
   python3.10 JetpackJoyride.py
   ```

## How to Play

- Click to start.
- Hold ‘space’ to boost and let go to fall.
- Zappers will scroll across the screen.
- Red missiles will give a warning and then go fast at the same height.
- Blue missiles will give a warning and then go slow but track your y position for half of the screen.
- Lasers will move up and down and give a warning before being activated.
- When you die, you will return to the menu, where you can see your best distance and coins (I gave you 1000 to start so you can just buy all of the gadgets/jetpacks).
- Click to unlock and equip any of the 4 gadgets/jetpacks (this will subtract money from your coin bank).
- Equipped gadgets and jetpacks will show up on the character profile on the left side, and in-game, the jetpack will be on and the gadget displayed on the top of the screen.
- The gadgets are:
  - magnetism - increases coin collect radius
  - doubleCoins - increases money per coin to 2
  - gravityBelt - gravity now can be flipped just by tapping ‘space’
  - pathFinder - displays a sequence of green dots that look for a survival path
- To play the game again, simply click play again.
- ENJOY!
