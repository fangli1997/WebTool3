
import urllib.request
import urllib.error
import time
from datetime import datetime

def check_website(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\nChecking: {url}")
    start = time.time()

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "WebPulse/1.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            elapsed = round((time.time() - start) * 1000, 2)

            print("\n[+] Website is ONLINE")
            print(f"[+] Status Code: {response.status}")
            print(f"[+] Response Time: {elapsed} ms")
            print(f"[+] Checked At: {datetime.now()}")

    except urllib.error.HTTPError as error:
        print(f"\n[!] HTTP Error: {error.code}")
    except urllib.error.URLError as error:
        print(f"\n[-] Website is OFFLINE or unreachable")
        print(f"[-] Reason: {error.reason}")
    except TimeoutError:
        print("\n[-] Request timed out")
    except Exception as error:
        print(f"\n[-] Error: {error}")


def main():
    print("=" * 40)
    print("          WEBPULSE v1.0")
    print("       Website Status Checker")
    print("=" * 40)

    while True:
        url = input("\nEnter website URL (or 'exit'): ").strip()

        if url.lower() == "exit":
            print("Thanks for using WebPulse!")
            break

        if not url:
            print("Please enter a valid URL.")
            continue

        check_website(url)


if __name__ == "__main__":
    main()
