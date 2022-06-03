#!/bin/bash
set -x

# ref: https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html
aws s3api get-object --bucket rikawsbuckets --key script.sh script_new.sh

expected_output=(
"
{
    "AcceptRanges": "bytes",
    "LastModified": "2022-05-09T17:34:20+00:00",
    "ContentLength": 818,
    "ETag": "\"829430053d953d824f01fc92f6186a9e\"",
    "ContentType": "application/x-shellscript",
    "Metadata": {}
}
"
)
