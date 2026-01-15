PRICE_MID_PER_KILO = 7.50

price_sku_per_kilo = float(input())
price_tsa_per_kilo = float(input())
kg_pala = float(input())
kg_saf = float(input())
kg_mid = int(input())

price_pala_per_kilo = price_sku_per_kilo + price_sku_per_kilo * 0.60
pala = price_pala_per_kilo * kg_pala

price_saf = price_tsa_per_kilo + price_tsa_per_kilo * 0.80
saf = price_saf * kg_saf
mid = PRICE_MID_PER_KILO * kg_mid

total = pala + saf + mid
print(f"{total:.2f}")