import win32evtlog  # For reading Windows event logs
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Directories
report_dir = 'reports'
os.makedirs(report_dir, exist_ok=True)

def fetch_system_logs(log_type='System', event_types=[1, 2, 3, 4, 5]):
    """ Fetch logs from Windows Event Viewer """
    server = 'localhost'  # Local machine
    log = log_type        # Log type: System, Application, Security

    hand = win32evtlog.OpenEventLog(server, log)
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    events = []
    
    while True:
        events_list = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
        if not events_list:
            break
        for event in events_list:
            if event.EventType in event_types:
                events.append({
                    'TimeGenerated': event.TimeGenerated.Format(),
                    'SourceName': event.SourceName,
                    'EventID': event.EventID,
                    'EventType': event.EventType,
                    'Message': str(event.StringInserts)
                })
    return events

def process_and_generate_report(events):
    """ Process events and generate reports """
    if not events:
        print("No system logs found for the given filters.")
        return
    
    df = pd.DataFrame(events)

    # Save to Excel
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = os.path.join(report_dir, f"system_log_report_{timestamp}.xlsx")
    df.to_excel(report_file, index=False)
    
    # Plot Event Type Counts
    df['EventType'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('System Event Type Count')
    plt.xlabel('Event Type')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.tight_layout()

    # Save the chart
    chart_file = os.path.join(report_dir, f"system_log_chart_{timestamp}.png")
    plt.savefig(chart_file)
    plt.close()

    print(f"Report and chart saved in '{report_dir}'.")

# Run the process
events = fetch_system_logs()
process_and_generate_report(events)
