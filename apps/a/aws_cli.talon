app: terminal
tag: user.aws_cli
-

A W S version: "aws --version\n"
A W S help: "aws --no-paginate help\n"
A W S configure: "aws configure\n"

A W S S T S get caller identity: "aws sts get-caller-identity\n"
A W S S T S get access key info:
    "aws sts get-access-key-info --access-key-info "
    edit.paste()
    key(enter)

# S3 Bucket
A W S [S three] bucket help: "aws --no-paginate s3 help\n"
A W S [S three] bucket list help: "aws --no-paginate s3 ls help\n"
A W S [S three] bucket list: "aws s3 ls\n"
A W S [S three] bucket list clip:
    "aws s3 ls "
    edit.paste()
    key(enter)
