#!/bin/bash

set -eu -o pipefail

TIMEFORMAT='%R'
DAY=${1:-day*}
FAILURERET=${2:-}

rundaypart() {
    if [ -f "$1"/"$2".py ]; then
        echo -n "Running $1 $2... "
        t=$({
            time python -Bbb "$1"/"$2".py <"$1"/input.txt || return "${FAILURERET:-$?}"
        } 2>&1)
        echo "${t}s"
    else
        echo "Missing $1 $2"
    fi
}

for day in $DAY; do
    rundaypart "${day}" part1
    rundaypart "${day}" part2
done
