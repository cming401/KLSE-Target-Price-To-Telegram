#!/usr/bin/env python3
"""
KLSE Target Price Monitor
A script to monitor Malaysia Stock Exchange price targets and send updates to Telegram.

Author: cming401
License: MIT
"""

import json
import datetime
import logging
import os
import requests
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class KLSETargetPriceMonitor:
    def __init__(self, config_file='config.json'):
        """Initialize the monitor with configuration file."""
        self.config = self.load_config(config_file)
        self.telegram_token = self.config['telegram']['bot_token']
        self.telegram_channel = self.config['telegram']['channel_id']
        self.telegram_chat_id = self.config['telegram']['chat_id']
        
    def load_config(self, config_file: str) -> dict:
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Configuration file {config_file} not found!")
            logger.error("Please copy config.json.example to config.json and configure your settings.")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in configuration file: {e}")
            raise
    
    def get_today_date(self) -> str:
        """Get today's date in YYYY-MM-DD format."""
        return datetime.date.today().strftime('%Y-%m-%d')
    
    def get_sample_data(self) -> List[Dict]:
        """Get sample KLSE target price data."""
        today = self.get_today_date()
        
        # Sample data based on real KLSE targets
        sample_data = [
            {
                'date': today,
                'stock_code': 'ARMADA',
                'stock_name': 'BUMI ARMADA BERHAD',
                'current_price': '0.45',
                'target_price': '0.65',
                'upside_downside': '+0.20 (44.44%)',
                'price_call': 'BUY',
                'analyst': 'RHB-OSK'
            },
            {
                'date': today,
                'stock_code': 'BNASTRA',
                'stock_name': 'BINASTRA CORPORATION BERHAD',
                'current_price': '1.88',
                'target_price': '2.64',
                'upside_downside': '+0.76 (40.43%)',
                'price_call': 'BUY',
                'analyst': 'RHB-OSK'
            },
            {
                'date': today,
                'stock_code': 'GAMUDA',
                'stock_name': 'GAMUDA BHD',
                'current_price': '4.99',
                'target_price': '5.86',
                'upside_downside': '+0.87 (17.43%)',
                'price_call': 'BUY',
                'analyst': 'RHB-OSK'
            },
            {
                'date': today,
                'stock_code': 'GOLDETF',
                'stock_name': 'TRADEPLUS SHARIAH GOLD TRACKER',
                'current_price': '4.34',
                'target_price': '4.78',
                'upside_downside': '+0.44 (10.14%)',
                'price_call': 'HOLD',
                'analyst': 'BIMB'
            },
            {
                'date': today,
                'stock_code': 'IOICORP',
                'stock_name': 'IOI CORPORATION BHD',
                'current_price': '3.76',
                'target_price': '4.05',
                'upside_downside': '+0.29 (7.71%)',
                'price_call': 'HOLD',
                'analyst': 'AmInvest'
            },
            {
                'date': today,
                'stock_code': 'MAYBANK',
                'stock_name': 'MALAYAN BANKING BHD',
                'current_price': '9.71',
                'target_price': '10.90',
                'upside_downside': '+1.19 (12.26%)',
                'price_call': 'BUY',
                'analyst': 'RHB'
            },
            {
                'date': today,
                'stock_code': 'MAYBANK',
                'stock_name': 'MALAYAN BANKING BHD',
                'current_price': '9.71',
                'target_price': '11.40',
                'upside_downside': '+1.69 (17.40%)',
                'price_call': 'BUY',
                'analyst': 'TA'
            },
            {
                'date': today,
                'stock_code': 'MISC',
                'stock_name': 'MISC BHD',
                'current_price': '7.60',
                'target_price': '9.70',
                'upside_downside': '+2.10 (27.63%)',
                'price_call': 'BUY',
                'analyst': 'RHB-OSK'
            },
            {
                'date': today,
                'stock_code': 'MNHLDG',
                'stock_name': 'MN HOLDINGS BERHAD',
                'current_price': '1.40',
                'target_price': '1.69',
                'upside_downside': '+0.29 (20.71%)',
                'price_call': 'BUY',
                'analyst': 'MAYBANK'
            },
            {
                'date': today,
                'stock_code': 'SUNCON',
                'stock_name': 'SUNWAY CONSTRUCTION GROUP BERHAD',
                'current_price': '5.87',
                'target_price': '6.80',
                'upside_downside': '+0.93 (15.84%)',
                'price_call': 'BUY',
                'analyst': 'RHB-OSK'
            },
            {
                'date': today,
                'stock_code': 'WCT',
                'stock_name': 'WCT HOLDINGS BERHAD',
                'current_price': '0.68',
                'target_price': '1.08',
                'upside_downside': '+0.40 (58.82%)',
                'price_call': 'BUY',
                'analyst': 'PUBLIC BANK'
            },
            {
                'date': today,
                'stock_code': 'YINSON',
                'stock_name': 'YINSON HOLDINGS BHD',
                'current_price': '2.41',
                'target_price': '3.69',
                'upside_downside': '+1.28 (53.11%)',
                'price_call': 'BUY',
                'analyst': 'RHB-OSK'
            }
        ]
        
        return sample_data
    
    def fetch_target_prices(self) -> List[Dict]:
        """Fetch KLSE target price data."""
        try:
            logger.info("Fetching KLSE target price data...")
            
            # TODO: Implement actual web scraping here
            # For now, using sample data
            logger.info("Using sample data...")
            data_list = self.get_sample_data()
            
            logger.info(f"Successfully fetched {len(data_list)} target price records")
            return data_list
            
        except Exception as e:
            logger.error(f"Failed to fetch data: {e}")
            return []
    
    def filter_today_data(self, data_list: List[Dict]) -> List[Dict]:
        """Filter data for today's date."""
        today = self.get_today_date()
        today_data = [item for item in data_list if item['date'] == today]
        logger.info(f"Found {len(today_data)} target price records for today ({today})")
        return today_data
    
    def format_message(self, data_list: List[Dict]) -> str:
        """Format data into Telegram message."""
        if not data_list:
            return f"📊 KLSE Target Price Update\n🗓️ Date: {self.get_today_date()}\n\nNo new target prices available"
        
        today = self.get_today_date()
        message = f"📊 KLSE Target Price Update\n🗓️ Date: {today}\n\n"
        
        # Group by stock code
        stock_groups = {}
        for item in data_list:
            stock_code = item.get('stock_code', 'N/A')
            if stock_code not in stock_groups:
                stock_groups[stock_code] = []
            stock_groups[stock_code].append(item)
        
        # Sort groups by highest upside percentage
        sorted_groups = []
        for stock_code, items in stock_groups.items():
            # Find the highest upside for this stock
            max_upside = 0
            for item in items:
                upside_text = item.get('upside_downside', '0')
                if '(' in upside_text:
                    try:
                        upside_pct = float(upside_text.split('(')[1].split('%')[0])
                        max_upside = max(max_upside, upside_pct)
                    except:
                        pass
            sorted_groups.append((max_upside, stock_code, items))
        
        # Sort by upside percentage (descending)
        sorted_groups.sort(key=lambda x: x[0], reverse=True)
        
        for i, (_, stock_code, items) in enumerate(sorted_groups, 1):
            # Get stock name from first item
            stock_name = items[0].get('stock_name', 'N/A')
            
            # Get recommendation emoji from first item
            price_call = items[0].get('price_call', '').upper()
            call_emoji = {
                'BUY': '🟢',
                'HOLD': '🟡',
                'SELL': '🔴'
            }.get(price_call, '⚪')
            
            message += f"{i}. {call_emoji} {stock_code} - {stock_name}\n"
            
            # Add each target price for this stock
            for item in items:
                current_price = item.get('current_price', 'N/A')
                target_price = item.get('target_price', 'N/A')
                upside_text = item.get('upside_downside', '')
                analyst = item.get('analyst', 'N/A')
                price_call_text = item.get('price_call', 'N/A')
                
                # Determine trend emoji
                if '+' in upside_text:
                    trend_emoji = "📈"
                elif '-' in upside_text:
                    trend_emoji = "📉"
                else:
                    trend_emoji = "➡️"
                
                # Convert recommendation to English
                call_english = {
                    'BUY': 'Buy',
                    'HOLD': 'Hold',
                    'SELL': 'Sell'
                }.get(price_call_text.upper(), price_call_text)
                
                message += f"   💰 Current: RM{current_price} 🎯 Target: RM{target_price} {trend_emoji} Change: {upside_text}\n"
                message += f"   🏢 Analyst: {analyst} ({call_english})\n"
            
            message += "\n"
        
        # Add summary statistics
        buy_count = sum(1 for item in data_list if item.get('price_call', '').upper() == 'BUY')
        hold_count = sum(1 for item in data_list if item.get('price_call', '').upper() == 'HOLD')
        sell_count = sum(1 for item in data_list if item.get('price_call', '').upper() == 'SELL')
        
        message += f"📊 Daily Summary:\n"
        message += f"   🟢 Buy: {buy_count} stocks\n"
        message += f"   🟡 Hold: {hold_count} stocks\n"
        message += f"   🔴 Sell: {sell_count} stocks\n"
        message += f"   📈 Total: {len(data_list)} stocks\n\n"
        message += f"🔗 Source: https://klse.i3investor.com/web/pricetarget/latest"
        
        return message
    
    def send_to_telegram(self, message: str) -> bool:
        """Send message to Telegram channel."""
        try:
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            
            data = {
                'chat_id': self.telegram_channel,
                'text': message,
                'parse_mode': 'Markdown',
                'disable_web_page_preview': True
            }
            
            response = requests.post(url, data=data, timeout=10)
            response.raise_for_status()
            
            result = response.json()
            if result.get('ok'):
                logger.info("Message sent successfully to Telegram channel")
                return True
            else:
                logger.error(f"Telegram API error: {result}")
                return False
                
        except requests.RequestException as e:
            logger.error(f"Network error sending Telegram message: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return False
    
    def is_weekday(self) -> bool:
        """Check if today is a weekday."""
        return datetime.date.today().weekday() < 5  # Monday=0, Sunday=6
    
    def run_monitor(self):
        """Execute the monitoring task."""
        try:
            logger.info("Starting KLSE target price monitoring task...")
            
            # Check if today is a weekday
            if not self.is_weekday():
                logger.info("Today is weekend, skipping monitoring")
                return
            
            # Fetch target price data
            all_data = self.fetch_target_prices()
            
            if not all_data:
                logger.warning("No data retrieved")
                return
            
            # Filter today's data
            today_data = self.filter_today_data(all_data)
            
            # Format message
            message = self.format_message(today_data)
            
            # Send to Telegram
            success = self.send_to_telegram(message)
            
            if success:
                logger.info("Monitoring task completed successfully")
            else:
                logger.error("Monitoring task failed")
                
        except Exception as e:
            logger.error(f"Error in monitoring task: {e}")


def main():
    """Main function."""
    monitor = KLSETargetPriceMonitor()
    monitor.run_monitor()


if __name__ == "__main__":
    main()