# Loops
```
for (( i=0; i<${#array[@]}; i++ )); do echo $i ;done
```
```
for h_id in a b c ; do echo $h_id; done
```
```
### count of array items
echo ${#array[@]}
```

# Read file

```
 while IFS= read -r ip;
  do
    echo $ip
   
  done < "$IP_FILE"
```
# Seq
```
for n in `seq 1 18`
do
   np=$(($n*8))
   hosts=`seq -f "hpc%g:8" -s"," 1 $n`
done
```
# scp
```
for ip in `cat b4_ips`; do echo $ip; scp debian@${ip}:/tmp/g* . ; done
```
