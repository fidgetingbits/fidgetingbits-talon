firewall list all: "sudo iptables-nft -L\n"

firewall flush ruleset: "nft flush ruleset\n"
