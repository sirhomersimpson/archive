#How to read a file line by line
export INPUT_FILE="tenants.txt"
export AIRPORT_CODE="iad1"

while IFS= read -r TENANT_OCID
do
  echo "$TENANT_OCID"
done < ${INPUT_FILE}
