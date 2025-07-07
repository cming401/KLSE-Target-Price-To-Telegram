# KLSE Target Price to Telegram

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

An automated monitoring system that tracks Malaysia Stock Exchange (KLSE) price targets and sends formatted updates to Telegram channels.

## 🚀 Features

- 📈 **Smart Sorting**: Displays stocks sorted by highest upside percentage
- 🔄 **Auto Grouping**: Merges multiple price targets for the same stock
- 📱 **Clean Format**: Compact, readable Telegram message format
- ⏰ **Scheduled Updates**: Automated daily runs (Monday to Friday at 6 PM)
- 📊 **Statistics**: Complete summary with buy/hold/sell counts
- 🔧 **Easy Setup**: Simple configuration and deployment

## 📋 Prerequisites

- Python 3.7 or higher
- Telegram Bot Token
- Telegram Channel ID

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cming401/klse-target-price-telegram.git
   cd klse-target-price-telegram
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Telegram settings**
   ```bash
   cp config.json.example config.json
   # Edit config.json with your Telegram credentials
   ```

4. **Test the script**
   ```bash
   python klse_monitor.py
   ```

5. **Set up automated scheduling**
   ```bash
   bash setup_cron.sh
   ```

## ⚙️ Configuration

Create a `config.json` file based on `config.json.example`:

```json
{
    "telegram": {
        "bot_token": "YOUR_BOT_TOKEN",
        "channel_id": "YOUR_CHANNEL_ID",
        "chat_id": "YOUR_CHAT_ID"
    },
    "schedule": {
        "enabled": true,
        "time": "18:00",
        "weekdays_only": true
    }
}
```

### Getting Telegram Credentials

1. **Create a Telegram Bot**:
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Use `/newbot` command
   - Save the bot token

2. **Get Channel ID**:
   - Add your bot to the channel as an administrator
   - Send a message to the channel
   - Visit: `https://api.telegram.org/bot<YourBOTToken>/getUpdates`
   - Find your channel ID in the response

## 📱 Message Format

The bot sends messages in this format:

```
📊 KLSE Target Price Update
🗓️ Date: 2025-01-07

1. 🟢 WCT - WCT HOLDINGS BERHAD
   💰 Current: RM0.68 🎯 Target: RM1.08 📈 Change: +0.40 (58.82%)
   🏢 Analyst: PUBLIC BANK (Buy)

2. 🟢 YINSON - YINSON HOLDINGS BHD
   💰 Current: RM2.41 🎯 Target: RM3.69 📈 Change: +1.28 (53.11%)
   🏢 Analyst: RHB-OSK (Buy)

3. 🟢 MAYBANK - MALAYAN BANKING BHD
   💰 Current: RM9.71 🎯 Target: RM11.40 📈 Change: +1.69 (17.40%)
   🏢 Analyst: TA (Buy)
   💰 Current: RM9.71 🎯 Target: RM10.90 📈 Change: +1.19 (12.26%)
   🏢 Analyst: RHB (Buy)

📊 Daily Summary:
   🟢 Buy: 10 stocks
   🟡 Hold: 2 stocks
   🔴 Sell: 0 stocks
   📈 Total: 12 stocks

🔗 Source: https://klse.i3investor.com/web/pricetarget/latest
```

## 📁 Project Structure

```
klse-target-price-telegram/
├── klse_monitor.py         # Main monitoring script
├── update_data.py          # Manual data update tool
├── setup_cron.sh          # Cron job setup script
├── requirements.txt        # Python dependencies
├── config.json.example    # Configuration template
├── .gitignore             # Git ignore file
├── LICENSE                # MIT License
└── README.md              # This file
```

## 🔄 Manual Data Updates

To manually update stock data:

```bash
python update_data.py
```

Follow the prompts to add new stock information.

## 📅 Scheduling

The system is configured to run Monday to Friday at 6:00 PM.

To modify the schedule:
1. Edit the cron expression in `setup_cron.sh`
2. Run `bash setup_cron.sh` to apply changes

### Useful Commands

```bash
# View active cron jobs
crontab -l

# View logs
tail -f klse_monitor.log

# Manual run
python klse_monitor.py

# Remove cron job
crontab -e  # Then delete the relevant line
```

## 🐛 Troubleshooting

### Common Issues

1. **Telegram API Error**: Verify bot token and channel ID
2. **Permission Error**: Ensure bot is admin in the channel
3. **No Data**: Check internet connection and data source availability

### Debug Mode

Enable verbose logging by setting log level to DEBUG in the script.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Current Stock Coverage

The system currently monitors 12 KLSE stocks with the following breakdown:
- 🟢 **Buy recommendations**: 10 stocks
- 🟡 **Hold recommendations**: 2 stocks
- 🔴 **Sell recommendations**: 0 stocks

## 🔒 Security

- Telegram credentials are stored in a separate config file
- Config file is excluded from version control
- No sensitive information is hardcoded in the scripts

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Acknowledgments

- Data source: [i3investor KLSE Price Targets](https://klse.i3investor.com/web/pricetarget/latest)
- Built for the Malaysian investment community

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above

---

**Disclaimer**: This tool is for informational purposes only. Always do your own research before making investment decisions.