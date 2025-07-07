#!/bin/bash

# KLSE Target Price Monitor - Cron Job Setup Script
# Sets up automated daily execution (Monday to Friday at 6 PM)

# Get current script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/klse_monitor.py"
LOG_FILE="$SCRIPT_DIR/klse_monitor.log"

echo "KLSE Target Price Monitor - Cron Job Setup"
echo "==========================================="

# Check if Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script not found: $PYTHON_SCRIPT"
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r "$SCRIPT_DIR/requirements.txt"

# Create log directory
mkdir -p "$(dirname "$LOG_FILE")"

# Set execute permissions
chmod +x "$PYTHON_SCRIPT"

# Create cron job
# Runs daily at 6 PM (Monday to Friday)
CRON_JOB="0 18 * * 1-5 cd $SCRIPT_DIR && python3 $PYTHON_SCRIPT >> $LOG_FILE 2>&1"

echo "Setting up cron job..."
echo "Cron job: $CRON_JOB"

# Backup existing crontab
crontab -l > /tmp/crontab_backup_$(date +%Y%m%d_%H%M%S) 2>/dev/null

# Remove existing KLSE monitor jobs
if crontab -l 2>/dev/null | grep -q "klse_monitor.py"; then
    echo "Removing existing KLSE monitor jobs..."
    crontab -l 2>/dev/null | grep -v "klse_monitor.py" | crontab -
fi

# Add new cron job
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Cron job setup completed!"
echo ""
echo "Job details:"
echo "- Schedule: Daily at 6:00 PM (Monday to Friday)"
echo "- Script: $PYTHON_SCRIPT"
echo "- Log file: $LOG_FILE"
echo ""
echo "Useful commands:"
echo "  View cron jobs:    crontab -l"
echo "  View logs:         tail -f $LOG_FILE"
echo "  Manual run:        python3 $PYTHON_SCRIPT"
echo "  Edit cron jobs:    crontab -e"
echo ""
echo "Next scheduled run: $(date -d 'next Monday 18:00' 2>/dev/null || echo 'Monday at 6:00 PM')"