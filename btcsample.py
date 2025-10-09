import pandas as pd

# Load your BTC dataset (already done earlier)
btc = pd.read_csv("btcsales.csv")

# Create a smaller sample — adjust 'n' as you wish
btc_sample = btc.sample(n=10000, random_state=50)

# Save it as a new file
btc_sample.to_csv("btc_sample.csv", index=False)
