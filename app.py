import streamlit as st
import pandas as pd
import requests


def predict ():
    # ⚠️ in order to push a submission to kaggle you need to use the WHOLE dataset
    nrows = 100
    #generate_submission_csv(nrows, kaggle_upload=False)
    data = [{"key":1,
        "pickup_datetime": str(d.year) + "-" + str(d.month) + "-" + str(d.day) + " " + str(t.hour) + ":" + str(t.min),
        "pickup_longitude": numberplong,
        "pickup_latitude": numberplat,
        "dropoff_longitude": numberdlong,
        "dropoff_latitude": numberdlat,
        "passenger_count": numberpc
        }]
    df = pd.DataFrame.from_dict(data)

    fecha = str(d.year) + "-" + str(d.month) + "-" + str(d.day) + " " + str(t.hour) + ":" + str(t.minute) + ":" + str(t.second)

    #return fecha

    url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={fecha}&pickup_longitude={numberplong}&pickup_latitude={numberplat}&dropoff_longitude={numberdlong}&dropoff_latitude={numberdlat}&passenger_count={int(numberpc)}'
    response = requests.get(url).json()

    return response["fare"]
    #generate_submission_df(df)

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
'''
import datetime

d = st.date_input(
    "- date",
    datetime.date(2019, 7, 6))

import datetime

t = st.time_input(' and time', datetime.time(8, 45))

numberplong = st.number_input('pickup longitude')

numberplat = st.number_input('pickup latitude')

numberdlong = st.number_input('dropoff longitude')

numberdlat = st.number_input('dropoff latitude')

numberpc = st.number_input('passenger count')

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    st.write('Further clicks are not visible but are executed')

    print (predict())

    st.write('I was clicked 🎉')
    st.write(predict())
else:
    st.write('I was not clicked 😞')
