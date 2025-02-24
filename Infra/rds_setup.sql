create schema transactions;

create table transactions.fraud(
transaction_id varchar,
user_id varchar,
amount decimal,
location varchar,
device_id varchar,
timestamp varchar
);