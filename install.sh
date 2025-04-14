#!/bin/bash

echo "Installing NazovJazyka..."
mkdir -p ~/.lanx
cp compiler/nzj /usr/local/bin/lanx
chmod +x /usr/local/bin/lanx
echo "LanX installed to /usr/local/bin."
