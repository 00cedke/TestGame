#!/bin/bash

if ! docker ps --format '{{.Names}}' | grep -q "^mongodb$"; then
    echo "Starting a MongoDB container named 'mongodb'..."
    docker run -d --name mongodb -p 27017:27017 mongo:4.4
else
    echo "MongoDB container is already running."
fi

sleep 5

echo "Creating database 'mygame' and collection 'players'..."
docker exec mongodb mongo --eval "
    use mygame;
    db.createCollection('players');
"

echo "Database 'mygame' with collection 'players' created successfully."
