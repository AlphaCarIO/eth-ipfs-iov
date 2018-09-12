#####
##Makefile for Ethereum Test Env
#####

.PHONY : test ropsten
.IGNORE : del_test_geth ropsten

DATADIR=./eth_node/test_ethereum

del_eth:
	cd $(DATADIR) && ls |grep -v keystore| xargs rm -rf && rm -rf geth.log

attach:
	geth attach $(DATADIR)/geth.ipc

bn:
	cd nginx && ./cp_dist.sh
	docker-compose -f docker-compose_nginx.yml build

r_nginx:
	docker-compose -f docker-compose_nginx.yml restart nginx
