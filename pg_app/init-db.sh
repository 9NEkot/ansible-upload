#!/bin/bash
set -e

psql  --username dj_user <<-EOSQL
    CREATE DATABASE testdb;
    GRANT UPDATE ON testdb to dj_user
EOSQL
