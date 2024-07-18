sudo -u postgres psql

CREATE DATABASE user_accounts;
CREATE USER kennykguo WITH PASSWORD 'rex25244';
ALTER ROLE kennykguo SET client_encoding TO 'utf8';
ALTER ROLE kennykguo SET default_transaction_isolation TO 'read committed';
ALTER ROLE kennykguo SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE user_accounts TO kennykguo;