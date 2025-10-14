from datetime import date, datetime

#################################################################################
#### Date #######################################################################

# Bugünün tarihi
bugun:date =date.today();
print(f"bugün: => {bugun}")
print(f"bugün yılı: => {bugun.year}")
print(f"bugün ayı: => {bugun.month}")
print(f"bugün günü: => {bugun.day}")
print(f"bugün haftası: => {bugun.weekday()}")  # 0=Monday

print()
########################################################

# Sabit tarih
tarih:date =date(2025,10,14)
print(f"Tarih: => {tarih}")

print()
########################################################

# Bugünün tarihi
simdiki_Zaman =datetime.now();
print(f"Şimdiki uzun tarih: {simdiki_Zaman}")

print()
########################################################

# # Formatter
date_format = date(2025, 10, 14)
print(date_format)

# Türkiye
tr = date_format.strftime("%A.%B.%Y / %d-%m-%Y")
print(tr)