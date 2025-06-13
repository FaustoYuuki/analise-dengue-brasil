import pandas as pd
import io
import re

raw_data = """
TOTAL 1641.329.8382.594.7944.114.9394.304.4283.015.182980.148404.895237.338186.481191.331275.864438.73318.074.135
11 Rondônia 28.89610.28910.8056.4924.0932.3011.6341.0648521.2982.6994.41654.841
12 Acre -18.54813.6759.4065.2294.2551.9711.8283.2938.75511.09613.04013.208104.304
13 Amazonas -9.1599.2019.9958.2545.3723.4552.9502.3132.6443.3394.0765.47066.228
14 Roraima -5044184074275305805386495965035904836.225
15 Pará -12.17616.75517.89313.4408.9124.5163.2973.2992.6822.5883.5704.81293.940
16 Amapá -2.2923.9273.9972.8372.0571.5081.6661.6251.1621.14977146423.455
17 Tocantins 212.11712.58212.84012.86610.9974.8942.3251.6251.1161.4303.6737.93784.404
21 Maranhão 26.24213.33519.77516.8109.3924.2662.5421.9821.3491.2181.4171.84080.170
22 Piauí -3.4707.52716.75025.26221.58912.3426.1943.2471.5091.1041.1181.317101.429
23 Ceará 610.59819.40035.68360.30570.54552.33533.03119.9439.9356.0526.4265.522329.781
24 Rio Grande do Norte 610.46328.43339.86639.48837.89127.35919.60013.2027.0975.3104.7414.556238.012
25 Paraíba 39.26114.99824.49026.64430.38521.24115.97610.4366.8355.0074.4846.709176.469
26 Pernambuco 2626.78134.18745.23652.94950.69632.38622.69416.87814.44114.44423.21323.228357.159
27 Alagoas 36.3568.33811.65915.48325.52024.92721.01513.3128.7127.0717.3175.256154.969
28 Sergipe 11.3302.3602.7103.1193.8494.0384.5803.6703.2222.3062.8241.51535.524
29 Bahia 833.42986.204147.735142.082105.46250.95532.50718.82612.83011.19512.19915.067668.499
31 Minas Gerais 28302.550715.242995.867878.012521.123127.43732.16615.64014.67118.28335.30069.5633.725.882
32 Espírito Santo -21.90421.16624.93822.44524.42119.58712.2017.6125.8886.6167.75513.049187.582
33 Rio de Janeiro 463.158128.685141.872110.05675.61631.31015.7549.7337.5127.72311.29821.823624.544
35 São Paulo 37361.857725.9641.376.4471.535.4101.087.765277.19476.63435.13928.33431.22645.24288.9825.670.231
41 Paraná 999.578218.589408.988446.164287.96762.98617.6207.5516.2067.82014.16627.1261.604.770
42 Santa Catarina 17.88038.441143.409229.478159.17038.0658.5312.4711.2941.3251.5363.406635.007
43 Rio Grande do Sul 15.31124.112100.090172.306101.82516.2943.4331.1618037699361.242428.283
50 Mato Grosso do Sul -40.72355.26769.95060.48139.68013.6536.0983.4702.8993.8279.39015.725321.163
51 Mato Grosso 338.51543.92642.73543.30635.51816.9798.7945.5264.2094.8059.29216.430270.038
52 Goiás 21139.499221.198286.882284.263223.75497.20840.62626.79524.29627.55939.53259.1041.470.737
53 Distrito Federal 177.240120.567114.51290.81866.79830.36110.6616.8766.6326.2689.25920.483560.476
00 Ignorado/exterior -1822--------13
"""

# Define column headers based on the TabNet interface
columns = ["UF_Notificacao", "Ign_Em_Branco", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez", "Total"]

data = []
# Regex to split the state name/code from the numbers, and then split the numbers
# This regex is complex due to the concatenated numbers and potential '-'
# It assumes state name ends before the first digit or '-' that starts the numeric data
pattern = re.compile(r"^(.*?)\s+(-?\d{1,3}(?:\.\d{3})*|-)\s*(\d.*|-\d.*)$", re.UNICODE)
# Regex to find numbers separated by dots (potential thousands separators) or just digits, including potential negatives starting a sequence
num_pattern = re.compile(r"(-?\d{1,3}(?:\.\d{3})*|-)")

for line in io.StringIO(raw_data):
    line = line.strip()
    if not line:
        continue

    match = pattern.match(line)
    if match:
        uf_name = match.group(1).strip()
        ign_branco = match.group(2).strip()
        numbers_str = match.group(3).strip()

        # Clean up state name (remove leading code if present)
        uf_name = re.sub(r"^\d+\s+", "", uf_name)

        # Clean Ign_Em_Branco
        ign_branco = ign_branco.replace('.', '').replace('-', '0')

        # Extract numbers using the num_pattern on the remaining string
        # This needs refinement as simple findall might not respect order/boundaries correctly
        # Let's try a simpler split approach first based on typical number lengths or look for patterns
        # Trying findall first, might need adjustment
        numbers = num_pattern.findall(numbers_str)

        # Handle the special case for 'Ignorado/exterior' with dashes
        if uf_name == 'Ignorado/exterior':
             cleaned_numbers = ['0'] * 12 # 12 months
             # Extract the last number which should be the total
             total_match = re.search(r'(\d+)$', numbers_str)
             if total_match:
                 cleaned_numbers.append(total_match.group(1).replace('.', ''))
             else:
                 cleaned_numbers.append('0')
        else:
            # Clean numbers by removing dots and replacing '-' with '0'
            cleaned_numbers = [num.replace('.', '').replace('-', '0') for num in numbers]

        # Combine the row
        row = [uf_name, ign_branco] + cleaned_numbers

        # Ensure the row has the correct number of columns (15)
        if len(row) < len(columns):
             row.extend(['0'] * (len(columns) - len(row))) # Pad with 0
        elif len(row) > len(columns):
             row = row[:len(columns)] # Truncate if too long

        data.append(row)
    else:
        # Handle the 'Ignorado/exterior' case specifically if the main pattern fails
        if 'Ignorado/exterior' in line:
            parts = line.split('-')
            uf_name = parts[0].strip()
            ign_branco = '0'
            cleaned_numbers = ['0'] * 12 # 12 months
            total = parts[-1].strip().replace('.', '') if parts[-1].strip() else '0'
            cleaned_numbers.append(total)
            row = [uf_name, ign_branco] + cleaned_numbers
            if len(row) == len(columns):
                 data.append(row)
            else:
                 print(f"Skipping line (Ignorado/exterior format error): {line}")
        else:
            print(f"Skipping line (no match): {line}") # Debugging unmatched lines

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Convert numeric columns to appropriate types
for col in columns[1:]: # Skip UF_Notificacao
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Save to CSV
output_path = "/home/ubuntu/dengue_data_raw.csv"
df.to_csv(output_path, index=False)

print(f"Data saved to {output_path}")
print(df.head().to_string())
print(df.info())

