tag: terminal
-

(cert|certificate) show: "openssl x509 -in "
(cert|certificate) show expiry: "openssl x509 -enddate -noout -in "
(cert|certificate) show fingerprint [<user.zsh_file_completion>]:
    insert("openssl x509 -fingerprint -sha256 -noout -in ")
    insert(zsh_file_completion or "")
