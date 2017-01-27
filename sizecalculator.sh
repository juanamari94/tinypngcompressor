#!/bin/sh
echo "Size in KB"
echo $(du -shk $1)
echo $(du -shk $2)
