#!/bin/bash
cd /Users/atharvalepse/Documents/Luxora
export PATH="/Users/atharvalepse/.nvm/versions/node/v24.14.1/bin:$PATH"
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npm run dev
