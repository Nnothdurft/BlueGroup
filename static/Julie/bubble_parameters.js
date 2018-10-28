data = JSON.parse(csvData);
var BUBBLE_PARAMETERS = {
    "data_file": data,
    "map_file": "static/Julie/us.json",
    "report_title": "S&P 500 Market Cap",
    "footer_text": "Washington University Data Analytics - 2018 Blue Group.",
    "width": 940,
    "height": 600,
    "force_strength": 0.03,
    "force_type": "charge",
    "radius_field": "MktCap2018",
    "numeric_fields": ["MktCap2018", "Debt", "MktCap2018", "Change vs 2015", "Stake"],
    "fill_color": {
        "data_field": "Sector",
        "color_groups": {
            "Industrials": "rgb(141, 211, 199)",
            "Health Care": "rgb(255, 255, 179)",
            "Information Technology": "rgb(190, 186, 218)",
            "Communication Services": "rgb(251, 128, 114)",
            "Consumer Discretionary": "rgb(128, 177, 211)",
            "Real Estate": "rgb(253, 180, 98)",
            "Utilities": "rgb(179, 222, 105)",
            "Financials": "rgb(252, 205, 229)",
            "Materials": "rgb(217, 217, 217)",
            "Consumer Staples": "rgb(188, 128, 189)",
            "Energy": "rgb(204, 235, 197)"
        }
    },
    "tooltip": [
        {"title": "Company", "data_field": "Company"},
        {"title": "Sector", "data_field": "Sector"},
        {"title": "Market Cap 2018", "data_field": "MktCap2018", "format_string": ",.7r"},
        {"title": "Market Cap 2013", "data_field": "MktCap2013", "format_string": ",.7r"},
        {"title": "Percent Change 2013 vs 2015", "data_field": "Changevs2015"}
    ],
    "modes": [
        {
            "button_text": "2018 Market Cap",
            "button_id": "all",
            "type": "grid",
            "labels": null,
            "grid_dimensions": {"rows": 1, "columns": 1},
            "data_field": null
        },
        {
            "button_text": "Market Cap by Sector",
            "button_id": "region",
            "type": "grid",
            "labels": ["Utilities", "Energy", "Real Estate", "Communication Services", "Consumer Discretionary", "Financials", "Materials", "Information Technology", "Industrials", "Consumer Staples", "Health Care", ""],
            "grid_dimensions": {"rows": 3, "columns": 4},
            "data_field": "Sector"
        },
        {
            "button_text": "Market Cap 2013 vs 2018",
            "button_id": "Change",
            "type": "grid",
            "labels": ["Down", "No Change", "Up"],
            "grid_dimensions": {"rows": 1, "columns": 3},
            "data_field": "Change"
        },
        {
            "button_text": "2013 to 2018 Winners and Losers",
            "button_id": "change_vs_net_value",
            "type": "scatterplot",
            "x_data_field": "Stake",
            "y_data_field": "Stake",
            "x_format_string": ",.2r",
            "y_format_string": ",.2r"
        },
        {
            "button_text": "Assets by Location",
            "button_id": "assets_on_map",
            "type": "map",
            "latitude_field": "Latitude",
            "longitude_field": "Longitude"
        }
    ]
};