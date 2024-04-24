not os: windows
and tag: terminal
-

# disk management
<user.drive> (usage | space): "df -h\n"
<user.drive> list: "lsblk\n"
<user.drive> file systems: "lsblk -f\n"
<user.drive> mounted: "mount\n"
<user.drive> mount: "mount "
<user.drive> mount list: "mount | rg '^/'\n"
<user.drive> mount list fuse: "mount | rg fuse\n"
<user.drive> mount list all: "mount\n"
<user.drive> (unmount | U mount): "umount "

<user.drive> F stab: "cat /etc/fstab\n"
<user.drive> remount temp (exec | executable): "mount /tmp -o remount,exec"

swap on: "swapon "
swap off: "swapoff "
swap make: "mkswap "

<user.drive> key dump: "sudo cryptsetup luksDump /dev/"
<user.drive> key add: "sudo cryptsetup luksAddKey --key-slot "
<user.drive> enroll pass key: "sudo systemd-cryptenroll --fido2-device auto /dev/"

# FIXME: abstract this to use per-device paths
<user.drive> mount nix volume: "sudo mount /dev/mapper/encrypted-nixos"
