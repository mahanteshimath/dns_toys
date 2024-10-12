# Useful Utilities and Services over DNS - Streamlit App

This Streamlit app provides a simple interface to interact with the creative DNS-based services offered by [dns.toys](https://dns.toys/). The app allows users to run `dig` commands in the background to access various utilities over DNS, such as world time, weather, unit conversions, currency conversions, and much more.

## Features

The app supports the following DNS-based utilities:

1. **World Time**: Fetch the current time of any city.
2. **Timezone Conversion**: Convert time between two cities.
3. **Weather**: Fetch current weather for any city.
4. **Unit Conversion**: Convert between various units (e.g., km to mi, GB to MB).
5. **Currency Conversion**: Convert between currencies with up-to-date exchange rates.
6. **IP Echo**: Fetch your IPv4 or IPv6 address.
7. **Number to Words**: Convert a number to its word representation.
8. **CIDR Range**: Parse CIDR notation to find the first and last usable IP in a subnet.
9. **Number Base Conversion**: Convert numbers between bases (hex, dec, oct, bin).
10. **Pi**: Fetch digits of Pi.
11. **Dictionary**: Get definitions for English words.
12. **Rolling Dice**: Simulate rolling dice (for tabletop RPGs).
13. **Coin Toss**: Simulate tossing coins.
14. **Random Number Generation**: Generate a random number within a specified range.
15. **Epoch/Unix Timestamp Conversion**: Convert a Unix timestamp to a human-readable date.
16. **Aerial Distance**: Calculate the aerial distance between two geographic points.
17. **UUID Generation**: Generate random UUIDs.

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/dns-utilities-streamlit.git
    ```

2. Navigate to the project directory:
    ```bash
    cd dns-utilities-streamlit
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have `dig` installed on your system:
    - **Linux**: Install via `dnsutils`
      ```bash
      sudo apt-get install dnsutils
      ```
    - **macOS**: Install via Homebrew
      ```bash
      brew install bind
      ```
    - **Windows**: Install via BIND from ISC (Internet Systems Consortium) [here](https://www.isc.org/download/).

5. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

6. Open the app in your browser at `http://localhost:8501`.

## Requirements

- Python 3.7 or higher
- `streamlit` 1.25.0
- `dig` command-line utility installed on your system

## Example Utilities

### World Time
Enter the city name (e.g., `mumbai`) and get the current time.

```bash
dig mumbai.time @dns.toys
