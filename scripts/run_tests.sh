#/bin/bash

set -eo pipefail


main() {
    env pytest tests
}

main "$@"
