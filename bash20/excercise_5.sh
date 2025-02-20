#!/bin/bash

read -p "Enter first number: " a
read -p "Enter second number: " b
read -p "Enter operation (+, -, *, /): " op

case $op in
    "+")
        echo "Result: $((a + b))"
        ;;
    "-")
        echo "Result: $((a - b))"
        ;;
    "*")
        echo "Result: $((a * b))"
        ;;
    "/")
        if [ $b -eq 0 ]; then
            echo "Division by zero is not allowed"
        else
            echo "Result: $((a / b))"
        fi
        ;;
    *)
        echo "Invalid operation"
        ;;
esac
