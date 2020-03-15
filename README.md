Scripts working with F5 API
1. asm-policy ----- List asm plicy and hash value
2. vs-pool  ----- List VS, address:port and pool mapping.

example output:

VS名称 -------> VS IP端口 ---------------> pool名称 -------> pool members

vs_http ---> /Common/10.1.10.100:80 ---> /Common/pool-1 ---> ['/Common/10.1.20.1:80', '/Common/10.1.20.2:80']
vs_https ---> /Common/10.1.10.101:443 ---> /Common/pool-2 ---> ['/Common/10.1.20.3:443', '/Common/10.1.20.4:443']
