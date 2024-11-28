tag: terminal
-

G cloud activate: "gcloud auth activate-service-account --key-file "

G cloud mount [{user.gcloud_buckets}]:
    insert("gcsfuse ")
    insert(gcloud_buckets or "")

G cloud bucket {user.gcloud_buckets}: "{gcloud_buckets}"
G cloud bucket full {user.gcloud_buckets}: "gs://{gcloud_buckets}"
G cloud list buckets: "gsutil ls\n"
G cloud list [{user.gcloud_buckets}]:
    insert("gsutil ls ")
    if gcloud_buckets: insert("gs://{gcloud_buckets}")
G cloud list clip: "gsutil ls "
    edit.paste()
    key(enter)

