#!/usr/bin/env python3
"""
Manual Data Update Tool for KLSE Target Price Monitor
Allows users to manually input new target price data.

Author: cming401
License: MIT
"""

import json
import datetime
from typing import List, Dict
from klse_monitor import KLSETargetPriceMonitor


def update_data_from_input():
    """Update data from user input."""
    print("📝 KLSE Target Price Data Update Tool")
    print("=" * 40)
    
    today = datetime.date.today().strftime('%Y-%m-%d')
    print(f"📅 Today's date: {today}")
    print()
    
    data_list = []
    
    while True:
        print(f"Enter data for stock #{len(data_list) + 1} (type 'q' to quit):")
        
        stock_code = input("Stock code (e.g., MAYBANK): ").strip()
        if stock_code.lower() == 'q':
            break
        
        stock_name = input("Company name (e.g., MALAYAN BANKING BHD): ").strip()
        current_price = input("Current price (e.g., 9.71): ").strip()
        target_price = input("Target price (e.g., 10.90): ").strip()
        upside_downside = input("Change (e.g., +1.19 (12.26%)): ").strip()
        price_call = input("Recommendation (BUY/HOLD/SELL): ").strip().upper()
        analyst = input("Analyst (e.g., RHB): ").strip()
        
        data_list.append({
            'date': today,
            'stock_code': stock_code,
            'stock_name': stock_name,
            'current_price': current_price,
            'target_price': target_price,
            'upside_downside': upside_downside,
            'price_call': price_call,
            'analyst': analyst
        })
        
        print(f"✅ Added {stock_code}")
        print()
    
    if data_list:
        # Save to file
        filename = f"klse_data_{today}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.datetime.now().isoformat(),
                'date': today,
                'data': data_list
            }, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Data saved to {filename}")
        print(f"📊 Total records saved: {len(data_list)}")
        
        # Show preview
        print("\n📋 Data preview:")
        for i, item in enumerate(data_list, 1):
            print(f"{i}. {item['stock_code']} - {item['stock_name']}")
            print(f"   Current: RM{item['current_price']} -> Target: RM{item['target_price']}")
            print(f"   Change: {item['upside_downside']}, Recommendation: {item['price_call']}")
            print()
        
        # Ask if user wants to send to Telegram
        send_now = input("Send to Telegram now? (y/n): ").strip().lower()
        if send_now == 'y':
            try:
                monitor = KLSETargetPriceMonitor()
                
                # Override the sample data method
                monitor.get_sample_data = lambda: data_list
                
                # Send message
                message = monitor.format_message(data_list)
                success = monitor.send_to_telegram(message)
                
                if success:
                    print("✅ Message sent to Telegram channel")
                else:
                    print("❌ Failed to send message. Check your configuration.")
            except Exception as e:
                print(f"❌ Error sending to Telegram: {e}")
    
    else:
        print("❌ No data entered")


if __name__ == "__main__":
    update_data_from_input()