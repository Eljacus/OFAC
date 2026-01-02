from utils.ManagementScreen import ManagementScreen

ofac = ManagementScreen()
ofac.openBrowser()

amount= ofac.searchPerson("PEDRO AREVALO")
print("Resultados encontrados:", amount)

