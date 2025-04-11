import streamlit as st
import requests
import json

def langflow_recipe_generator(prompt):
    # The complete API endpoint URL for this flow
    url = f"https://api.langflow.astra.datastax.com/lf/{st.secrets['LANGFLOW_API_EP']}"

    # Request payload configuration
    payload = {
        "input_value": prompt,
        # The input value to be processed by the flow
        "output_type": "chat",  # Specifies the expected output format
        "input_type": "chat"  # Specifies the input format
    }

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['LANGFLOW_APPLICATION_TOKEN']}"  # Authentication key from environment variable
    }

    try:
        # Send API request
        response = requests.request("POST", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
        message = json.loads(response.text)

        # return response
        return message['outputs'][0]['outputs'][0]['results']['message']['data']['text']

    except requests.exceptions.RequestException as e:
        st.exception(f"Error making API request: {e}")
    except ValueError as e:
        st.exception(f"Error parsing response: {e}")

def display_footer():
    footer = """
    <style>
    /* Ensures the footer stays at the bottom of the sidebar */
    [data-testid="stSidebar"] > div: nth-child(3) {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }

    .footer {
        color: grey;
        font-size: 15px;
        text-align: center;
        background-color: transparent;
    }
    </style>
    <div class="footer">
    Made with ❤️ by <a href="mailto:zeeshan.altaf@gmail.com">Zeeshan</a>.
    </div>
    """
    st.sidebar.markdown(footer, unsafe_allow_html=True)