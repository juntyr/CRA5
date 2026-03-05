# After getting the ERA5 data ready, you can explore the compression.
from cra5.api import cra5_api
cra5_API = cra5_api(local_root="../data")

####=======================compression functions=====================
# Or if you want to directly compress and save the binary stream to a folder
cra5_API.encode_era5_as_bin(time_stamp="2024-06-01T00:00:00", save_root='../data/cra5')
