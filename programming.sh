#! /bin/bash

echo "Python requirements.txt 3.lib"

INSTALL="Yükle"

#####################################################
chmod +x shell_countdown.sh

#####################################################
version_info(){
  ./shell_countdown.sh
  python --version
  pip --version
}
version_info

#disable=SC2162
#########################################################
# Database File Delete
requirements_txt() {

    # Geri Sayım (dosya varsa çalışır)
    ./shell_countdown.sh

    echo -e "\n###### ${INSTALL:-REQUIREMENTS} ######"
    read -rp "requirements eklenecektir? e/h: " requirements

    if [[ $requirements == "e" || $requirements == "E" ]]; then
        echo -e "Bulunduğum dizin => $(pwd)\n"
        echo -e "requirements.txt oluşturulmaya başladı ..."
        ./shell_countdown.sh

        rm -f requirements.txt
        sleep 1

        # DİKKAT: 'EOF' satırı en başta, boşluksuz olmalı
        cat > requirements.txt <<'EOF'
# veri türü zorunluluğu
beartype>=0.19.0
# başka paketler
EOF

        echo "✓ requirements.txt yazıldı."
    else
        echo -e "requirements.txt oluşturulmadı!"
    fi
}

requirements_txt
