app: terminal
tag: user.nix_cli
-

nix firewall help:
    insert("nixos-firewall-tool --help\n")

nix firewall show:
    insert("sudo nixos-firewall-tool show\n")

nix firewall open T C P <user.number_string>:
    insert("sudo nixos-firewall-tool open tcp {number_string}\n")

nix firewall open U D P <user.number_string>:
    insert("sudo nixos-firewall-tool open udp {number_string}\n")

nix firewall reset:
    insert("sudo nixos-firewall-tool reset\n")
