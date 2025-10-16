#!/bin/bash

# Renk Kodları
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
#############################################################################

# Script Ayarları
set -e  # Hata durumunda scripti durdur

# Yetkilendirme
chmod +x shelling_countdown.sh

#############################################################################
echo -e "${BLUE}Kurulum Yapılıyor...${NC}"
# 1.YOL
# Install
pip install matplotlib
./shelling_countdown.sh

#############################################################################
# Update
#pip install --upgrade matplotlib
#./shelling_countdown.sh

#############################################################################
# list
pip list
./shelling_countdown.sh

#############################################################################
# show
pip show matplotlib

#############################################################################
# Mevcut paketlerimizi requirement içine eklensin
pip freeze > requirements_revize.txt
#pip freeze > requirements_revize.txt

##############################################################################
# PEP8

# Pylint
# Pylint: Kod stil uyumluluğunu, olası hataları eklemek, smell coding(Kötü kod)
pip install pylint


# Flake8:Python kodu için en popüler olan linting,
# stil problemlerini sağlamak
pip install flake8

# Black
# Black: PEP 8 standartlarına uygun, sade ve okunabilir Python kodunu hazırlar
# Kodlarımızı daha okunabilir olmasını ve düzenli olmasını sağlar.
# python -m pip install --upgrade pip
# pip install black
# pip install -r requirements.txt
pip install black

##############################################################################
# 2.YOL
# pip install -r requirements.txt