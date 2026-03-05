from cra5.api.era5_downloader import era5_downloader
ERA5_data = era5_downloader('./cra5/api/era5_config.py') #specify the dataset config for what we want to download
data = ERA5_data.get_form_timestamp(time_stamp="2024-06-01T00:00:00", local_root='./data/ERA5')
