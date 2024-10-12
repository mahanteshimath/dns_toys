import streamlit as st
import requests
import uuid
import random
from datetime import datetime
import time

# Functions for different utilities

def get_world_time(city):
    # Dummy implementation; You can integrate with a world time API
    return f"The current time in {city.capitalize()} is {datetime.now()}."

def get_weather(city):
    # You can use a weather API like OpenWeather or yr.no
    return f"Weather for {city.capitalize()}: Sunny, 25°C"

def convert_timezone(date_time, from_city, to_city):
    # Dummy implementation; integrate with a time zone conversion API
    return f"{date_time} in {from_city.capitalize()} is equivalent to {datetime.now()} in {to_city.capitalize()}."

def unit_conversion(value, from_unit, to_unit):
    # Dummy conversion logic; use a proper unit conversion library
    conversions = {
        'km': 1000,
        'mi': 1609.34,
        'gb': 1024,
        'mb': 1
    }
    return f"{value} {from_unit.upper()} equals {value * conversions[from_unit.lower()]} {to_unit.upper()}"

def currency_conversion(value, from_currency, to_currency):
    # Use an API like exchangerate.host for real-time conversion
    return f"{value} {from_currency.upper()} equals {value * 80} {to_currency.upper()}"

def get_ip(ip_version):
    # Return dummy IPs or use external IP API
    return f"Your IPv{ip_version} address is 192.0.2.1" if ip_version == 4 else "2001:0db8::1"

def number_to_words(number):
    # Use num2words package or similar
    from num2words import num2words
    return num2words(number)

def cidr_range(cidr):
    # Dummy implementation; can use an IP library
    return f"Usable range for {cidr}: 10.0.0.1 - 10.0.0.254"

def number_base_conversion(number, from_base, to_base):
    # Conversion between number bases
    base_map = {'dec': 10, 'hex': 16, 'oct': 8, 'bin': 2}
    return f"{number} in {from_base.upper()} equals {int(str(number), base_map[from_base])} in {to_base.upper()}"

def random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def generate_uuid(count):
    return [str(uuid.uuid4()) for _ in range(count)]

def toss_coin(count):
    return [random.choice(['Heads', 'Tails']) for _ in range(count)]

# Streamlit UI

st.title('DNS Toys Utilities in Streamlit')

option = st.sidebar.selectbox(
    "Choose a service",
    ("World Time", "Weather", "Timezone Conversion", "Unit Conversion", 
     "Currency Conversion", "IP Echo", "Number to Words", "Usable CIDR Range", 
     "Number Base Conversion", "Random Number", "UUID Generation", "Coin Toss")
)

if option == "World Time":
    city = st.text_input("Enter city name", "mumbai")
    if st.button("Get Time"):
        st.write(get_world_time(city))

elif option == "Weather":
    city = st.text_input("Enter city name", "mumbai")
    if st.button("Get Weather"):
        st.write(get_weather(city))

elif option == "Timezone Conversion":
    date_time = st.text_input("Enter date-time (YYYY-MM-DDTHH:MM)", "2023-05-28T14:00")
    from_city = st.text_input("From city", "mumbai")
    to_city = st.text_input("To city", "paris/fr")
    if st.button("Convert"):
        st.write(convert_timezone(date_time, from_city, to_city))

elif option == "Unit Conversion":
    value = st.number_input("Enter value", 42)
    from_unit = st.text_input("From unit (e.g., km)", "km")
    to_unit = st.text_input("To unit (e.g., mi)", "mi")
    if st.button("Convert"):
        st.write(unit_conversion(value, from_unit, to_unit))

elif option == "Currency Conversion":
    value = st.number_input("Enter value", 100)
    from_currency = st.text_input("From currency (e.g., USD)", "USD")
    to_currency = st.text_input("To currency (e.g., INR)", "INR")
    if st.button("Convert"):
        st.write(currency_conversion(value, from_currency, to_currency))

elif option == "IP Echo":
    ip_version = st.selectbox("Choose IP version", [4, 6])
    if st.button("Get IP"):
        st.write(get_ip(ip_version))

elif option == "Number to Words":
    number = st.number_input("Enter number", 987654321)
    if st.button("Convert"):
        st.write(number_to_words(number))

elif option == "Usable CIDR Range":
    cidr = st.text_input("Enter CIDR notation", "10.0.0.0/24")
    if st.button("Get Usable Range"):
        st.write(cidr_range(cidr))

elif option == "Number Base Conversion":
    number = st.number_input("Enter number", 100)
    from_base = st.text_input("From base (e.g., dec)", "dec")
    to_base = st.text_input("To base (e.g., hex)", "hex")
    if st.button("Convert"):
        st.write(number_base_conversion(number, from_base, to_base))

elif option == "Random Number":
    min_num = st.number_input("Min number", 1)
    max_num = st.number_input("Max number", 100)
    if st.button("Generate"):
        st.write(random_number(min_num, max_num))

elif option == "UUID Generation":
    count = st.number_input("How many UUIDs?", 5)
    if st.button("Generate UUIDs"):
        st.write(generate_uuid(count))

elif option == "Coin Toss":
    count = st.number_input("How many coins?", 1)
    if st.button("Toss"):
        st.write(toss_coin(count))
