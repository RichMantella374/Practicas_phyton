import pandas as pd

# Initialize the DataFrame based on the image
facturas_df = pd.DataFrame({
    "Cliente": ["C1", "C3", "C2", "C1", "C2", "C1"],
    "Factura": ["f100", "f105", "f103", "f102", "f106", "f101"],
    "Importe": [100, 200, 100, 200, 100, 200],
    "Pagado": [True, True, True, False, True, True]
})

# Filter for unpaid invoices
facturas_no_pagadas = facturas_df[facturas_df['Pagado'] == False]

# Group by 'Cliente' and sum the 'Importe'
total_no_pagado_por_cliente_series = facturas_no_pagadas.groupby('Cliente')['Importe'].sum()

# Convert the Series to a DataFrame and manually set column names
tabla_importe_no_pagado = total_no_pagado_por_cliente_series.reset_index()
tabla_importe_no_pagado.columns = ['Cliente', 'Total']

print("Tabla de importe total de facturas no pagadas por cliente:")
print(tabla_importe_no_pagado)
# Calculate the total number of invoices per client
total_facturas_por_cliente_series = facturas_df.groupby('Cliente')['Factura'].count()

# Calculate the number of paid invoices per client
facturas_pagadas_por_cliente_series = facturas_df.groupby('Cliente')['Pagado'].sum()

# Convert series to DataFrames and set column names
total_facturas_por_cliente_df = total_facturas_por_cliente_series.reset_index()
total_facturas_por_cliente_df.columns = ['Cliente', 'TotalFacturas']

facturas_pagadas_por_cliente_df = facturas_pagadas_por_cliente_series.reset_index()
facturas_pagadas_por_cliente_df.columns = ['Cliente', 'FacturasPagadas']

# Set 'Cliente' as the index for easier lookup
total_facturas_por_cliente_df = total_facturas_por_cliente_df.set_index('Cliente')
facturas_pagadas_por_cliente_df = facturas_pagadas_por_cliente_df.set_index('Cliente')

# Add temporary columns to the original DataFrame for comparison
facturas_df['total_del_cliente'] = total_facturas_por_cliente_df.loc[facturas_df['Cliente'], 'TotalFacturas'].reset_index().iloc[:, 1]
facturas_df['pagadas_del_cliente'] = facturas_pagadas_por_cliente_df.loc[facturas_df['Cliente'], 'FacturasPagadas'].reset_index().iloc[:, 1]

# Create a boolean column indicating if the client has all invoices paid
facturas_df['cliente_todo_pagado'] = (facturas_df['total_del_cliente'] == facturas_df['pagadas_del_cliente'])

# Filter the DataFrame to keep only clients who are NOT 'todo_pagado'
facturas_final = facturas_df[facturas_df['cliente_todo_pagado'] == False]

# Select only the original columns to effectively "drop" the temporary ones
facturas_final = facturas_final[['Cliente', 'Factura', 'Importe', 'Pagado']]

print("\nTabla original después de eliminar clientes con todas sus facturas pagadas:")
print(facturas_final)