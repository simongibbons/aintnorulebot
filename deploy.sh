#! /bin/bash

aws lambda update-function-code --function-name hello_world --zip fileb://function.zip --region eu-west-1

