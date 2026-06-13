from ecommerce.shipping import calc_shipping
from pathlib import Path

path = Path()

for file in path.glob("*.py"):
    print(file)

# ecommerce.shipping.calc_shipping()
calc_shipping()