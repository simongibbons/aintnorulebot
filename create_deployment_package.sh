#! /bin/bash

pushd package
zip -r9 ../function.zip .
popd

zip -gr9 function.zip aintnorulebot
