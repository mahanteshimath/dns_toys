import streamlit as st
import subprocess

# Function to run a dig command and return the output
def run_dig(query):
    try:
        result = subprocess.run(['dig', query, '@dns.toys', '+short'], stdout=subprocess.PIPE, text=True)
        return result.stdout if result.stdout else "No data available for this query."
    except Exception as e:
        return f"Error: {str(e)}"

# App Title
st.title("Useful Utilities over DNS - Powered by dns.toys")

# Sidebar with utility selection
utility = st.sidebar.selectbox("Select Utility", [
    "World Time", "Timezone Conversion", "Weather", 
    "Unit Conversion", "Currency Conversion", 
    "IP Echo", "Number to Words", "CIDR Range", 
    "Number Base Conversion", "Pi", "Dictionary", 
    "Rolling Dice", "Coin Toss", "Random Number", 
    "Epoch Timestamp", "Aerial Distance", "UUID Generation"
])

# World Time Utility
if utility == "World Time":
    city = st.text_input("Enter City (e.g., mumbai, newyork):")
    if st.button("Get Time"):
        if city:
            output = run_dig(f"{city}.time")
            st.code(output)
        else:
            st.warning("Please enter a city name.")

# Timezone Conversion
elif utility == "Timezone Conversion":
    date_time = st.text_input("Enter Date and Time (YYYY-MM-DDTHH:MM):")
    from_city = st.text_input("From City (e.g., mumbai):")
    to_city = st.text_input("To City (e.g., paris/fr):")
    if st.button("Convert Time"):
        if date_time and from_city and to_city:
            output = run_dig(f"{date_time}-{from_city}-{to_city}.time")
            st.code(output)
        else:
            st.warning("Please enter all required fields.")

# Weather Utility
elif utility == "Weather":
    city = st.text_input("Enter City (e.g., mumbai, amsterdam/nl):")
    if st.button("Get Weather"):
        if city:
            output = run_dig(f"{city}.weather")
            st.code(output)
        else:
            st.warning("Please enter a city name.")

# Unit Conversion
elif utility == "Unit Conversion":
    value = st.number_input("Enter Value:", min_value=0.0)
    from_unit = st.text_input("From Unit (e.g., km, GB):")
    to_unit = st.text_input("To Unit (e.g., mi, MB):")
    if st.button("Convert Unit"):
        if value and from_unit and to_unit:
            output = run_dig(f"{int(value)}{from_unit}-{to_unit}.unit")
            st.code(output)
        else:
            st.warning("Please enter value and units.")

# Currency Conversion
elif utility == "Currency Conversion":
    value = st.number_input("Enter Amount:", min_value=0.0)
    from_currency = st.text_input("From Currency (e.g., USD, CAD):")
    to_currency = st.text_input("To Currency (e.g., INR, AUD):")
    if st.button("Convert Currency"):
        if value and from_currency and to_currency:
            output = run_dig(f"{int(value)}{from_currency}-{to_currency}.fx")
            st.code(output)
        else:
            st.warning("Please enter amount and currencies.")

# IP Echo
elif utility == "IP Echo":
    ip_version = st.selectbox("Select IP Version", ['IPv4', 'IPv6'])
    if st.button("Get IP Address"):
        ip_flag = "-4" if ip_version == "IPv4" else "-6"
        output = run_dig(f"{ip_flag} ip")
        st.code(output)

# Number to Words
elif utility == "Number to Words":
    number = st.text_input("Enter Number (e.g., 987654321):")
    if st.button("Convert to Words"):
        if number.isdigit():
            output = run_dig(f"{number}.words")
            st.code(output)
        else:
            st.warning("Please enter a valid number.")

# CIDR Range
elif utility == "CIDR Range":
    cidr = st.text_input("Enter CIDR (e.g., 10.0.0.0/24):")
    if st.button("Get Usable Range"):
        if cidr:
            output = run_dig(f"{cidr}.cidr")
            st.code(output)
        else:
            st.warning("Please enter a CIDR notation.")

# Number Base Conversion
elif utility == "Number Base Conversion":
    number = st.text_input("Enter Number and Base (e.g., 100dec-hex):")
    if st.button("Convert Base"):
        if number:
            output = run_dig(f"{number}.base")
            st.code(output)
        else:
            st.warning("Please enter number and base conversion format.")

# Pi
elif utility == "Pi":
    if st.button("Get Digits of Pi"):
        output = run_dig("pi")
        st.code(output)

# Dictionary
elif utility == "Dictionary":
    word = st.text_input("Enter Word (e.g., fun, big-time):")
    if st.button("Get Definition"):
        if word:
            output = run_dig(f"{word}.dict")
            st.code(output)
        else:
            st.warning("Please enter a word.")

# Rolling Dice
elif utility == "Rolling Dice":
    dice_roll = st.text_input("Enter Dice Roll (e.g., 1d6, 3d20/2):")
    if st.button("Roll Dice"):
        if dice_roll:
            output = run_dig(f"{dice_roll}.dice")
            st.code(output)
        else:
            st.warning("Please enter a valid dice roll format.")

# Coin Toss
elif utility == "Coin Toss":
    number_of_coins = st.text_input("Enter Number of Coins (e.g., 2):")
    if st.button("Toss Coin"):
        if number_of_coins.isdigit():
            output = run_dig(f"{number_of_coins}.coin")
            st.code(output)
        else:
            st.warning("Please enter a valid number of coins.")

# Random Number Generation
elif utility == "Random Number":
    range_input = st.text_input("Enter Range (e.g., 1-100):")
    if st.button("Generate Random Number"):
        if range_input:
            output = run_dig(f"{range_input}.rand")
            st.code(output)
        else:
            st.warning("Please enter a valid range.")

# Epoch/Unix Timestamp Conversion
elif utility == "Epoch Timestamp":
    timestamp = st.text_input("Enter Epoch Timestamp (e.g., 784783800):")
    if st.button("Convert to Date"):
        if timestamp.isdigit():
            output = run_dig(f"{timestamp}.epoch")
            st.code(output)
        else:
            st.warning("Please enter a valid timestamp.")

# Aerial Distance
elif utility == "Aerial Distance":
    coords = st.text_input("Enter Coordinates (e.g., A12.9352,77.6245/12.9698,77.7500):")
    if st.button("Calculate Distance"):
        if coords:
            output = run_dig(f"{coords}.aerial")
            st.code(output)
        else:
            st.warning("Please enter valid coordinates.")

# UUID Generation
elif utility == "UUID Generation":
    num_of_uuids = st.text_input("Enter Number of UUIDs (e.g., 5):")
    if st.button("Generate UUIDs"):
        if num_of_uuids.isdigit():
            output = run_dig(f"{num_of_uuids}.uuid")
            st.code(output)
        else:
            st.warning("Please enter a valid number.")
