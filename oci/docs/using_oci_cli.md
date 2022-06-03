# Use session to create profile
ref: https://learn.hashicorp.com/tutorials/terraform/oci-build?in=terraform/oci-get-started <br/>

```oci session authenticate```

# oci cli / jq
```
#list all instances

oci compute instance list --compartment-id ocid1.compartment.oc1..aaaaaaaadmtdep3rn7qwjgwjektj4cz7t4x5d5ejhvru6xvsqiqio5vfn6ha

#detach a vnic

oci compute instance detach-vnic --compartment-id ocid1.compartment.oc1..aaaaaaaadmtdep3rn7qwjgwjektj4cz7t4x5d5ejhvru6xvsqiqio5vfn6ha --vnic-id ocid1.vnic.oc1.phx.abyhqljt34pd5sre3za34b2wtcyxii5zm5rkw62aneil3yg75jrdl2jes4iq --wait-for-state DETACHED --force

#List all vnics

oci compute instance list-vnics --compartment-id ocid1.compartment.oc1..aaaaaaaadmtdep3rn7qwjgwjektj4cz7t4x5d5ejhvru6xvsqiqio5vfn6ha --instance-id ocid1.instance.oc1.phx.anyhqljt6if7otacsotd3ub6sadva7lywaov7dflf2ly5ztnf65knzgcwklq

#Get vnic

oci compute instance list-vnics --compartment-id ocid1.compartment.oc1..aaaaaaaadmtdep3rn7qwjgwjektj4cz7t4x5d5ejhvru6xvsqiqio5vfn6ha --instance-id ocid1.instance.oc1.phx.anyhqljt6if7otacsotd3ub6sadva7lywaov7dflf2ly5ztnf65knzgcwklq |jq .data[0].id

#Attach vnic

oci compute instance attach-vnic --instance-id ocid1.instance.oc1.phx.anyhqljt6if7otacsotd3ub6sadva7lywaov7dflf2ly5ztnf65knzgcwklq --subnet-id ocid1.subnet.oc1.phx.aaaaaaaakofdgupw6ixycifnp3pgkxd55wvkzbtwpamdvhoy3engqzekyfha

#List vnics

oci compute instance list-vnics --compartment-id ocid1.compartment.oc1..aaaaaaaadmtdep3rn7qwjgwjektj4cz7t4x5d5ejhvru6xvsqiqio5vfn6ha --instance-id ocid1.instance.oc1.phx.anyhqljt6if7otacsotd3ub6sadva7lywaov7dflf2ly5ztnf65knzgcwklq |jq '.data[] | select(."is-primary" == false)' | jq -r '.id'

#Get vnic

vnic=`oci compute instance list-vnics --compartment-id ocid1.compartment.oc1..aaaaaaaadmtdep3rn7qwjgwjektj4cz7t4x5d5ejhvru6xvsqiqio5vfn6ha --instance-id ocid1.instance.oc1.phx.anyhqljt6if7otacsotd3ub6sadva7lywaov7dflf2ly5ztnf65knzgcwklq |jq '.data[] | select(."is-primary" == false)' | jq -r '.id'
```
# get display name
 oci compute instance list -c $C | jq '.data[0]."display-name"'

# Get cluster information
```
oci compute-management cluster-network list | jq .data[].id
oci compute-management cluster-network list | jq .data[].\"display-name\"
```

# Object store

```
oci os bucket list
{
}

## --file is name of downloaded file
oci os object get --bucket-name "canary" --name "hpc-canary-test-2.json" --file "rik.json"

```
Uploads bulk
```
oci os object bulk-upload  --bucket-name hpc-images --src-dir . 
oci os object bulk-download --bucket-name hpc-images 
oci compute instance list --profile HPC_DEFAULT_COMPUTE_DEV --compartment-id $C

export C="ocid1.t.oc1..buq"
oci os bucket list --profile HPC_DEFAULT_COMPUTE_DEV -ns hpc -c $C
oci os object bulk-upload --profile HPC_DEFAULT_COMPUTE_DEV --bucket-name hpc-images-compute --src-dir .  --no-overwrite
```

# Research query hacks
ref: https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm <br>
```
query
  instance resources matching "notable-poodle"
```

#use WR to find BM time created
``` 
oci work-requests work-request list --compartment-id ocid1.compartment.region1..aaaaaaaap4af444xs5zfenrudblsd7li3bi56ovmcb3akuqlr64cz52gf3jq --resource-id ocid1.instance.region1.sea.anzwkljsnjq7b6yclyp54yuee24mer2iuyo4ambd3xiyjcywzkpznwet6gcq
```
