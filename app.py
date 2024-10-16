import streamlit as st
import requests

# Function to query the dns.toys API
def query_dns(query):
    url = f"https://dns.toys/{query}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit app layout
st.title("DNS Utilities App")

# Select utility type
utility_type = st.selectbox("Select a Utility:", [
    "World Time",
    "Weather",
    "Timezone Conversion",
    "Unit Conversion",
    "Currency Conversion",
    "IP Echo",
    "Number to Words",
    "Usable CIDR Range",
    "Random Number Generation",
    "Generate UUIDs",
    "Help"
])

# Utility Selection Logic
if utility_type == "World Time":
    city = st.text_input("Enter city name (e.g., mumbai) for world time:")
    if st.button("Get World Time"):
        if city:
            result = query_dns(f"{city}.time")
            st.write(result)

elif utility_type == "Weather":
    city_weather = st.text_input("Enter city name (e.g., newyork) for weather:")
    if st.button("Get Weather"):
        if city_weather:
            result = query_dns(f"{city_weather}.weather")
            st.write(result)

elif utility_type == "Timezone Conversion":
    date_time = st.text_input("Enter in format YYYY-MM-DDTHH:MM-fromCity-toCity:")
    if st.button("Convert Timezone"):
        if date_time:
            result = query_dns(f"{date_time}.time")
            st.write(result)

elif utility_type == "Unit Conversion":
    value_unit = st.text_input("Enter in format ValueFromUnit-ToUnit (e.g., 42km-mi):")
    if st.button("Convert Unit"):
        if value_unit:
            result = query_dns(f"{value_unit}.unit")
            st.write(result)

elif utility_type == "Currency Conversion":
    currency_input = st.text_input("Enter in format ValueFromCurrency-ToCurrency (e.g., 100USD-INR):")
    if st.button("Convert Currency"):
        if currency_input:
            result = query_dns(f"{currency_input}.fx")
            st.write(result)

elif utility_type == "IP Echo":
    if st.button("Get IPv4 Address"):
        result = query_dns("ip")
        st.write(f"IPv4 Address: {result}")

    if st.button("Get IPv6 Address"):
        result = query_dns("-6 ip")
        st.write(f"IPv6 Address: {result}")

elif utility_type == "Number to Words":
    number_input = st.text_input("Enter a number to convert to words:")
    if st.button("Convert Number to Words"):
        if number_input:
            result = query_dns(f"{number_input}.words")
            st.write(result)

elif utility_type == "Usable CIDR Range":
    cidr_input = st.text_input("Enter a CIDR notation (e.g., 10.0.0.0/24):")
    if st.button("Get Usable CIDR Range"):
        if cidr_input:
            result = query_dns(f"{cidr_input}.cidr")
            st.write(result)

elif utility_type == "Random Number Generation":
    random_input = st.text_input("Enter range for random number (e.g., 1-100):")
    if st.button("Generate Random Number"):
        if random_input:
            result = query_dns(f"{random_input}.rand")
            st.write(result)

elif utility_type == "Generate UUIDs":
    uuid_count = st.text_input("Enter number of UUIDs to generate (e.g., 5):")
    if st.button("Generate UUIDs"):
        if uuid_count:
            result = query_dns(f"{uuid_count}.uuid")
            st.write(result)

elif utility_type == "Help":
    if st.button("List Available Services"):
        result = query_dns("help")
        st.write(result)

# Footer
st.markdown("""
### Note:
- For city names and other inputs, please ensure to follow the expected format.
- This app queries the dns.toys API for various utilities.
""")
