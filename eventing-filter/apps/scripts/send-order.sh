#!/bin/bash

if ! command -v kn &> /dev/null
then
    echo "kn CLI could not be found!"
    exit
fi

while getopts c:a: flag
do
    case "${flag}" in
        c) customer_name=${OPTARG};;
        a) amount=${OPTARG};;
    esac
done

if [ -z "$customer_name" ] || [ -z "$amount" ]
then
    echo "Please provide the following parameters:"
    echo "  -c (string)"
    echo "  -a (int)"
    echo "For example: -c John -a 100"
    exit
fi

if ! command -v uuidgen &> /dev/null
then
    ORDER_ID=$RANDOM
else
    ORDER_ID=$(uuidgen)
fi

ORDERS_PROCESSOR_URL=$(kn service describe order-processor -o url)

echo
echo "Sending Order..."
echo "  - ID: $ORDER_ID"
echo "  - Customer: $customer_name";
echo "  - Amount: $amount";
echo

curl -XPOST "$ORDERS_PROCESSOR_URL/order/process" \
    -H 'Content-Type: application/json' \
    -d "{\"id\": \"$ORDER_ID\", \"customer\": \"$customer_name\", \"amount\": $amount }"
