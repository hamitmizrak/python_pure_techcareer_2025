#!/bin/bash

# ANSI Renk Kodları
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # Renk sıfırlama (No Color)

# Geri Sayım Süresi (saniye)
countdown_time=3

# Başlık
echo -e "${CYAN}\n🚀 Geri Sayım Başlıyor...${NC}"

# Geri Sayım Döngüsü
while [ $countdown_time -gt 0 ]; do
    echo -e "${YELLOW}$countdown_time saniye kaldı...${NC}"
    sleep 1
    countdown_time=$((countdown_time - 1))
done

# Bitiş Bildirimi
echo -e "${GREEN}\a✅ İşlem başlıyor...${NC}\n"
