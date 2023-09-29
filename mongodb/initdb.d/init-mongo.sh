#!/bin/bash
set -e

mongosh <<EOF
use admin
db.createUser(
  {
    user: "${MONGO_INITDB_USER}",
    pwd: "${MONGO_INITDB_PWD}",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)

use ${MONGO_INITDB_DATABASE}
db.createCollection("projects")
db.projects.createIndex()
EOF