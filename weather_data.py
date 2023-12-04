import argparse
from Reports import Reports


def main():
    weather = Reports()
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", required=False, help="Annual Report")
    parser.add_argument("-a", required=False, help="Monthly Report")
    parser.add_argument("-c", required=False, help="Bar Chart Report")

    args = parser.parse_args()

    if args.e:
        year = int(args.e)
        weather.annual_report(year)
    if args.a:
        year, month = args.a.split("/")
        weather.monthly_report(int(year), int(month))
    if args.c:
        year, month = args.c.split("/")
        weather.bar_chart_report(int(year), int(month))


if __name__ == "__main__":
    main()
