# Set / Get max clock for graphics

ref: https://nvidia.custhelp.com/app/answers/detail/a_id/3751/~/useful-nvidia-smi-queries

``
sudo nvidia-smi -lgc `nvidia-smi --query-supported-clocks=gr --format=nounits,noheader,csv | sort -n | tail -1`
``
