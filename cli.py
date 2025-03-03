import argparse
from logmate import log

def main():
    parser = argparse.ArgumentParser(description="LogMate - Smart Log Management CLI")
    parser.add_argument("--level", help="Filter logs by level (INFO, WARNING, ERROR)")
    parser.add_argument("--keywords", help="Comma-separated list of keywords")
    parser.add_argument("--since_hours", type=int, help="Filter logs from the last N hours")
    parser.add_argument("--export_json", help="Export logs to a JSON file")
    parser.add_argument("--export_csv", help="Export logs to a CSV file")
    args = parser.parse_args()

    extracted_logs = log.extract_logs(
        "logmate.log",
        level=args.level,
        since_hours=args.since_hours,
        keywords=args.keywords.split(",") if args.keywords else None,
        export_file=args.export_json,
        export_csv=args.export_csv
    )

    print("\nExtracted Logs:")
    for entry in extracted_logs:
        print(entry)

if __name__ == "__main__":
    main()

