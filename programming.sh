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

disable=SC2162
#########################################################
# Database File Delete
requirements_txt() {

    # Geri Sayım
    ./shell_countdown.sh

    echo -e "\n###### ${INSTALL} ######  "
#    disable=SC2162
    read -p "requirements ekleyenecektir ? e/h " requirements
    if [[ $requirements == "e" || $requirements == "E" ]]; then
        echo -e "Bulunduğum dizin => $(pwd)\n"
        echo -e "requirents_txt oluşturulmaya Başladı ..."
         # Geri Sayım
        ./shell_countdown.sh
        rm -rf requirents.txt
        sleep 1
        cat > requirements.txt << 'EOF'
        # veri türü zorunluluğu
        beartype>=0.19.0
        #başka paketler
        EOF
    else
        echo -e "requirents_txt oluşturulmadı !!!"
    fi
}
requirements_txt