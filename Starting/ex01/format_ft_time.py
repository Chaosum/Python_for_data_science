from datetime import datetime


def main():
    now = datetime.now()
    timestamp = now.timestamp()
    print(f"Seconds since January 1, 1970:\
 {timestamp:,.4f} or {timestamp:.2e} \
in scientific notation")
    print(now.strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
