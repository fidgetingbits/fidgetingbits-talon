tag: user.nftables
-
firewall list all: "sudo iptables-nft -L --line-numbers\n"

firewall delete rule numb <number>: user.insert_between("sudo iptables-nft -D ", "{number}")

firewall flush rules: "nft flush ruleset\n"
