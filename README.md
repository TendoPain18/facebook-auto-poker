# Facebook Auto Poker Bot 🤖👆

![thumbnail](images/thumbnail.png)

## ⚔️ The Origin Story

So there was this poking war going on between me and my friends on Facebook.

The rules were simple — you get poked, you poke back. First one to give up loses.

The problem? They had time. I had **Python**.

While they were sitting there manually hitting "Poke Back" like peasants, I built my weapon — an automated bot that never sleeps, never forgets, and never loses a poke war. 🏆

You poke me? My script pokes you back within 5 minutes. At 3 AM. While I'm asleep. They never stood a chance.

## 📋 Description

A Python automation script that monitors your Facebook Pokes page and automatically pokes back a predefined list of friends whenever they poke you. It runs in a continuous loop, refreshing every 5 minutes to check for new pokes, and logs all activity with timestamps to the console.

## ✨ Features

- **Auto Poke Back**: Automatically pokes back friends from your defined list
- **Selective Targeting**: Only pokes back accounts in your configured list
- **Continuous Monitoring**: Checks for new pokes every 5 minutes
- **Activity Logging**: Prints timestamped logs for every poke sent and received
- **Firefox Support**: Uses Firefox WebDriver for browser automation

## 🚀 Getting Started

### Prerequisites

```
Python 3.7+
Firefox Browser
geckodriver (Firefox WebDriver)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/TendoPain18/facebook-auto-poker.git
cd facebook-auto-poker
```

2. **Install dependencies**
```bash
pip install selenium
```

3. **Download geckodriver**
   - Download from [Mozilla geckodriver releases](https://github.com/mozilla/geckodriver/releases)
   - Add it to your system PATH

### Usage

1. **Configure your poke list** in `main.py`
```python
poke_bad_list = ["Friend Name 1", "Friend Name 2", "Friend Name 3"]
```

2. **Run the script**
```bash
python main.py
```

3. **Log in manually** when the Firefox browser opens Facebook, then press **Enter** in the terminal to continue.

4. The script will navigate to your Pokes page and start monitoring automatically.

## 📊 How It Works

1. Opens Firefox and navigates to Facebook
2. Waits for you to log in manually, then press Enter
3. Navigates to the Facebook Pokes page
4. Scans all visible poke entries for names matching your list
5. Pokes back any matching accounts and logs the action
6. Refreshes every 5 minutes and repeats

**Console Output Example:**
```
Mohamed Gad Poked Me At (2 hours ago)
I Poked Mohamed Gad Back! At (Mon Mar 4 14:32:10 2024)

--------------------------------------------------------------------------
Refreshed At (Mon Mar 4 14:37:10 2024)
--------------------------------------------------------------------------
```

## ⚠️ Disclaimer

This script is for educational purposes. Use it responsibly and in accordance with [Facebook's Terms of Service](https://www.facebook.com/terms.php). Automated interactions may violate platform policies.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Selenium WebDriver](https://www.selenium.dev/)

## <!-- CONTACT -->
<!-- END CONTACT -->
