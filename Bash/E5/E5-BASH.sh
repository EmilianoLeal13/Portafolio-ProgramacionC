#!/bin/bash
haveibeenpwned(){

  curl https://haveibeenpwned.com/api/v3/breachedaccount/$mail -H "hibp-api-key:$api"
}

  echo "ingresa la API: "
  read -s api

while IFS= read -r mail
  do
    if [[ "$mail" == *"@"* ]]; then
      echo "Brechas encontradas en la cuenta:"
      echo "$mail"
      haveibeenpwned
  fi
done < gmails.txt 

#cfccfca8a55b497f9f3c5b22a9cd132a