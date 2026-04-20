
Untitled3.ipynb_
jayvee shah

prn- 25070123058

a3 entc

covid data analysis

 
[ ]
Start coding or generate with AI.

 
[ ]
import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as snsdata=pd.read_csv("/content/covid_19_data.csv", on_bad_lines='skip', low_memory=False)data.head()

 
 
[ ]
data=data.drop(['SNo','Last Update'],axis=1)
data.head()
 
 
[ ]
data.info()
 <class 'pandas.core.frame.DataFrame'>
RangeIndex: 306429 entries, 0 to 306428
Data columns (total 6 columns):
 #   Column           Non-Null Count   Dtype  
---  ------           --------------   -----  
 0   ObservationDate  306429 non-null  object 
 1   Province/State   228326 non-null  object 
 2   Country/Region   306429 non-null  object 
 3   Confirmed        306429 non-null  float64
 4   Deaths           306429 non-null  float64
 5   Recovered        306429 non-null  float64
dtypes: float64(3), object(3)
memory usage: 14.0+ MB
 
[ ]
data['ObservationDate'] = pd.to_datetime(data['ObservationDate'], errors='coerce')
data['Confirmed'] = data['Confirmed'].fillna(0).astype('int64')
data['Deaths'] = data['Deaths'].fillna(0).astype('int64')
data['Recovered'] = data['Recovered'].fillna(0).astype('int64')
data.info()
 <class 'pandas.core.frame.DataFrame'>
RangeIndex: 306429 entries, 0 to 306428
Data columns (total 6 columns):
 #   Column           Non-Null Count   Dtype         
---  ------           --------------   -----         
 0   ObservationDate  306429 non-null  datetime64[ns]
 1   Province/State   228326 non-null  object        
 2   Country/Region   306429 non-null  object        
 3   Confirmed        306429 non-null  int64         
 4   Deaths           306429 non-null  int64         
 5   Recovered        306429 non-null  int64         
dtypes: datetime64[ns](1), int64(3), object(2)
memory usage: 14.0+ MB
 
[ ]
data.head()
 
 
[ ]
##active cases
data['Active']=data['Confirmed']-data['Recovered']-data['Deaths']
data.head(50)
data.iloc[50:100]
 
 
[ ]
##last/current date
data['ObservationDate'].max()

 Timestamp('2021-05-29 00:00:00')
 
[ ]
##fetch the last data date
latest_data=data[data['ObservationDate']==data['ObservationDate'].max()]
latest_data.head()
 
 
[ ]
latest_data.shape
 (765, 7)
 
[ ]
latest_data['Country/Region'].value_counts()
 
 
[ ]
latest_data['Country/Region'].nunique()
 195
 
[ ]
latest_data['Country/Region'].unique()
 array(['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
       'Antigua and Barbuda', 'Argentina', 'Armenia', 'Austria',
       'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
       'Belarus', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
       'Bosnia and Herzegovina', 'Botswana', 'Brunei', 'Bulgaria',
       'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia',
       'Cameroon', 'Central African Republic', 'Chad', 'Comoros',
       'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia',
       'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Diamond Princess',
       'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon',
       'Gambia', 'Georgia', 'Ghana', 'Greece', 'Grenada', 'Guatemala',
       'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See',
       'Honduras', 'Hungary', 'Iceland', 'Indonesia', 'Iran', 'Iraq',
       'Ireland', 'Israel', 'Ivory Coast', 'Jamaica', 'Jordan',
       'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait',
       'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
       'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'MS Zaandam',
       'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
       'Marshall Islands', 'Mauritania', 'Mauritius', 'Micronesia',
       'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
       'Mozambique', 'Namibia', 'Nepal', 'New Zealand', 'Nicaragua',
       'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Panama',
       'Papua New Guinea', 'Paraguay', 'Philippines', 'Poland',
       'Portugal', 'Qatar', 'Romania', 'Rwanda', 'Saint Kitts and Nevis',
       'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
       'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
       'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',
       'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
       'South Korea', 'South Sudan', 'Sri Lanka', 'Sudan', 'Suriname',
       'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
       'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago',
       'Tunisia', 'Turkey', 'Uganda', 'United Arab Emirates', 'Uruguay',
       'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
       'West Bank and Gaza', 'Yemen', 'Zambia', 'Zimbabwe', 'Italy',
       'Brazil', 'Russia', 'Mexico', 'Japan', 'US', 'Canada', 'Colombia',
       'Peru', 'Spain', 'India', 'UK', 'Mainland China', 'Chile',
       'Belgium', 'Netherlands', 'Australia', 'Pakistan', 'Germany',
       'Sweden', 'Ukraine', 'Hong Kong', 'Macau'], dtype=object)
 
[ ]
## count of cases for each county
countries=latest_data.groupby("Country/Region")[["Confirmed","Deaths","Recovered","Active"]].sum()
countries=countries.reset_index()
countries
 
 
[ ]
countries[countries['Country/Region']=="India"]
 
 
[ ]
countries[countries['Country/Region']=="Mainland China"]
 
 
[ ]
countries[countries['Country/Region']=="US"]
 
 
[ ]
##plot world map


 
[ ]
import plotly.express as px
 
[ ]
world_map=px.choropleth(countries,locations="Country/Region",locationmode="country names", color="Confirmed", color_continuous_scale="reds",range_color=[0,10000000])
world_map.show()
 
 
[ ]
top=latest_data.groupby("Country/Region")[["Confirmed","Recovered"]].sum().reset_index()
top=top.sort_values(by=["Confirmed"],ascending=False)
top.head()
 
 
[ ]
india=data[data["Country/Region"]=="India"]
india
 
 
[ ]
# find total number of states
india['Province/State'].nunique()
 38
 
[ ]
india['Province/State'].unique()
 array([nan, 'Andaman and Nicobar Islands', 'Andhra Pradesh',
       'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
       'Chhattisgarh', 'Dadar Nagar Haveli', 'Delhi', 'Goa', 'Gujarat',
       'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
       'Karnataka', 'Kerala', 'Ladakh', 'Madhya Pradesh', 'Maharashtra',
       'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
       'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
       'Telangana', 'Tripura', 'Unknown', 'Uttar Pradesh', 'Uttarakhand',
       'West Bengal', 'Dadra and Nagar Haveli and Daman and Diu',
       'Lakshadweep'], dtype=object)
 
[ ]
india['Province/State']=india["Province/State"].fillna("mode")
 /tmp/ipykernel_2716/3182080433.py:1: SettingWithCopyWarning:


A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

 
[ ]
india['Province/State'].mode()
 
 
[ ]
india_latest_data=india[india["ObservationDate"]==india['ObservationDate'].max()]
india_latest_data
 
 
[ ]
top_state = india_latest_data.groupby("Province/State")[['Confirmed','Recovered']].sum().reset_index()
top_state = top_state.sort_values(['Confirmed'],ascending=False)
top_state.head(20)
 
 
[ ]
top_state['Confirmed'].max()

 5713215
 
[ ]
top_state[top_state['Confirmed'] == top_state['Confirmed'].max()]
 
 
[ ]
##plot india map

 
[ ]
import plotly.express as px
 
[ ]

india_map=px.choropleth(
    top_state,
    locations="Province/State",
    locationmode="country names",
    color="Confirmed",
    color_continuous_scale="reds",
    range_color=[0, top_state['Confirmed'].max()],
    scope="asia"
)
india_map.show()
 
Downloading GeoJSON for Indian States

Since you don't have a GeoJSON file, I will download a common one from a public source directly into your Colab environment. This file contains the geographical boundaries for the states of India, which is necessary for plotly.express to draw an accurate choropleth map.

I will then re-run the code to load this GeoJSON file and plot the map with your top_state data.

 
[ ]
import requests

geojason_url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson"
geojson_filename = "india_states.geojson"

try:
    response = requests.get(geojason_url)
    response.raise_for_status() # Raise an exception for HTTP errors
    with open(geojson_filename, 'wb') as f:
        f.write(response.content)
    print(f"Successfully downloaded {geojson_filename}")
except requests.exceptions.RequestException as e:
    print(f"Error downloading GeoJSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Now, let's load the downloaded GeoJSON file
 Successfully downloaded india_states.geojson
 
[ ]
import json

# Assuming you have uploaded 'india_states.geojson' to your Colab environment
# Make sure the file name matches exactly.
geojson_path = 'india_states.geojson'

try:
    with open(geojson_path) as f:
        india_states_geojson = json.load(f)
    print(f"Successfully loaded {geojson_path}")

    # Inspect the GeoJSON features to find the correct `featureidkey`
    # For example, to see properties of the first feature:
    # if india_states_geojson and 'features' in india_states_geojson and len(india_states_geojson['features']) > 0:
    #     print("First GeoJSON feature properties:")
    #     print(india_states_geojson['features'][0]['properties'])

except FileNotFoundError:
    print(f"Error: {geojson_path} not found. Please upload the GeoJSON file to Colab.")
    india_states_geojson = None
except Exception as e:
    print(f"Error loading GeoJSON: {e}")
    india_states_geojson = None

 Successfully loaded india_states.geojson
 
[ ]
if india_states_geojson:
    # It's crucial to find the correct `featureidkey` from your GeoJSON file.
    # Common keys are 'ST_NM', 'NAME_1', 'state', etc.
    # For the downloaded GeoJSON, 'NAME_1' is a common property for state names.

    # Example: if your GeoJSON feature properties look like {'NAME_1': 'Maharashtra', ...},
    # then 'properties.NAME_1' is correct.

    # Ensure the 'Province/State' column in `top_state` matches the names in the GeoJSON property.

    india_map_geojson = px.choropleth(
        top_state,
        geojson=india_states_geojson,
        featureidkey="properties.NAME_1", # **Adjust this to your GeoJSON's state name property if different**
        locations="Province/State", # Column in your DataFrame with state names
        color="Confirmed",
        color_continuous_scale="reds",
        range_color=[0, top_state['Confirmed'].max()],
        hover_name="Province/State", # Display state name on hover
        title="Confirmed Cases in Indian States",
        projection="mercator" # A common projection for world/country maps
    )

    india_map_geojson.update_geos(
        fitbounds="locations", # Zoom to the bounds of the provided locations
        visible=False # Hide the base map for cleaner look
    )

    india_map_geojson.show()
else:
    print("Cannot plot map: GeoJSON data not loaded.")
 
 
[ ]
print("Sample of Province/State names from your top_state DataFrame:")
print(top_state['Province/State'].head().tolist())

# Extract some NAME_1 values from the GeoJSON for comparison
geojson_state_names = []
if india_states_geojson and 'features' in india_states_geojson:
    for feature in india_states_geojson['features']:
        if 'properties' in feature and 'NAME_1' in feature['properties']:
            geojson_state_names.append(feature['properties']['NAME_1'])
    print("\nSample of state names from GeoJSON (NAME_1 property):")
    print(geojson_state_names[:5]) # Print first 5 for brevity
 
[ ]
import json

# Assuming you have uploaded 'india_states.geojson' to your Colab environment
# Make sure the file name matches exactly.
geojson_path = 'india_states.geojson'

try:
    with open(geojson_path) as f:
        india_states_geojson = json.load(f)
    print(f"Successfully loaded {geojson_path}")

    # Inspect the GeoJSON features to find the correct `featureidkey`
    # For example, to see properties of the first feature:
    # if india_states_geojson and 'features' in india_states_geojson and len(india_states_geojson['features']) > 0:
    #     print("First GeoJSON feature properties:")
    #     print(india_states_geojson['features'][0]['properties'])

except FileNotFoundError:
    print(f"Error: {geojson_path} not found. Please upload the GeoJSON file to Colab.")
    india_states_geojson = None
except Exception as e:
    print(f"Error loading GeoJSON: {e}")
    india_states_geojson = None

 Successfully loaded india_states.geojson
Colab paid products - Cancel contracts here
