import numpy as np

# After getting the ERA5 data ready, you can explore the compression.
from cra5.api import cra5_api
cra5_API = cra5_api(local_root="../data")

####=======================decompression functions=====================
# If you have saveed  or downloaded the binary file, then you can directly restore the binary file into reconstruction.
output = cra5_API.decode_from_bin("2024-06-01T00:00:00", return_format='de_normalized') # Return the de-normalized cra5 data
x_hat = output['x_hat'].cpu().numpy()

u_hat = x_hat[[cra5_API.vname_to_channels[f"u_{int(p)}"] for p in cra5_API.cfg.pressure_level]]
v_hat = x_hat[[cra5_API.vname_to_channels[f"v_{int(p)}"] for p in cra5_API.cfg.pressure_level]]

np.save("../data/cra5/2024/2024-06-01T00:00:00_u.npy", u_hat)
np.save("../data/cra5/2024/2024-06-01T00:00:00_v.npy", v_hat)

# cra5_API.show_image(
#     reconstruct_data=x_hat,
#     time_stamp="2024-06-01T00:00:00",
#     show_variables=['u_500', 'v_500'],
#     save_path = '../data/CRA5_vis',
# )
