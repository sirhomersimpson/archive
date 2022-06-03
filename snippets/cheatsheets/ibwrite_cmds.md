# GPU Shapes

## client
``
./ib_write_bw -F -x 3 -T 105 -S 5 -m 4096 -q 1 -R -b -d mlx5_6 -p 18515 176.16.0.193 -D 10 --report_gbits --perform_warm_up --retry_count=10 --use_cuda=0
``

## server 
``
./ib_write_bw -x 3 -T 105 -S 5 -b -F -m 4096 -R -d mlx5_6 -p 18515 -D 10 --report_gbits --perform_warm_up --retry_count=10 --use_cuda=0
``
