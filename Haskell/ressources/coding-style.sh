# Run the command and capture its output
output=$(./ressources/lambdananas ./)

# Check if the output is not empty
if [ -n "$output" ]; then
    exit 84
else
    exit 0
fi